# Generated by Django 4.1 on 2024-11-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_imagescarousel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagescarousel',
            name='image',
            field=models.ImageField(upload_to='carousel'),
        ),
    ]
