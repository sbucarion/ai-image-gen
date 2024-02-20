# Generated by Django 5.0.2 on 2024-02-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageconfigs',
            old_name='cfgScale',
            new_name='cfg_scale',
        ),
        migrations.RenameField(
            model_name='imageconfigs',
            old_name='denoisingStrength',
            new_name='denoising_strength',
        ),
        migrations.RenameField(
            model_name='imageconfigs',
            old_name='hrScale',
            new_name='hr_scale',
        ),
        migrations.RenameField(
            model_name='imageconfigs',
            old_name='hrUpscaler',
            new_name='hr_upscaler',
        ),
        migrations.RenameField(
            model_name='imageconfigs',
            old_name='samplerSetps',
            new_name='sample',
        ),
        migrations.AddField(
            model_name='imageconfigs',
            name='sampler_steps',
            field=models.CharField(default='test', max_length=500),
            preserve_default=False,
        ),
    ]
