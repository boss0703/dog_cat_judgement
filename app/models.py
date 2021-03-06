from django.db import models


class ImageFileModel(models.Model):
    # image = models.ImageField(upload_to='images', blank=True, null=True)
    image = models.ImageField(upload_to='images')
    published_date = models.DateTimeField(blank=True, null=True)
