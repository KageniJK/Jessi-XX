from django import forms
from .models import Profile, Image


class UpdateProfile(forms.ModelForm):
    """
    Enables the user to update their bio and profile picture
    """
    class Meta:
        model = Profile
        exclude = ['user']


class PostImageForm(forms.ModelForm):
    """
    Enables the user to upload images
    """
    class Meta:
        model = Image
        exclude = ['user', 'post_date', 'likes']