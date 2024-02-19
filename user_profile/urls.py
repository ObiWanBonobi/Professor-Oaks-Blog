""" Urls for user profile, connects to the CommentList class in the views.py file """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.CommentList.as_view(), name='user_profile'),
]
