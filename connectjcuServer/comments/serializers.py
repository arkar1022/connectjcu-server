from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from api.serializers import UserPublicSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    content_type_name = serializers.SerializerMethodField()  # For reading
    content_type = serializers.PrimaryKeyRelatedField(  # For writing
        queryset=ContentType.objects.all(), 
        write_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'content_type', 'content_type_name', 'object_id', 'created_at', 'updated_at']
        extra_kwargs = {
            'content_type': {'write_only': True},  # Ensure it's write-only
        }

    def get_content_type_name(self, obj):
        return obj.content_type.model
    


