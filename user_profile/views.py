""" Views for the socials app """

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from blog.models import Comment
from .models import Socials


def social_profiles(request):
    """
    Shows social page with all the users, exept the user thats logged in. And
    all the comments from the users that the user is following (if the user is
    following someone). If the user isn't logged in it'll show all users and
    no comment section.

    Connects to the :model:`user_profile.Socials` and :model:`blog.Comment`
    Displays on :template:`user_profile/socials.html`
    """
    if request.user.is_authenticated:
        profiles = Socials.objects.exclude(user=request.user)
        followed_users = request.user.socials.follows.all()
        followed_usernames = followed_users.values_list(
            "user__username", flat=True
            )
        comments = Comment.objects.filter(
            author__username__in=followed_usernames
            )

        return render(
            request,
            "user_profile/socials.html",
            {
                "profiles": profiles,
                "comments": comments,
                "followed_users": followed_users,
            },
        )
    else:
        profiles = Socials.objects.all()
        return render(
            request,
            "user_profile/socials.html",
            {"profiles": profiles},
        )


def profile_user(request, pk):
    """
    Shows the profile page of a user where the logged in user can follow or
    unfollow this users profile, if the user isn't logged in it won't show
    these follow and unfollow buttons.

    Connects to the :model:`user_profile.Socials`
    Displays on :template:`user_profile/profile.html`
    """
    profile = Socials.objects.get(user=pk)

    if request.method == "POST":
        current_user_profile = request.user.socials
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
            messages.add_message(
                request, messages.SUCCESS, "You're now following this user!"
            )
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
            messages.add_message(
                request, messages.SUCCESS, "You stopped following this user!"
            )
        current_user_profile.save()

    return render(request, "user_profile/profile.html", {"profile": profile})


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Updates the user profile image and favourite pokemon for a logged in user.

    Connects to the :model:`user_profile.Socials`
    Displays on :template:`user_profile/update_profile.html`
    """

    model = Socials
    fields = [
        "user_image",
        "fav_pokemon",
    ]
    template_name = "user_profile/update_profile.html"

    def get_success_url(self):
        pk = self.get_object().user.pk
        messages.success(self.request, "Profile updated!")
        return reverse_lazy("profile", kwargs={"pk": pk})

    def test_func(self):
        return self.request.user == self.get_object().user


def delete_user(request, user_id):
    """
    Deletes profile of logged in user

    Connects to the :model:`auth.User`
    Returns to :template:`user_profile/socials.html` after deletion
    """
    user_profile = get_object_or_404(User, pk=user_id)

    if user_profile == request.user:
        user_profile.delete()
        messages.add_message(request, messages.SUCCESS, "Profile deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own profile!"
        )

    return HttpResponseRedirect(reverse("social_profiles"))
