from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from typing import Union


class User(AbstractUser):
    profile_pic = models.ImageField(('profile_picture'), upload_to='profile_picture', blank=True)
    bio = models.CharField(blank=True, null=True, max_length=250)

    def __str__(self):
        return self.username

    def get_posts(self):
        return Post.objects.filter(user=self).values_list('id', flat=True)


RequestUser = Union[AnonymousUser, User]





class Post(models.Model):
    caption = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(('post_picture'), upload_to='post_picture', blank=True)
    image_filter = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.caption

    def get_image_url(self, obj):
        return obj.image.url