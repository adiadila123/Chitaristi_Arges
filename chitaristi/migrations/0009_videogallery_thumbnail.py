# Generated by Django 4.2.14 on 2024-07-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chitaristi', '0008_videogallery_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogallery',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='videos/thumbnails/'),
        ),
    ]
