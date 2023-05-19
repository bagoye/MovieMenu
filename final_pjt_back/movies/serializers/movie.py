from rest_framework import serializers
from movies.models import Movie, MovieReview
# from .actor import ActorSerializer, ActorListSerializer
# from community.serializers.article import ArticleSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
            
class MovieReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ('movie',)