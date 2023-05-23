from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
from .models import Movie, Genre, Actor, MovieReview
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie
from .serializers.movie import MovieListSerializer, MovieReviewSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', ])
def popular(request):
    movie_data = Movie.objects.all().order_by('-popularity')[:50]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def vote_average(request):
    movie_data = Movie.objects.all().order_by('-vote_average')[:50]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def adventure(request):
    movie_data = Movie.objects.filter(genres__pk=12)[:50]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def action(request):
    movie_data = Movie.objects.filter(genres__pk=28)[:50]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def sf(request):
    movie_data = Movie.objects.filter(genres__pk=878)[:50]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def allmovie(request):
    movie_data = Movie.objects.all()[:50]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def alonemovie(request):
    genre_pks = [18, 9648, 14, 35]
    movie_data = Movie.objects.filter(genres__pk__in=genre_pks)[:180]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def lovermovie(request):
    genre_pks = [10749, 10402, 35, 27]
    movie_data = Movie.objects.filter(genres__pk__in=genre_pks)[:180]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def friendmovie(request):
    genre_pks = [28, 80, 53, 878]
    movie_data = Movie.objects.filter(genres__pk__in=genre_pks)[:180]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def familymovie(request):
    genre_pks = [16, 10751, 18, 12]
    movie_data = Movie.objects.filter(genres__pk__in=genre_pks)[:180]
    serializer = MovieListSerializer(movie_data, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    actors_data = []
    for actor in movie.actors.all():
        actor_data = {
            'name': actor.name,
            'profile_path': actor.profile_path.url if actor.profile_path else None
        }
        actors_data.append(actor_data)
    
    directors_data = []
    for director in movie.directors.all():
        director_data = {
            'name': director.name,
            'profile_path': director.profile_path.url if director.profile_path else None
        }
        directors_data.append(director_data)
    
    movie_data = {
        'title': movie.title,
        'release_date': movie.release_date,
        'runtime': movie.runtime,
        'youtube_key': movie.youtube_key,
        'vote_average': movie.vote_average,
        'overview': movie.overview,

        # 다른 필드들도 필요에 따라 추가
        'actors': actors_data,
        'directors': directors_data
    }
    
    return JsonResponse(movie_data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        reviews = movie.movie_reviews.all()
        serializer = MovieReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 리뷰 CREATE / READ / DELETE / UPDATE
# @api_view(['GET', 'POST', 'PUT', ])
# @permission_classes([IsAuthenticated])
# def movie_review(request, movie_pk):
#     movie = get_object_or_404(Movie, id=movie_pk)
#     if request.method == 'GET':
#         reviews = get_list_or_404(MovieReview)
#         serializer = MovieReviewSerializer(reviews, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MovieReviewSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user, movie=movie)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'PUT':
    #     serializer = MovieReviewSerializer(reviews, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
