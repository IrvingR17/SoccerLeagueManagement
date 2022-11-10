from django.urls import include, path
from .views import *

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('managers/list/', UserListView.as_view(), name="user-list"),
    path('players/list/<int:id>', PlayerRetrieveView.as_view(), name="player-list"),
    path('leagues/list/', LeaguesListView.as_view(), name="leagues-list"),
    path('leagues/list/<int:id>', LeagueRetrieveView.as_view(), name="league-list"),
    path('leagues/create/', LeaguesCreateView.as_view(), name="leagues-create"),
    path('leagues/edit/<int:id>', LeaguesEditView.as_view(), name="leagues-edit"),
    path('leagues/delete/<int:id>', LeaguesDeleteView.as_view(), name="leagues-delete"),
    path('teams/list/', TeamListView.as_view(), name="teams-list"),
    path('teams/list/<int:league_name>', TeamRetrieveView.as_view(), name="team-list"),
    path('teams/list2/<int:id>', TeamRetrieveView2.as_view(), name="team-list"),
    path('teams/create/', CreateTeamView.as_view(), name="teams-create"),
    path('team_player/list/<int:team>', TeamPlayerListView.as_view(), name="player-list"),
    path('team_player/create/', TeamPlayerCreateView.as_view(), name="player-create"),
]
