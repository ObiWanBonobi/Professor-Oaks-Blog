"""
View for the socials page. It shows all the users in a list. When one is clicked,
the user can see that users page.
"""

from django.shortcuts import render
from .models import Socials


def social_profiles(request):
    """
    Shows social page with all the users, exept the user thats logged in.
    Connects to the :model:`user_profile.Socials`
    Displays on :template:`user_profile/socials.html`
    """
    profiles = Socials.objects.exclude(user=request.user)
    return render(request, "user_profile/socials.html", {"profiles": profiles})


def profile_user(request, pk):
    """
    Connects to the :model:`user_profile.Socials`
    Displays on :template:`user_profile/profile.html`
    """
    profile = Socials.objects.get(pk=pk)
    return render(request, "user_profile/profile.html", {"profile": profile})
