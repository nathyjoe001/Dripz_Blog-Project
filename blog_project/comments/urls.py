from django.urls import path
from .views import CommentCrateView, CommentUpdateView

urlpatterns = [
    path('posts/<int:post_id>/comments/',CommentCrateView.as_view(), name='create-comment' ),
    path('comments/<int:pk>',CommentUpdateView.as_view(), name='comment-update-delete' )
]