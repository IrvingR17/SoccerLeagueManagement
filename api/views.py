from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializer import LeaguesSerializer, PlayerSerializer, UserSerializer
from .models import Leagues, Players, CustomUser

class LeaguesListView(ListAPIView):
    serializer_class = LeaguesSerializer
    queryset = Leagues.objects.all()

class LeagueRetrieveView(RetrieveAPIView):
    serializer_class = LeaguesSerializer
    queryset = Leagues.objects.all()
    lookup_field = "id"

class LeaguesCreateView(CreateAPIView):
    serializer_class = LeaguesSerializer

class ListPlayersView(ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Players.objects.all()

class CreatePlayerView(CreateAPIView):
    serializer_class = PlayerSerializer
