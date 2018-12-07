from django.contrib import admin
from django.urls import path
from games import views


urlpatterns = [
    path('', views.game_list),
    #path('games/', views.game_list),
]