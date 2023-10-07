from rest_framework import serializers
from .models import CustomUser, Collection, Movie

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genres', 'uuid']

    def create(self, validated_data):
        collection = Collection.objects.get(**validated_data)
        for movie_data in validated_data:
            Movie.objects.create(collection=collection, **movie_data)

        return Movie



class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, required=False)

    class Meta:
        model = Collection
        fields = ['title', 'description', 'movies']

    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        collection = Collection.objects.create(**validated_data)
        for movie_data in movies_data:
            Movie.objects.create(collection=collection, **movie_data)

        return collection

