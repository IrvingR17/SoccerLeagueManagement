from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from .models import CustomUser

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
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

class TeamPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayerRecords
        fields = '__all__'




class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name']

class PlayerTeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(read_only=True)

    class Meta:
        model = TeamPlayerRecords
        fields = ['players']
















