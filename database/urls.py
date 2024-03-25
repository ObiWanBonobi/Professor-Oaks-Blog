""" Urls for database app """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.PokemonList.as_view(), name='pokemon_database'),
]
