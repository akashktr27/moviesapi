# Generated by Django 4.1.7 on 2023-10-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0010_alter_movie_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
    ]
