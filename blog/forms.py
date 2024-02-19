""" Comment form for post details """

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Form """
    class Meta:
        """ Form """
        model = Comment
        fields = ('body',)
