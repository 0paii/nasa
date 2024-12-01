# Generated by Django 4.1 on 2024-12-01 10:46

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('main', '0006_alter_sortablecarousel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortablecarousel',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to=settings.FILER_IMAGE_MODEL),
        ),
    ]