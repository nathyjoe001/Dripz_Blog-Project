from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    def __str__(self):
        return self.username