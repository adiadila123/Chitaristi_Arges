# Generated by Django 4.2.14 on 2024-07-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chitaristi', '0004_alter_slider_options_slider_link_slider_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.AlterModelOptions(
            name='imagegallery',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='imagegallery',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]