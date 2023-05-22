from rest_framework import serializers
from movies.models import Movie, MovieReview
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
            
class MovieReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'

    user = UserSerializer(read_only = True)
    class Meta:
        model = MovieReview
        fields = ('pk', 'user', 'content', 'article', 'created_at', 'updated_at')
        read_only_fields = ('article', 'created_at', 'updated_at',)