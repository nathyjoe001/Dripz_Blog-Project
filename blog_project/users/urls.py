from django.urls import path
from .views import UserRegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', TokenObtainPairView.as_view(), name='token-obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]