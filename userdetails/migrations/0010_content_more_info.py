# Generated by Django 4.1.1 on 2022-11-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0009_rename_home_native_language_home_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='more_info',
            field=models.TextField(null=True),
        ),
    ]