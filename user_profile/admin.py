""" Admin for the blog page. Connects the Post model to the admin dashboard """

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ProfileComment


@admin.register(ProfileComment)
class ProfileAdmin(SummernoteModelAdmin):
    """ Gives the admin panel greater functionality and clarity """
    summernote_fields = ('content',)
