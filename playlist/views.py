from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import CollectionSerializer, MovieSerializer, UserSerializer
from.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from dotenv import load_dotenv
from collections import Counter
import os
import requests
from .middleware import RequestMiddleware
from django.http import *
from rest_framework.decorators import api_view
import json


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {

                'access': str(refresh.access_token),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MoviesView(APIView):

    def get(self, request, format=None):

        load_dotenv('.env')
        username = os.getenv('username')
        password = os.getenv('password')

        try:
            headers = {
                "Content-Type": "application/json",
                "username": username,
                "Password": password,
                "User-Agent": "PostmanRuntime/7.33.0"
            }

            i = 0
            while i <= 5:
                resp = requests.post('https://demo.credy.in/api/v1/maya/movies', headers=headers, verify=False)
                if resp.status_code == 200:
                    return Response(resp.json())
                else:
                    i += 1
            else:
                data = {
                    'error': 'Exception occured in API',
                    'status_code': 404,
                }
                resp = json.dumps(data)
                return Response(resp)
        except Exception as e:
            resp = {
                'error': 'Exception occured as' + str(e),
            }
            resp = json.dumps(resp)
            return Response(resp)






class CollectionAPIView(APIView):

    def top_three(self):
        collections_with_movies = Collection.objects.prefetch_related('movies').all()
        all_genres = []
        for collection in collections_with_movies:
            for movie in collection.movies.all():
                genres = movie.genres.split(',')
                all_genres.extend([genre.strip() for genre in genres if genre])
        genre_counts = Counter(all_genres)
        top_genres = genre_counts.most_common(3)
        favorite_genres = ', '.join([genre[0] for genre in top_genres])
        return favorite_genres


    def get(self, request, *args, **kwargs):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)

        favorite_genres = self.top_three()
        if serializer.data:

            response_data = {
                "is_success": True,
                "data": {
                    "collections": serializer.data,
                    "favourite_genres": favorite_genres,
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)
        resp = {
            'error': 'No collection found'
        }
        return Response(resp)



    def post(self, request, format=None):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCollectionView(APIView):

    def get_object(self, pk):
        try:
            instance = Collection.objects.get(pk=pk)
            return instance
        except Collection.DoesNotExist as e:
            return e
    def get(self, request, pk):
        try:
            instance = self.get_object(pk)
            movies_in_collection = instance.movies.all()
            movies = [movie.title for movie in movies_in_collection]

            response_data = {
                "data": {
                    "title": instance.title,
                    "description": instance.description,
                    "movies": movies,
                }
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'error': str(e)
            }
            data = json.dumps(response_data)
            return Response(data)


    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            if 'title' in serializer.validated_data:
                instance.title = serializer.validated_data['title']
            if 'description' in serializer.validated_data:
                instance.description = serializer.validated_data['description']
            if 'movies' in serializer.validated_data:
                updated_movies = serializer.validated_data['movies']
                for i in updated_movies:
                    Movie.objects.create(collection=instance,**i)
            instance.save()

            return Response({"message": "Resource updated successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = self.get_object(pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            resp = {
                'error': 'Object not found'
            }
            data = json.dumps(resp)
            return Response(data)

class RequestView(APIView):

    def get(self, request):
        obj = RequestCount.objects.get(id=1)
        data = {
            'requests': obj.count
        }
        return JsonResponse(data)


@api_view(['POST'])
def request_reset(request):

    if request.method == 'POST':
        RequestMiddleware.num_req = 0
        RequestCount.objects.filter(pk=1).update(count=0)
        data = {
            'message': 'request count reset Successfully'
        }
        return JsonResponse(data)
