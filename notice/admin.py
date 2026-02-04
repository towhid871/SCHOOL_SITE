from django.contrib import admin
from .models import Notice


# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at',)




admin.site.register(Notice, NoticeAdmin)
