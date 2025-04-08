# users/signals.py
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserToken

@receiver(user_logged_in)
def generate_token_on_login(sender, request, user, **kwargs):
    # Generate and store a new token for the logged-in user
    UserToken.objects.create(user=user)
