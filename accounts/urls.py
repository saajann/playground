from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registration/', views.user_registration),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
]