from django.contrib import admin
from .models import Post, Project, Art

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_date',
        'tag_list'
    )
    exclude = ('slug',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_date',
        'tag_list'
    )
    exclude = ('slug',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_date',
        'tag_list'
    )
    exclude = ('slug',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
