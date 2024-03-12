""" Urls for user profile, connects to the CommentList class in the views.py file """

from django.urls import path
from . import views


urlpatterns = [
    path("socials/", views.social_profiles, name="social_profiles"),
    path("profile/<int:pk>", views.profile_user, name="profile"),
]
