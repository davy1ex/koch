from django.db import models


class Playground(models.Model):
    playground_type = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    rating = models.IntegerField()
    description = models.CharField(max_length=512)
    latitude = models.FloatField(unique=True)
    longitude = models.FloatField(unique=True)
    photo = models.ImageField(verbose_name='Photo', upload_to="playground", null=True, blank=True)
