from django.db import models


class ImageFileModel(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
