# Generated by Django 4.2.3 on 2023-07-23 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='movie_type',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='imdb_votes',
        ),
    ]
