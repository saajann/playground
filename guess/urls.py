from django.urls import path
from . import views

urlpatterns = [
    path('', views.number),
    path('game/finished/<int:id>', views.finished),
    path('new/', views.new_game, name='new_game'),
    path('game/<int:game_id>/', views.play_game, name='play_game'),
]