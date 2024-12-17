from django.contrib import admin
from .models import AnnotationTask

# Register the AnnotationTask model with the admin panel
@admin.register(AnnotationTask)
class AnnotationTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')  # Fields to display in the list view
    search_fields = ('name',)  # Allow search by name
    list_filter = ('created_at',)  # Filter by creation date
