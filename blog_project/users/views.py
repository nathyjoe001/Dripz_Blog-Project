from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response  # Import Response
from rest_framework import status  # Import status
from rest_framework.exceptions import ValidationError  # Import ValidationError
from django.db import IntegrityError  # Import IntegrityError

# Create your views here.

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                # Save the new user instance
                self.perform_create(serializer)
                return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                raise ValidationError({"detail": "Username already exists."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
