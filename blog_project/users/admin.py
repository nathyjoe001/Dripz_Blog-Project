
# users/admin.py
from django.contrib import admin
from .models import CustomUser

#admin.site.register(CustomUser)

# users/admin.py
from django.contrib import admin
from .models import UserToken, CustomUser

@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_photo')

