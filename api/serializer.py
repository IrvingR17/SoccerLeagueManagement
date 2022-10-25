from dataclasses import fields
from rest_framework import serializers
from .models import Players, Team_Owner
from .models import CustomUser

class UserSelializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    user = UserSelializer()

    class Meta: 
        model = Players
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        player = Players.objects.create(**validated_data, user=user)
        return player