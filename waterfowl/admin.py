from django.contrib import admin
from waterfowl.models import Articles
from waterfowl.models import Gallery


class GalleryInline(admin.TabularInline):
    model = Gallery
    fk_name = 'articles'


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline,
    ]
