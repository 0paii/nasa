from django.contrib import admin
from django.utils.safestring import mark_safe
from main.models import SortableCarousel
from adminsortable2.admin import SortableAdminMixin


@admin.register(SortableCarousel)
class ImagesSortableCarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail', 'my_order')
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        return mark_safe('<img src="%s" width="50" height="50" />' % obj.image.url)

    image_thumbnail.short_description = 'Изображение'
