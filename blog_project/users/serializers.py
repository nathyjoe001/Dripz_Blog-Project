from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    profile_photo = serializers.ImageField(required=False)  # Optional field

    class Meta:
        model = CustomUser  # Make sure you're using the CustomUser model
        fields = ['id', 'username', 'email', 'profile_photo']

    def create(self, validated_data):
        # Use CustomUser instead of User
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    
