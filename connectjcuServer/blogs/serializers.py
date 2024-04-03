from rest_framework import serializers
from .models import Blog
from resources.models import Resource
from categories.models import Category
from api.serializers import UserPublicSerializer
from categories.serializers import CategoryRelatedFieldSerializer
# from django.contrib.contenttypes.models import ContentType
# content_type = ContentType.objects.get_for_model(Resource)
# print(content_type.id)

class BlogSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    category = CategoryRelatedFieldSerializer(queryset=Category.objects.all())
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