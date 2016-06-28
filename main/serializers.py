from rest_framework import serializers
from main.models import Movie, Rater, Rating


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'video_release_date', 'imdb_url',
        'unknown', 'action', 'adventure', 'animation', 'children', 'comedy', 'crime',
        'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 'musical', 'mystery',
        'romance', 'scifi', 'thriller', 'war', 'western']

class RaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rater
        fields = ['id', 'age', 'gender', 'occupation', 'zip']


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['rater', 'movie', 'rating', 'timestamp']
