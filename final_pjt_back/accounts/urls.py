from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('profile/<username>/follow/', views.follow),
    path('profile/<int:username>/', views.get_my_profile),
]