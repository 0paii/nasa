from django.db import models
from filer.fields.image import FilerImageField


class SortableCarousel(models.Model):
    title = models.CharField("Title", max_length=255, )
    image = FilerImageField(related_name='slider_images', on_delete=models.CASCADE)
    my_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['my_order']
