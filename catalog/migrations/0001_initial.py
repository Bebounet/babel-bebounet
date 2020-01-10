# Generated by Django 3.0.1 on 2020-01-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=61)),
                ('century_birth', models.IntegerField()),
                ('date_birth', models.DateField()),
                ('place_birth', models.CharField(max_length=50)),
            ],
        ),
    ]
