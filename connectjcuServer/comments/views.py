from rest_framework import generics, mixins
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer

class CommentMixinListView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.query_params.get('sort')
        
        # Filter by content_type and object_id if they are provided as query parameters
        content_type_id = self.request.query_params.get('content_type')
        object_id = self.request.query_params.get('object_id')
        
        if content_type_id:
            queryset = queryset.filter(content_type_id=content_type_id)
        if object_id:
            queryset = queryset.filter(object_id=object_id)

        if sort_by:
            if sort_by.startswith('-'):
                field_name = sort_by[1:]
                queryset = queryset.order_by(F(field_name).desc())
            else:
                queryset = queryset.order_by(sort_by)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentMixinDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)