# Generated by Django 3.0.2 on 2020-01-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20200110_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name="Url de l'image"),
        ),
        migrations.AlterField(
            model_name='publication',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name="Url de l'image"),
        ),
    ]
