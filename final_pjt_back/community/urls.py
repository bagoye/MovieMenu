from django.urls import path
from . import views

urlpatterns = [
    path('free/', views.free_article),
    path('free/<int:article_pk>', views.free_detail),
    path('together/', views.together_article),    
    path('together/<int:article_pk>', views.together_detail),
]