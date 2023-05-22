from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import FreeArticle, TogetherArticle, FreeComment, TogetherComment
from .serializers.community import FreeArticleSerializer, FreeCommentSerializer, TogetherArticleSerializer, TogetherCommentSerializer, FreeArticleListSerializer, TogetherArticleListSerializer
	
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def free_article(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(FreeArticle)
        serializer = FreeArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FreeArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def free_detail(request, article_pk):
    article = get_object_or_404(FreeArticle, pk=article_pk)

    if request.method == 'GET':
        serializer = FreeArticleListSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        # 작성자와 로그인한 사용자 비교
        if article.user == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 작성자와 로그인한 사용자 비교
        if article.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = FreeArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def together_article(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(TogetherArticle)
        serializer = TogetherArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TogetherArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def together_detail(request, article_pk):
    article = get_object_or_404(TogetherArticle, pk=article_pk)

    if request.method == 'GET':
        serializer = TogetherArticleListSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        # 작성자와 로그인한 사용자 비교
        if article.user == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 작성자와 로그인한 사용자 비교
        if article.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = TogetherArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)