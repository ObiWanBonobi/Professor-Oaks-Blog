""" View for the database """
from django.shortcuts import render
from django.http import HttpResponse


def poke_data(request):
    """ Database """
    return HttpResponse("Hello, database!")
