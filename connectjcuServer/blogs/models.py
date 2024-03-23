from django.db import models
from django.conf import settings
from django.db.models import Q

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    image_file = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    
