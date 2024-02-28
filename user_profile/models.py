""" Models for the blog page """

from django.db import models
from django.contrib.auth.models import User


class Socials(models.Model):
    """
    Model for creating a comment on a post. Connects to :model:`auth.User`
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )

    def __str__(self):
        """ This method gives our posts a nicer title in the admin page """
        return f"User : {self.user}"
