from django import forms


class UpdateProfile(forms.Form):
    """
    Enables the user to update their bio and profile picture
    """
    bio = forms.CharField(label='bio', max_length=250)
    profile_pic = forms.FileField
