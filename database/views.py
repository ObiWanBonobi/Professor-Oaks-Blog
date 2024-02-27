""" View for the database, connects to the  """

from django.views import generic
from .models import PokeDatabase


class PokemonList(generic.ListView):
    """ Shows pokemon data from the :model:`database.PokeDatabase` """
    queryset = PokeDatabase.objects.all()
    template_name = "database/database.html"
