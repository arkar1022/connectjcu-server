from rest_framework import generics,mixins
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from categories.models import Category
from .serializers import BlogSerializer

class BlogMixinListView(mixins.CreateModelMixin,mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        category_id = self.request.data.get('category')
        category = Category.objects.get(id=category_id)
        serializer.save(user=self.request.user, category=category)

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.query_params.get('sort')

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


class BlogMixinDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

