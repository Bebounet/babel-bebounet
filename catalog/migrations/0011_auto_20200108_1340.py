# Generated by Django 3.0.2 on 2020-01-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200108_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dewey',
            name='bg_color',
            field=models.CharField(blank=True, choices=[('#000000', 'black'), ('#8B4513', 'maroon'), ('#FF0000', 'red'), ('#FF4500', 'orange'), ('#FFFF00', 'yellow'), ('#32CD32', 'green'), ('#1E90FF', 'blue'), ('#8B008B', 'purple'), ('#A9A9A9', 'grey'), ('#FFFFFF', 'white')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dewey',
            name='text_color',
            field=models.CharField(blank=True, choices=[('#FFFFFF', 'white'), ('#000000', 'black')], max_length=7, null=True),
        ),
    ]
