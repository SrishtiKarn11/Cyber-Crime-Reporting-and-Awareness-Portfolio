from django.contrib import admin
from .models import Complaint, AwarenessPost

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'crime_type', 'status', 'created_at')
    list_filter = ('status', 'crime_type')
    search_fields = ('user__username', 'crime_type')

@admin.register(AwarenessPost)
class AwarenessAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
