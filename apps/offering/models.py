from django.db import models

# Create your models here.
class Offernig(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    title2 = models.CharField(
        max_length = 255,
        verbose_name = "Название2"
    )
    image = models.ImageField(
        max_length= 255,
        verbose_name= "Фотография"
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Предложение"