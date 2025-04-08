from django.urls import path
from .views import CategoryListCreateView, PostListCreateView, PostDetailView,PostDeleteView


urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]


