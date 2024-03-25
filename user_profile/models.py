""" Models for the user_profile app """

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from database.models import PokeDatabase


class Socials(models.Model):
    """
    Stores a single user profile.

    Connects to :model:`auth.User` and :model:`database.PokeDatabase`, then
    connects to itself through the ManyToManyField in follows.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )
    user_image = CloudinaryField("image", default="placeholder")
    fav_pokemon = models.ForeignKey(
        PokeDatabase, on_delete=models.CASCADE, related_name="fav_pokemon", default='152'
    )

    def __str__(self):
        """This method gives our posts a nicer title in the admin page"""
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Stores a users profile.

    Connects to :model:`user_profile.Socials`.
    """
    if created:
        user_profile = Socials(user=instance)
        user_profile.save()
