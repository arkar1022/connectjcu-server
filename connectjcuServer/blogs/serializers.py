from rest_framework import serializers
from .models import Blog
from categories.models import Category
from api.serializers import UserPublicSerializer
from categories.serializers import CategoryPublicSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    category = CategoryPublicSerializer()
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content',
            'view_count',
            'image_file',
            'category',
            'author',
            'created_at',
            'updated_at',
        ]