# Generated by Django 3.0.2 on 2020-01-07 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200107_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Author'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='dewey_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Dewey'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='genre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='publication',
            name='reference',
            field=models.CharField(editable=False, max_length=30),
        ),
    ]
