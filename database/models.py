""" Models for the database page """

from django.db import models
from django.contrib.auth.models import User


class PokeDatabase(models.Model):
    """ Stores a single blog post entry related to :model:`auth.User`. """

