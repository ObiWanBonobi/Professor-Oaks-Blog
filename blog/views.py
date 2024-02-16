""" View for the blog """

from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """ class based view """
    queryset = Post.objects.all()
    template_name = "post_list.html"
