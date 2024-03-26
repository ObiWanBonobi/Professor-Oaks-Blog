""" Test for the blog.form.py file """

from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test for all fields for :form:`blog.CommentForm`
    """
    def test_form_is_valid(self):
        """ Tests if the comment form works with a message in the body """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """ Tests if the comment form works without a message in the body """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
