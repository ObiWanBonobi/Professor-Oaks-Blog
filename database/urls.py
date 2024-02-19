""" Urls for database, connects to the PokemonList class in the views.py file """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.PokemonList.as_view(), name='pokemon_database'),
]
