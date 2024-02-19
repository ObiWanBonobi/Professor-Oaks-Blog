""" Models for the blog page """

from django.db import models
from django.contrib.auth.models import User


class ProfileComment(models.Model):
    """ Model for creating a comment on a post """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profilecommenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ This class orders our comments from oldest to newest """
        ordering = ["created_on"]

    def __str__(self):
        """ This method gives our comments a nicer title in the admin page """
        return f"Comment: {self.body} | by: {self.author}"
