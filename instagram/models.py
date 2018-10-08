from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    class that extends the user profile from django
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def update_caption(self, update):
        self.caption = update
        self.save()

    @classmethod
    def delete_image(cls, id):
        to_delete = cls.objects.filter_by(id=id)
        to_delete.delete()


class Comments(models.Model):
    """
    class that defines the post comments
    """
    user = models.ForeignKey(Profile)
    image = models.ForeignKey(Image)
    comment = models.CharField(max_length=250)
    pub_time = models.DateTimeField(auto_now_add=True)

