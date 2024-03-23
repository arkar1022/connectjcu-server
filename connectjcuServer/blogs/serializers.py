from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    # image_file = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content',
            'image_file',
            'created_at',
            'updated_at',
        ]
    # def get_image_file(self, obj):
    #     # Get the filename from the full URL
    #     return obj.image_file.name.split('/')[-1] if obj.image_file else None
    # def get_image_file(self, obj):
    #     if obj.image_file:
    #         # Replace "localhost" with "connectjcu.org" in the URL
    #         return obj.image_file.url.replace('localhost', 'connectjcu.org')
    #     return None