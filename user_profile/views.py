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
    if request.user.is_authenticated:
        profiles = Socials.objects.exclude(user=request.user)
    else:
        profiles = Socials.objects.all()
    return render(request, "user_profile/socials.html", {"profiles": profiles})


def profile_user(request, pk):
    """
    Shows the user page with follow and unfollow buttons.
    Connects to the :model:`user_profile.Socials`
    Displays on :template:`user_profile/profile.html`
    """
    profile = Socials.objects.get(pk=pk)

    if request.method == "POST":
        current_user_profile = request.user.socials
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "user_profile/profile.html", {"profile": profile})
