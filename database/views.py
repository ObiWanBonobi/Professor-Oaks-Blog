""" View for the database """

from django.views import generic
from .models import PokeDatabase


class PokemonList(generic.ListView):
    """
    Shows all the pokemon data.

    Connects to the :model:`database.PokeDatabase`
    Displays on :template:`database/database.html`
    """
    queryset = PokeDatabase.objects.all()
    template_name = "database/database.html"
