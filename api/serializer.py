from rest_framework import serializers
from .models import Players
from django.contrib.auth.models import User

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'

class UserPlayerSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'