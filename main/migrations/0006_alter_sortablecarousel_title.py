# Generated by Django 4.2.16 on 2024-11-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_sortablecarousel_delete_imagescarousel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortablecarousel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]