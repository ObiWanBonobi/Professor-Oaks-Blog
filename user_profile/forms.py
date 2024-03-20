""" Comment form for post details """

from django import forms
from .models import Socials


class UpdateProfile(forms.ModelForm):
    """ Form """
    class Meta:
        """ Form """
        model = Socials
        fields = ('user_image', 'fav_pokemon',)
        labels = {"user_image": "Update profile picture",
              "fav_pokemon": "Update favourite Pokémon",}
