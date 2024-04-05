from django.db import models
from django.conf import settings
from django.db.models import Q
from categories.models import Category


class Qna(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    view_count = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

