from rest_framework import serializers
# from community.models import Community
from movies.models import *
from django.contrib.auth import get_user_model

User = get_user_model

# 전체, 장르, 