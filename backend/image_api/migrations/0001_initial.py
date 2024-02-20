# Generated by Django 5.0.2 on 2024-02-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imageConfigs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('seed', models.CharField(max_length=500)),
                ('samplerSetps', models.CharField(max_length=500)),
                ('denoisingStrength', models.CharField(max_length=500)),
                ('cfgScale', models.CharField(max_length=500)),
                ('hrScale', models.CharField(max_length=500)),
                ('hrUpscaler', models.CharField(max_length=500)),
            ],
        ),
    ]
