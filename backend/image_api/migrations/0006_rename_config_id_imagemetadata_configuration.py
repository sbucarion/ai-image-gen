# Generated by Django 4.1.4 on 2024-02-18 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0005_imagemetadata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemetadata',
            old_name='config_id',
            new_name='configuration',
        ),
    ]