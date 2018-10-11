from django import forms
from .models import Profile, Image, Comments


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


class CommentForm(forms.ModelForm):
    """
    Enables users to comment on images
    """
    class Meta:
        model = Comments
        exclude = ['user', 'pub_time', 'image']
