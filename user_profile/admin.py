""" Admin for the user_profile app, connects to the Socials model """

from django.contrib import admin
from .models import Socials


admin.site.register(Socials)
