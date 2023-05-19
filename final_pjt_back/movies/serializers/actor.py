from rest_framework import serializers
from movies.models import Actor
from django.contrib.auth import get_user_model

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'