# Generated by Django 3.0.2 on 2020-01-10 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20200109_0833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name'], 'verbose_name': 'Auteur'},
        ),
        migrations.AlterModelOptions(
            name='dewey',
            options={'ordering': ['number'], 'verbose_name': 'Classement dewey'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['reference'], 'verbose_name': 'Publication'},
        ),
        migrations.AlterField(
            model_name='author',
            name='century_birth',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='Siècle de naissance'),
        ),
        migrations.AlterField(
            model_name='author',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_died',
            field=models.DateField(blank=True, null=True, verbose_name='Date de décès'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name="Fichier de l'image"),
        ),
        migrations.AlterField(
            model_name='author',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name="Url de l'image"),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(editable=False, max_length=61, verbose_name='Nom complet'),
        ),
        migrations.AlterField(
            model_name='author',
            name='place_birth',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Lieu de naissance'),
        ),
        migrations.AlterField(
            model_name='author',
            name='place_died',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Lieu de décès'),
        ),
        migrations.AlterField(
            model_name='dewey',
            name='bg_color',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dewey',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='dewey',
            name='number',
            field=models.CharField(max_length=12, verbose_name='Numéro'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Author', verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_publication',
            field=models.DateField(blank=True, null=True, verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='dewey_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Dewey', verbose_name='Numéro dewey'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='genre',
            field=models.CharField(max_length=30, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name="Fichier de l'image"),
        ),
        migrations.AlterField(
            model_name='publication',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name="Url de l'image"),
        ),
        migrations.AlterField(
            model_name='publication',
            name='isbn',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='label_editor',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Label/Editeur'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='nb_tracks_pages',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nombre de Titres/Pages'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='reference',
            field=models.CharField(editable=False, max_length=30, verbose_name='Référence'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='type_publication',
            field=models.CharField(choices=[('B', 'Books'), ('M', 'Music'), ('F', 'Films'), ('_', 'Autre')], default='B', max_length=1, verbose_name='Type de publication'),
        ),
    ]
