# Generated by Django 4.1.1 on 2022-09-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0002_alter_content_audio_alter_content_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='text_content',
            field=models.TextField(null=True),
        ),
    ]
