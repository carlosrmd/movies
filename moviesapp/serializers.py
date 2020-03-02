from rest_framework import serializers
from .models import Movie, Person


class SubPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name']


class MovieSerializer(serializers.ModelSerializer):
    casting = SubPersonSerializer(many=True, read_only=True)
    directors = SubPersonSerializer(many=True, read_only=True)
    producers = SubPersonSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_year', 'casting', 'directors', 'producers']


class SubMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_year']


class PersonSerializer(serializers.ModelSerializer):
    movies_as_acting = SubMovieSerializer(many=True, read_only=True)
    movies_as_director = SubMovieSerializer(many=True, read_only=True)
    movies_as_producer = SubMovieSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'movies_as_acting', 'movies_as_director', 'movies_as_producer']

