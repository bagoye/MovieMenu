from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer
from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['POST'])
# @permission_classes([AllowAny])
def follow(request, username):
    profile_user = get_object_or_404(get_user_model(), username=username)
    profile = profile_user.profile
    me = request.user

    if me != profile_user:
        if me.followings.filter(pk=profile_user.pk).exists():
            # 언팔로우
            me.followings.remove(profile_user)
        else:
            # 팔로우
            me.followings.add(profile_user)

    serializer = ProfileSerializer(profile) 
    return Response(serializer.data)

@api_view(['GET'])
def get_my_profile(request):
    me = request.user
    profile = me.profile

    serializer = ProfileSerializer(profile)
    return Response(serializer.data)