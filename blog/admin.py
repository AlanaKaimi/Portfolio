from django.contrib import admin
from .models import Post, Project, Art

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_date',
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_date',
    )
    exclude = ('slug',)

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_date',
    )
    exclude = ('slug',)
