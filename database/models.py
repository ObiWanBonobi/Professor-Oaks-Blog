""" Models for the database page """

from django.db import models
import pokebase as pb


class PokeDatabase(models.Model):
    """ database """
    pokemon = pb.pokemon('charmander')
