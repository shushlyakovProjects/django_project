from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('game-pc', views.gamepc, name='game-pc'),
    path('about', views.about, name='about'),
    path('game-pc/<int:id>', views.gamepcitem, name='game-pc-item')
]
