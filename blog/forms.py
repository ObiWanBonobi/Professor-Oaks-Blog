""" Comment form for the blog app """

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ Form class for users to comment on a post """
    class Meta:
        """
        Form for commenting on the Post_details.html page. No label shown.

        Connects to the :model:`blog.Comment`
        Displays on :template:`blog/post_detail.html`
        """
        model = Comment
        fields = ('body',)
        labels = {'body': '', }
