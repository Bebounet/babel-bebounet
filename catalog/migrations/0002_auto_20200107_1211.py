# Generated by Django 3.0.2 on 2020-01-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='date_died',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='image_file',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='author',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='place_died',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]