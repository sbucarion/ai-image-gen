from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class imageConfigs(models.Model):
    model = models.CharField(max_length=200)
    sampler = models.CharField(max_length=500)
    sampler_steps = models.CharField(max_length=500)
    denoising_strength = models.CharField(max_length=500)
    cfg_scale = models.CharField(max_length=500)
    hr_scale = models.CharField(max_length=500)
    hr_upscaler = models.CharField(max_length=500)


class imageMetaData(models.Model):
    prompt = models.CharField(max_length=200)
    negative_prompt = models.CharField(max_length=500)
    seed = models.CharField(max_length=500)
    configuration = models.ForeignKey(imageConfigs, on_delete=models.CASCADE)
    unix_id = models.CharField(max_length=500)
