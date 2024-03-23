from rest_framework import generics,mixins

from .models import Blog
from .serializers import BlogSerializer

class BlogMixinListView(mixins.CreateModelMixin,mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogMixinDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

