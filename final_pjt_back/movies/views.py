# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from .models import Genre, Movie, Actor, Director, MovieActors, MovieDirectors
# import requests

# # TMDB API KEY 작성
# API_KEY = '779716af9004289d5cc205ea82476fab'

# GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
# POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'
# # DETAIL_MOVIE_URL = f'https://api.themoviedb.org/3/movie/{movie_id}'
# # CREDITS_CRUE_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'


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

# def movie_data(page=1):
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

# def tmdb_data(request):
#     Genre.objects.all().delete()
#     Actor.objects.all().delete()
#     Movie.objects.all().delete()
#     Director.objects.all().delete()

#     tmdb_genres()
#     for i in range(1, 21):
#         movie_data(i)
#     return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')



from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie
from .serializers.movie import MovieListSerializer

@api_view(['GET', ])
def movies(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)