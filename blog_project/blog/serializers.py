from rest_framework import serializers
from .models import Category, Post, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =['id', 'title', 'content', 'author', 'category', 'tag', 'created_at', 'updated_at', 'is_published']