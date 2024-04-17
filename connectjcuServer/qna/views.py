from rest_framework import generics,mixins
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from .models import Qna
from categories.models import Category
from .serializers import QnaSerializer
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404
from django.db.models import Q, Value

class QnaMixinListView(mixins.CreateModelMixin,mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        category_id = self.request.data.get('category')
        category = Category.objects.get(id=category_id)
        serializer.save(user=self.request.user, category=category)

    def get_serializer_context(self):
        """
        Pass the request object to the serializer context.
        """
        context = super(QnaMixinListView, self).get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.query_params.get('sort')
        search_term = self.request.query_params.get('search', None)
        category_id = self.request.query_params.get('category', None)
        user_id = self.request.query_params.get('user', None)

        if sort_by:
            if sort_by.startswith('-'):
                field_name = sort_by[1:]
                queryset = queryset.order_by(F(field_name).desc())
            else:
                queryset = queryset.order_by(sort_by)

        if search_term:
            # Annotate the queryset with a full_name field
            queryset = queryset.annotate(full_name=Concat('user__first_name', Value(' '), 'user__last_name'))
            # Filter the queryset for Qnas with titles containing the search term or users whose full name contains the search term
            queryset = queryset.filter(Q(title__icontains=search_term) | Q(full_name__icontains=search_term))
        
        if category_id:
            # Filter the queryset for Qnas that belong to the specified category
            queryset = queryset.filter(category__id=category_id)

        
        if user_id:
            queryset = queryset.filter(user__id=user_id)

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QnaMixinDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        return self.retrieve(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        category_id = self.request.data.get('category')
        if category_id:
            # Get the Category instance based on the provided ID
            category = get_object_or_404(Category, id=category_id)
            serializer.save(category=category)
        else:
            # If no category ID is provided, just save the serializer without updating the category
            serializer.save()
    
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_serializer_context(self):
        """
        Pass the request object to the serializer context.
        """
        context = super(QnaMixinDetailView, self).get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

