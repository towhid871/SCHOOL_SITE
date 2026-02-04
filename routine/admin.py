from django.contrib import admin
from .models import Routine

# Register your models here.

class RoutineAdmin(admin.ModelAdmin):
    list_display = ('department', 'semester', 'day', 'time_slot', 'subject', 'faculty', 'created_at')
    search_fields = ('department__name', 'semester', 'day', 'time_slot', 'subject', 'faculty__name')
    list_filter = ('department', 'semester', 'day', 'time_slot', 'faculty')
    ordering = ('department', 'semester', 'day', 'time_slot')



admin.site.register(Routine, RoutineAdmin)