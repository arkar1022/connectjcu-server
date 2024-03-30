from django.contrib import admin
from .models import Resource
# Register your models here.\
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')

admin.site.register(Resource, ResourceAdmin)