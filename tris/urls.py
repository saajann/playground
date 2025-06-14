from django.urls import path
from . import views

urlpatterns = [
    path('', views.tris),
    path('game/', views.game),
    path('game/finished/<int:id>', views.finished),
]