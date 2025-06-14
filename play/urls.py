from django.urls import path
from . import views

urlpatterns = [
    path('', views.play),
    path('past-games/', views.past_games),
    path('leaderboard/', views.leaderboard),
    path('stats/', views.stats),
]