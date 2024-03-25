""" User_profile app """
from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """
    Provides primary key type for the user_profile app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
