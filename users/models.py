from django.db import models
from django.conf import settings  # settings.AUTH_USER_MODEL을 사용하기 위해 import
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nickname = models.CharField(max_length=40, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    followers = models.ManyToManyField('self', through='Follow', related_name='following', symmetrical=False)

    def __str__(self):
        return self.user.username
    

class Follow(models.Model):
    follower = models.ForeignKey(Profile, related_name='following_set', on_delete=models.CASCADE)
    followed = models.ForeignKey(Profile, related_name='follower_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.follower} follows {self.followed}'

    class Meta:
        unique_together = ('follower', 'followed')