from django.contrib import admin
from django.urls import path
from .views import RegisterView, MoviesView, CollectionAPIView, UpdateCollectionView, RequestView, request_reset


urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('movies/', MoviesView.as_view(), name='movies'),
    path('collection/', CollectionAPIView.as_view(), name='collection'),
    path('collection/<int:pk>/', UpdateCollectionView.as_view(), name='collection_detail'),
    path('request-count/', RequestView.as_view(), name='request-count'),
    path('request-count/reset', request_reset, name='reset'),
]