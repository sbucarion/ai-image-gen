# Generated by Django 5.0.2 on 2024-02-17 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0002_rename_cfgscale_imageconfigs_cfg_scale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageconfigs',
            old_name='sample',
            new_name='sampler',
        ),
    ]