from django.db import models

# Create your models here.
class SmallBanner(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Зоголовок"
    )
    image = models.ImageField(
        upload_to= "images",
        verbose_name= "Фотография"
    )
    desription = models.TextField(
        verbose_name = "Описание"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Маленкий баннер"
        verbose_name_plural = "Маленкий баннер"

class BigBanner(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Зоголовок"
    )
    image = models.ImageField(
        upload_to= "images",
        verbose_name= "Фотография"
    )
    desription = models.TextField(
        verbose_name = "Описание"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Большой  баннер"
        verbose_name_plural = " Большой баннер"

class LongBanner(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Зоголовок"
    )
    image = models.ImageField(
        upload_to= "images",
        verbose_name= "Фотография"
    )
    desription = models.TextField(
        verbose_name = "Описание"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Длинный баннер"
        verbose_name_plural = "Длинный баннер"

class SquareBanner(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Зоголовок"
    )
    image = models.ImageField(
        upload_to= "images",
        verbose_name= "Фотография"
    )
    desription = models.TextField(
        verbose_name = "Описание"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "квадратный баннер"
        verbose_name_plural = "квадратный баннер"