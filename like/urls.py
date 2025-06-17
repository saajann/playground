from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.like_user),
    path('remove/<int:id>/', views.remove_like_user),
]
