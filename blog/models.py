""" Models for the blog page """

from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """ Stores a single blog post entry related to :model:`auth.User`. """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ This class orders our posts from newest to oldest """
        ordering = ["-created_on"]

    def __str__(self):
        """ This method gives our posts a nicer title in the admin page """
        return f"Title: {self.title} | by: {self.author}"


class Comment(models.Model):
    """ Model for creating a comment on a post """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ This class orders our comments from oldest to newest """
        ordering = ["created_on"]

    def __str__(self):
        """ This method gives our comments a nicer title in the admin page """
        return f"Comment: {self.body} | by: {self.author}"
