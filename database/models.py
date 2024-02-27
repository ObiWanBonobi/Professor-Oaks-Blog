""" Models for the database page """

from django.db import models


class PokeDatabase(models.Model):
    """ Stores pokemon data from the pokedata.json file """
    poke_id = models.CharField()
    name = models.CharField()
    image = models.CharField()
    poke_type = models.CharField()
    height = models.CharField()
    weight = models.CharField()

    class Meta:
        """ This class orders our posts from the pokemon id """
        ordering = ["poke_id"]

    def __str__(self):
        """ This method gives our posts a nicer title in the admin page """
        return f"{self.name}"
