from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import PlayerSerializer
from .models import Players

class ListPlayersView(ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Players.objects.all()

class CreatePlayerView(CreateAPIView):
    serializer_class = PlayerSerializer
