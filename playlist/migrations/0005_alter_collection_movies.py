# Generated by Django 4.1.7 on 2023-10-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_alter_collection_movies_remove_collection_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='movies',
            field=models.ManyToManyField(related_name='collection', to='playlist.movie'),
        ),
    ]
