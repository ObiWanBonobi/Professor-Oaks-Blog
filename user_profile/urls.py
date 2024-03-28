""" Urls for user profile app """

from django.urls import path
from . import views


urlpatterns = [
    path("", views.social_profiles, name="social_profiles"),
    path("profile/<int:pk>", views.profile_user, name="profile"),
    path(
        "update_profile/<int:pk>",
        views.ProfileUpdate.as_view(),
        name="update_profile"),
    path(
        "profile/user_delete/<int:user_id>",
        views.delete_user,
        name="delete_user"),
]
