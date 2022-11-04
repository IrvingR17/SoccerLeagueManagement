from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from .models import CustomUser

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = '__all__'

class UserSelializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    user = UserSelializer()

    class Meta: 
        model = Players
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    user = UserSelializer()

    class Meta: 
        model = Team_Owner
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        player = Players.objects.create(**validated_data, user=user)
        return player

class LeaguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = '__all__'

class LeagueSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Leagues
        fields = '__all__'

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'



















