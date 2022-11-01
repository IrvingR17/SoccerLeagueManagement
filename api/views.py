from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import LeaguesSelializer, PlayerSerializer, UserSelializer
from .models import Leagues, Players, CustomUser

class LeaguesListView(ListAPIView):
    serializer_class = LeaguesSelializer
    queryset = Leagues.objects.all()

class LeaguesCreateView(CreateAPIView):
    serializer_class = LeaguesSelializer

class ListPlayersView(ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Players.objects.all()

class CreatePlayerView(CreateAPIView):
    serializer_class = PlayerSerializer
