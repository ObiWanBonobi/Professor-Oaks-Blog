""" View for the User profile """

from django.views import generic
from .models import UserProfile


class ProfileUserList(generic.ListView):
    """ class based view, shows only the published posts """
    queryset = UserProfile.objects.all()
    template_name = "user_profile/profile.html"
