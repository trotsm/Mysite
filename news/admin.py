from django.contrib import admin
from news.models import Articles
from news.models import Gallery


class GalleryInline(admin.TabularInline):
    model = Gallery
    fk_name = 'articles'


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    inline = [GalleryInline, ]
