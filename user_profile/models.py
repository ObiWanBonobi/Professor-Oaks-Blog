""" Models for the blog page """

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Model for creating a comment on a post. Connects to :model:`auth.User`
    """
