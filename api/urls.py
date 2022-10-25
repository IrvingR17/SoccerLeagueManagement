from django.urls import path
from .views import CreatePlayerView, ListPlayersView

urlpatterns = [
    path('players/create/', CreatePlayerView.as_view(), name="create-player"),
    path('players/list/', ListPlayersView.as_view(), name="list-players")
]
