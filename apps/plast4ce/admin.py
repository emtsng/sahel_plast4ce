from django.contrib import admin
from apps.plast4ce.models import GalleryImage, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'sort_order', 'updated_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'excerpt', 'body')
    ordering = ('sort_order', '-created_at')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'is_published', 'sort_order', 'updated_at')
    list_filter = ('is_published', 'category')
    search_fields = ('alt_text', 'category')
    ordering = ('sort_order', '-created_at')
