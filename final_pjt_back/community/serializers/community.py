from rest_framework import serializers
from community.models import TogetherArticle, TogetherComment, FreeArticle, FreeComment
from django.contrib.auth import get_user_model
from movies.serializers.movie import MovieListSerializer
# User = get_user_model()

class FreeArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeArticle
        fields = '__all__'
        # read_only_fields = ('movie')

class FreeCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = FreeComment
        fields = '__all__'
        # read_only_fields = ('article',)

class FreeArticleSerializer(serializers.ModelSerializer):
    comment_set = FreeCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = FreeArticle
        fields = '__all__'
        read_only_fields = ('user', 'like_users',)


class TogetherArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TogetherArticle
        fields = '__all__'
        # read_only_fields = ('movie')

class TogetherCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TogetherComment
        fields = '__all__'
        # read_only_fields = ('article',)

class TogetherArticleSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    comment_set = FreeCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = TogetherArticle
        fields = '__all__'
        read_only_fields = ('user', 'like_users',)
