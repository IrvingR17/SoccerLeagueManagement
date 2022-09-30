from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import UserPlayerSerializer

class CreatePlayerView(CreateAPIView):
    serializer_class = UserPlayerSerializer
