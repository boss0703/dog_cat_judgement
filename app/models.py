from django.db import models


class ImageFileModel(models.Model):
    """
    データ定義クラス
    画像モデルを定義する
    """
    image = models.ImageField(upload_to='images')
    published_date = models.DateTimeField(blank=True, null=True)
