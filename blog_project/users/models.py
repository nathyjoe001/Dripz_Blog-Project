from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    def __str__(self):
        return self.username
    
# users/models.py
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserToken(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Create a refresh token when a new token is generated
        if not self.token:
            refresh = RefreshToken.for_user(self.user)
            self.token = str(refresh.access_token)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Token for {self.user.username}'
