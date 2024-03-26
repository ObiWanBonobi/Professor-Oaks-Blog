""" Models for the database app """

from django.db import models


class PokeDatabase(models.Model):
    """
    Stores pokemon data from the pokedata.json file
    """
    poke_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    poke_type = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)

    class Meta:
        """ This class orders our posts from the pokemon id """
        ordering = ["poke_id"]

    def __str__(self):
        """ This method gives our posts a nicer title in the admin page """
        return f"{self.name}"
