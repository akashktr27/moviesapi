# Generated by Django 4.1.7 on 2023-10-05 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0005_alter_collection_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='owner',
        ),
        migrations.AddField(
            model_name='movie',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='playlist.collection'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='uuid',
            field=models.CharField(max_length=36),
        ),
    ]
