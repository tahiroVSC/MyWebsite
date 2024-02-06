from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(
        upload_to="images",
        verbose_name= "Фотография"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "ФИО"
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    experience = models.IntegerField(
        verbose_name = "Опыт Работы"
    )
    project = models.IntegerField(
        verbose_name = "Кол-во Проектов"
    )
    happyclient = models.IntegerField(
        verbose_name = "Кол-во довольнных клиентов"
    )
    unhappyclient = models.IntegerField(
        verbose_name = "Кол-во Недовольныхх клиентов"
    )
    def __str__(self):
            return self.name
    
    class Meta:
          verbose_name = "Базовые настройки"    
          verbose_name_plural = "Базавая настройка"