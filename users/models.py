from django.db import models
from django.conf import settings  # settings.AUTH_USER_MODEL을 사용하기 위해 import
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.user.username