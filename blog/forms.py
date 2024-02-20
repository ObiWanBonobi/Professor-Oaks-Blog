""" Comment form for post details """

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Django's built-in class """
    class Meta:
        """ Form for commenting on the Post_details.html page """
        model = Comment
        fields = ('body',)
