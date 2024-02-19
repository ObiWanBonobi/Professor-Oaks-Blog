""" View for the database """

from django.views import generic
from .models import PokeDatabase


class PokemonList(generic.ListView):
    """ Stores a single blog post entry related to :model:`auth.User`. """
    queryset = PokeDatabase.objects.all()
    template_name = "database/database.html"
