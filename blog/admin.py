""" Admin for the blog page """

from django.contrib import admin
from .models import Post


admin.site.register(Post)
