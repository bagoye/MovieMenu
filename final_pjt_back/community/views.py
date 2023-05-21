from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import FreeArticle, TogetherArticle, FreeComment, TogetherComment
from .serializers.community import FreeArticleSerializer, FreeCommentSerializer, TogetherArticleSerializer, TogetherCommentSerializer, FreeArticleListSerializer
	
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def free_article(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(FreeArticle)
        serializer = FreeArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FreeArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def together_article() {
  
# }