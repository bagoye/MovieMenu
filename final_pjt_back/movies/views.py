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


# 리뷰 CREATE / READ / DELETE / UPDATE
@api_view(['GET', 'POST', 'PUT', ])
@permission_classes([IsAuthenticated])
def movie_review(request, movie_id):
    if request.method == 'GET':
        reviews = get_list_or_404(MovieReview)
        serializer = MovieReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie_id = request.data.get('movie_id')
        serializer = MovieReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie_id=movie_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = MovieReviewSerializer(reviews, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# ------------------- json 데이터 가져오기---------------------------

# TMDB API KEY 작성
# API_KEY = '779716af9004289d5cc205ea82476fab'


# GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
# POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'
# UPCOMING_MOVIE_URL = 'https://api.themoviedb.org/3/movie/upcoming'
# TOP_RATED_MOVIE_URL = 'https://api.themoviedb.org/3/movie/top_rated'

# def get_directors(movie):
#     movie_id = movie.id
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#         }
#     ).json()

#     for person in response.get('crew'):
#         director_id=person.get ('id')
#         if not Director.objects.filter(pk=director_id).exists():
#             director = Director.objects.create(
#                 id=person.get('id'),
#                 name=person.get('name'),
#                 profile_path = person.get('profile_path')
#             )
#         movie.directors.add(director_id)
#         if movie.directors.count() == 1:
#             break


# def tmdb_genres():
#     response = requests.get(
#         GENRE_URL,
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-KR',            
#         }
#     ).json()    
#     for genre in response.get('genres'):
#         if Genre.objects.filter(pk=genre['id']).exists(): continue        
#         print(genre)
#         Genre.objects.create(
#             id=genre['id'],
#             name=genre['name']
#         )
#     return JsonResponse(response)


# def get_youtube_key(movie_dict):    
#     movie_id = movie_dict.get('id')
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
#         params={
#             'api_key': API_KEY
#         }
#     ).json()
#     for video in response.get('results'):
#         if video.get('site') == 'YouTube':
#             return video.get('key')
#     return 'nothing'

# def get_runtime(movie_dict):    
#     movie_id = movie_dict.get('id')
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}',
#         params={
#             'api_key': API_KEY
#         }
#     ).json()
#     runtime = response.get('runtime')
#     return runtime


# def get_actors(movie):
#     movie_id = movie.id
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#         }
#     ).json()

#     for person in response.get('cast'):
#         if person.get('known_for_department') != 'Acting': continue
#         actor_id = person.get('id')
#         if not Actor.objects.filter(pk=actor_id).exists():
#             actor = Actor.objects.create(
#                 id=person.get('id'),
#                 name=person.get('name'),
#                 profile_path = person.get('profile_path'),
#                 character = person.get('character')
#             )
#         movie.actors.add(actor_id)
#         if movie.actors.count() == 5:
#             break

# def popular_movie_data(page=1):
#     response = requests.get(
#         POPULAR_MOVIE_URL,
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',     
#             'page': page,       
#         }
#     ).json()

#     for movie_dict in response.get('results'):
#         if not movie_dict.get('release_date'): continue   # 없는 필드 skip
#         # 유투브 key 조회
#         youtube_key = get_youtube_key(movie_dict)
#         runtime = get_runtime(movie_dict)

#         movie = Movie.objects.create(
#             id=movie_dict.get('id'),
#             title=movie_dict.get('title'),
#             release_date=movie_dict.get('release_date'),
#             popularity=movie_dict.get('popularity'),
#             vote_count=movie_dict.get('vote_count'),
#             vote_average=movie_dict.get('vote_average'),
#             overview=movie_dict.get('overview'),
#             poster_path=movie_dict.get('poster_path'),   
#             youtube_key=youtube_key,
#             runtime=runtime,
#         )
#         for genre_id in movie_dict.get('genre_ids', []):
#             movie.genres.add(genre_id)

#         # 배우들 저장
#         get_actors(movie)
#         get_directors(movie)
#         print('>>>', movie.title, '==>', movie.youtube_key)


# def upcoming_movie_data(page=1):
#     response = requests.get(
#         UPCOMING_MOVIE_URL,
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',     
#             'page': page,       
#         }
#     ).json()

#     for movie_dict in response.get('results'):
#         if not movie_dict.get('release_date'): continue   # 없는 필드 skip
#         # 유투브 key 조회
#         youtube_key = get_youtube_key(movie_dict)
#         runtime = get_runtime(movie_dict)

#         movie = Movie.objects.create(
#             id=movie_dict.get('id'),
#             title=movie_dict.get('title'),
#             release_date=movie_dict.get('release_date'),
#             popularity=movie_dict.get('popularity'),
#             vote_count=movie_dict.get('vote_count'),
#             vote_average=movie_dict.get('vote_average'),
#             overview=movie_dict.get('overview'),
#             poster_path=movie_dict.get('poster_path'),   
#             youtube_key=youtube_key,
#             runtime=runtime,
#         )
#         for genre_id in movie_dict.get('genre_ids', []):
#             movie.genres.add(genre_id)

#         # 배우들 저장
#         get_actors(movie)
#         get_directors(movie)
#         print('>>>', movie.title, '==>', movie.youtube_key)

# def top_rated_movie_data(page=1):
#     response = requests.get(
#         TOP_RATED_MOVIE_URL,
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',     
#             'page': page,       
#         }
#     ).json()

#     for movie_dict in response.get('results'):
#         if not movie_dict.get('release_date'): continue   # 없는 필드 skip
#         # 유투브 key 조회
#         youtube_key = get_youtube_key(movie_dict)
#         runtime = get_runtime(movie_dict)

#         movie = Movie.objects.create(
#             id=movie_dict.get('id'),
#             title=movie_dict.get('title'),
#             release_date=movie_dict.get('release_date'),
#             popularity=movie_dict.get('popularity'),
#             vote_count=movie_dict.get('vote_count'),
#             vote_average=movie_dict.get('vote_average'),
#             overview=movie_dict.get('overview'),
#             poster_path=movie_dict.get('poster_path'),   
#             youtube_key=youtube_key,
#             runtime=runtime,
#         )
#         for genre_id in movie_dict.get('genre_ids', []):
#             movie.genres.add(genre_id)

#         # 배우들 저장
#         get_actors(movie)
#         get_directors(movie)
#         print('>>>', movie.title, '==>', movie.youtube_key)

# def popular_tmdb_data(request):
#     Genre.objects.all().delete()
#     Actor.objects.all().delete()
#     Movie.objects.all().delete()
#     Director.objects.all().delete()

#     tmdb_genres()
#     for i in range(1, 21):
#         popular_movie_data(i)
#     return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# def top_rated_tmdb_data(request):
#     Genre.objects.all().delete()
#     Actor.objects.all().delete()
#     Movie.objects.all().delete()
#     Director.objects.all().delete()

#     tmdb_genres()
#     for i in range(1, 21):
#         top_rated_movie_data(i)
#     return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# def upcoming_tmdb_data(request):
#     Genre.objects.all().delete()
#     Actor.objects.all().delete()
#     Movie.objects.all().delete()
#     Director.objects.all().delete()

#     tmdb_genres()
#     for i in range(1, 21):
#         upcoming_movie_data(i)
#     return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')