from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializer import *
from .models import *

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.filter(is_manager=True)

class PlayerRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.filter(is_player=True)
    lookup_field = "id"

class TeamPlayerListView(ListAPIView):
    serializer_class = PlayerTeamSerializer
    queryset = TeamPlayerRecords.objects.all()
    lookup_field = "team"

class TeamPlayerCreateView(CreateAPIView):
    serializer_class = TeamPlayerSerializer

class LeaguesListView(ListAPIView):
    serializer_class = LeaguesSerializer
    queryset = Leagues.objects.all()

class LeagueRetrieveView(RetrieveAPIView):
    serializer_class = LeaguesSerializer
    queryset = Leagues.objects.all()
    lookup_field = "id"

class LeaguesCreateView(CreateAPIView):
    serializer_class = LeaguesSerializer

class LeaguesEditView(UpdateAPIView):
    serializer_class = LeaguesSerializer
    queryset = Leagues.objects.all()
    lookup_field = "id"

class LeaguesDeleteView(DestroyAPIView):
    serializer_class = LeaguesSerializer
    queryset = Leagues.objects.all()
    lookup_field = "id"

class TeamListView(ListAPIView):
    serializer_class = teamSerializer
    queryset = Teams.objects.all()

class CreateTeamView(CreateAPIView):
    serializer_class = teamSerializer

class TeamRetrieveView(ListAPIView):
    serializer_class = teamSerializer
    queryset = Teams.objects.all()
    lookup_field = "league_name"

class TeamRetrieveView2(RetrieveAPIView):
    serializer_class = teamSerializer
    queryset = Teams.objects.all()
    lookup_field = "id"

