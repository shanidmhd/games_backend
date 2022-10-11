# Generated by Django 4.1.1 on 2022-10-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0004_content_video_link_alter_content_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='html_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='short_video',
            field=models.FileField(max_length=255, null=True, upload_to='short_video/'),
        ),
        migrations.AddField(
            model_name='content',
            name='short_video_link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
