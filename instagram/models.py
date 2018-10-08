from django.db import models


class Profile(models.Model):
    """
    class that extends the user profile from django
    """
    profile_pic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=250)


class Image(models.Model):
    """
    class that defines the images to be uploaded on the site
    """
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(Profile)


class Comments(models.Model):
    """
    class that defines the post comments
    """
    user = models.ForeignKey(Profile)
    image = models.ForeignKey(Image)
    comment = models.CharField(max_length=250)
    pub_time = models.DateTimeField(auto_now_add=True)

