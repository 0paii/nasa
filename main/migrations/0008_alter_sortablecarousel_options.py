# Generated by Django 4.1 on 2024-12-01 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_sortablecarousel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sortablecarousel',
            options={'ordering': ['my_order']},
        ),
    ]
