""" Blog app """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Provides primary key type for the blog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
