from rest_framework import serializers
from .models import Blog
from categories.models import Category
from api.serializers import UserPublicSerializer
from categories.serializers import CategoryRelatedFieldSerializer
from qna.models import Qna
from django.contrib.contenttypes.models import ContentType
content_type = ContentType.objects.get_for_model(Qna)
print(content_type.id)

class BlogSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    category = CategoryRelatedFieldSerializer(queryset=Category.objects.all())
    is_owner = serializers.SerializerMethodField(read_only=True)
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
            'is_owner',
            'created_at',
            'updated_at',
        ]
    def get_is_owner(self, obj):
        # Check if request is present in the serializer context
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            # Check if the current user is the owner of the blog post
            return obj.user == request.user
        return False