from django.urls import include, path
from .views import CreatePlayerView, ListPlayersView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('players/create/', CreatePlayerView.as_view(), name="create-player"),
    path('players/list/', ListPlayersView.as_view(), name="list-players"),
]
