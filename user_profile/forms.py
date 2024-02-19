""" Comment form for post details """

from django import forms
from .models import ProfileComment


class ProfileCommentForm(forms.ModelForm):
    """ Form """
    class Meta:
        """ Form """
        model = ProfileComment
        fields = ('body',)
