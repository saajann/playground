from django.urls import path
from . import views

urlpatterns = [
    path('', views.hangman),
    path('game/finished/<int:id>', views.finished),
    path('new/', views.new_game, name='new_game_hangman'),
    path('play/<int:game_id>/', views.play_game, name='play_game_hangman'),
    path('words/', views.add_word, name='add_word'),
    path('edit/<int:id>/', views.edit_word, name='edit_word'),
    path('delete/<int:id>/', views.delete_word, name='delete_word'),
]
