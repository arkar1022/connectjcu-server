from django.contrib import admin
from .models import Qna
# Register your models here.\
class QnaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')

admin.site.register(Qna, QnaAdmin)