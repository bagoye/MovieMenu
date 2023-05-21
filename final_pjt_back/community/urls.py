from django.urls import path
from . import views

urlpatterns = [
    path('free/', views.free_article),
    # path('together/', views.together_article),
]