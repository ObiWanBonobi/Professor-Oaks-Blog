""" View for the User profile """

from django.views import generic
from .models import ProfileComment


class ProfileCommentList(generic.ListView):
    """ class based view, shows only the published posts """
    queryset = ProfileComment.objects.all()
    template_name = "user_profile/profile.html"
