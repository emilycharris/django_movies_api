from django.shortcuts import render
import json
from django.views.generic import View
from rest_framework import generics
from main.models import Movie, Rater, Rating
from main.serializers import MovieSerializer, RaterSerializer, RatingSerializer
# Create your views here.

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class RaterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer



class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer



class RatingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RaterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
