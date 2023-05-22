from asyncio import format_helpers
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Profile
from django.contrib.auth import get_user_model
from movies.serializers.movie import MovieListSerializer
from community.serializers.community import FreeArticleListSerializer

class ProfileSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        
        class FollowSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'profile',)

        followers = FollowSerializer(read_only=True, many=True)
        followings = FollowSerializer(read_only=True, many=True)
        
        followings_count = serializers.IntegerField(source="followings.count")
        followers_count = serializers.IntegerField(source="followers.count")

        # bookmark_movies = MoviePosterSerializer(read_only=True, many=True)
        # articles = ArticleListSerializer(read_only=True, many=True)
        # comments = CommentListSerializer(read_only=True, many=True)
        
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'