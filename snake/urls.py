from django.urls import path
from . import views

urlpatterns = [
    path('', views.game, name='game'),
    path('move/', views.move_snake, name='move_snake'),
]