from django.urls import path
from .views import CategoryListCreateView, PostListCreateView, PostDetailView


urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]
