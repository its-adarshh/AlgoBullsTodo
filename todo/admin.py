from django.contrib import admin
from .models import TodoItem, Tag

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    # Read-only for created_at
    readonly_fields = ('created_at',)

    # Fieldsets for better organization
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'created_at')
        }),
        ('Task Details', {
            'fields': ('due_date', 'tags', 'status')
        }),
    )

    # Filters for easier management
    list_filter = ('status', 'due_date', 'created_at')
    list_display = ('title', 'status', 'due_date', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)