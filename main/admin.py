from django.contrib import admin
from django.utils.safestring import mark_safe
from main.models import SortableCarousel
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer
from djangoProject.settings import THUMBNAIL_ALIASES


@admin.register(SortableCarousel)
class ImagesSortableCarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail', 'my_order')
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        thumbnail_options = THUMBNAIL_ALIASES['']['admin_preview']
        thumbnail_url = get_thumbnailer(obj.image).get_thumbnail(thumbnail_options).url
        return mark_safe('<img src="%s" width="50" height="50" />' % thumbnail_url)

    image_thumbnail.short_description = 'Изображение'
