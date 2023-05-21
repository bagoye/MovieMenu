from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import FreeArticle, TogetherArticle, FreeComment, TogetherComment
from .serializers.community import FreeArticleSerializer, FreeCommentSerializer, TogetherArticleSerializer, TogetherCommentSerializer, FreeArticleListSerializer
	
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


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
    

# 상세 FreeArticle 페이지
@api_view(['GET', 'DELETE', 'PUT'])
def free_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(FreeArticle, pk=article_pk)

    if request.method == 'GET':
        serializer = FreeArticleListSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FreeArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
