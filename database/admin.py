""" Admin for the Pokemon database page """

from django.contrib import admin
from .models import PokeDatabase

admin.site.register(PokeDatabase)
