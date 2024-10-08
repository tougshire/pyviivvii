# Generated by Django 5.0.9 on 2024-09-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibekwa', '0027_alter_sitetemplatesettings_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='embed_frame_style',
            field=models.CharField(blank=True, default='width:90%; height:1600px;', help_text='For pages with an iFrame, styling for the frame', max_length=255, verbose_name='Frame Style'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='embed_url',
            field=models.URLField(blank=True, help_text='For pages with an iFrame, the URL of the embedded contnet', verbose_name='Embed Target URL'),
        ),
    ]
