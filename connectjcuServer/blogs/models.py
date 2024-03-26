from django.db import models
from django.conf import settings
from django.db.models import Q

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    image_file = models.ImageField(upload_to='images/', blank=True, default='default.jpg')
    view_count = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

