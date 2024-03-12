""" View for the User profile """

from django.shortcuts import render
from .models import Socials


def social_profiles(request):
    """
    Shows social page with all the users, exept the user thats logged in.
    Displays on :template:`user_profile/socials.html`
    """
    profiles = Socials.objects.exclude(user=request.user)
    return render(request, "user_profile/socials.html", {"profiles": profiles})
