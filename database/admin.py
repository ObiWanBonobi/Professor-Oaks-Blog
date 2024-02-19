""" Admin for the Pokemon database page """

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PokeDatabase


@admin.register(PokeDatabase)
class DatabaseAdmin(SummernoteModelAdmin):
    """ Gives the admin panel greater functionality and clarity """
    summernote_fields = ('content',)
