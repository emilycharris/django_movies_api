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

    movie = serializers.HyperlinkedRelatedField(read_only=True, view_name="movie-detail")
    rater = serializers.HyperlinkedRelatedField(read_only=True, view_name="rater-detail")

    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = ['rater', 'movie', 'display_name', 'rating', 'timestamp']

    def get_display_name(self, rating):
        return rating.movie.title
