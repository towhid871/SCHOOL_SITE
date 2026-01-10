from django.contrib import admin
from .models import Member 

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_type', 'department', 'email', 'phone')
    search_fields = ('name', 'email', 'phone', 'student_id')
    list_filter = ('member_type', 'department')
    ordering = ('name',)





admin.site.register(Member, MemberAdmin)
