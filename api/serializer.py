from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from .models import CustomUser

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = '__all__'

class LeaguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = '__all__'

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'



















