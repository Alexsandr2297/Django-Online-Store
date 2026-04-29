from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("heading", "content", "created_at", "publication_attribute", "quantity_views")
    list_filter = ("publication_attribute", "created_at")
    search_fields = ("heading", "content")
