""" URL configuration for profoak project """
from django.contrib import admin
from django.urls import path
from blog.views import poke_blog
from database.views import poke_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', poke_blog, name='blog'),
    path('database/', poke_data, name='blog'),
]
