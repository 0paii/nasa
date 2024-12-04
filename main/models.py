from django.db import models
from filer.fields.image import FilerImageField


class SortableCarousel(models.Model):
    title = models.CharField("Название", max_length=255)
    image = FilerImageField(verbose_name="Добавить изображение (Drag and Drop)", related_name='slider_images', on_delete=models.CASCADE)
    my_order = models.PositiveSmallIntegerField(verbose_name="Сортировка", default=0, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['my_order']
