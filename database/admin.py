""" Admin for the Pokemon database page, connects to the PokeDatabase model """

from django.contrib import admin
from .models import PokeDatabase

admin.site.register(PokeDatabase)
