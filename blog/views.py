""" View for the blog """

from django.shortcuts import render
from django.http import HttpResponse


def poke_blog(request):
    """ Blog """
    return HttpResponse("Hello, Blog!")
