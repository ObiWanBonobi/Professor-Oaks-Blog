""" Urls for user profile, connects to the CommentList class in the views.py file """

from django.urls import path
from . import views


urlpatterns = [
    path("", views.social_profiles, name="social_profiles"),
    path("profile/<int:pk>", views.profile_user, name="profile"),
    path("update_profile/<int:pk>", views.ProfileUpdate.as_view(), name="update_profile"),
]
