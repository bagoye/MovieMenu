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
]
