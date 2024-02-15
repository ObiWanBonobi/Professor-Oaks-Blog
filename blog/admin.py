""" Admin for the blog page. Connects the Post model to the admin dashboard """

from django.contrib import admin
from .models import Post


admin.site.register(Post)
