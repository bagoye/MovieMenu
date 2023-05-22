from django.urls import path
from . import views

urlpatterns = [    
    path('popular/', views.popular),
    path('voteaverage/', views.vote_average),
    path('adventure/', views.adventure),
    path('action/', views.action),
    path('sf/', views.sf),
    path('allmovie/', views.allmovie),
    path('alonemovie/', views.alonemovie),
    path('lovermovie/', views.lovermovie),
    path('friendmovie/', views.friendmovie),
    path('familymovie/', views.familymovie),
    path('<int:movie_pk>/', views.movie_detail),

    path('review/<int:movie_pk>/', views.movie_review),
    # path('review/', views.movie_review),
]
