from dataclasses import field
from rest_framework import serializers
from .models import Players, Team_Owner
from django.contrib.auth.models import User

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'

class UserPlayerSerializer(serializers.ModelSerializer):
    players = PlayerSerializer()

    class Meta:
        model = User
        fields = '__all__'

class TeamManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Owner
        fields = '__all__'

class UserTeamManagerSerializer(serializers.ModelSerializer):
    team_manager = TeamManagerSerializer()

    class Meta:
        model = User
        fields = '__all__'