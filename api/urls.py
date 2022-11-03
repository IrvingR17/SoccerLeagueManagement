from django.urls import include, path
from .views import CreatePlayerView, ListPlayersView, LeaguesListView, LeaguesCreateView, LeagueRetrieveView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('players/create/', CreatePlayerView.as_view(), name="create-player"),
    path('players/list/', ListPlayersView.as_view(), name="list-players"),
    path('leagues/list/', LeaguesListView.as_view(), name="leagues-list"),
    path('leagues/list/<int:id>', LeagueRetrieveView.as_view(), name="league-list"),
    path('leagues/create/', LeaguesCreateView.as_view(), name="leagues-create"),
]
