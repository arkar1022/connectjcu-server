from rest_framework import serializers

class UserPublicSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    get_full_name = serializers.CharField(read_only=True)
    full_name = serializers.SerializerMethodField()
    profile_image = serializers.CharField(read_only=True)

    def get_full_name(self, obj):
        return obj.get_full_name