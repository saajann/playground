from django.urls import path
from . import views

urlpatterns = [
    path('', views.tris),
    path('game/finished/<int:id>', views.finished),
    path('new/ai/', views.new_game_ai, name='new_game_ai'),
    path('game/ai/<int:game_id>/', views.play_game_ai, name='play_game_ai'),
    path('new/player/', views.new_game_player, name='new_game_player'),
    path('game/player/<int:game_id>/', views.play_game_player, name='play_game_player'),
]