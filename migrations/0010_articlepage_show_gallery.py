# Generated by Django 5.0.9 on 2024-09-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0009_remove_articlepage_body_alter_articlepage_body_sf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='show_gallery',
            field=models.BooleanField(default=True, help_text='Show the gallery', verbose_name='show doc link'),
        ),
    ]
