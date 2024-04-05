from rest_framework import serializers
from .models import Qna
from categories.models import Category
from api.serializers import UserPublicSerializer
from categories.serializers import CategoryRelatedFieldSerializer

class QnaSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    category = CategoryRelatedFieldSerializer(queryset=Category.objects.all())
    is_owner = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Qna
        fields = [
            'id',
            'title',
            'content',
            'view_count',
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