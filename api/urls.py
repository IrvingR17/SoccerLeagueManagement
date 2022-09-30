from django.urls import path
from .views import CreatePlayerView

urlpatterns = [
    path('create/', CreatePlayerView.as_view(), name="create-player")
]
