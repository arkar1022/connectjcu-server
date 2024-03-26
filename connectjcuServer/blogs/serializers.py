from rest_framework import serializers
from .models import Blog
from api.serializers import UserPublicSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content',
            'view_count',
            'image_file',
            'author',
            'created_at',
            'updated_at',
        ]