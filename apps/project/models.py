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
        verbose_name_plural = ""
# class BigBanner(models.Model):

# class LongBanner(models.Model):

# class SquareBanner(models.Model):