from django.db import models

# Create your models here.
class Index(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Направление"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "ФИО"
    )
    image = models.ImageField(
        upload_to= "images",
        verbose_name= "Фотография"
    )
    instagram = models.URLField(
        verbose_name = "Инстаграм",
        blank =True, null=True
    )
    telegram = models.URLField(
        verbose_name = "Телеграмм",
        blank =True, null=True
    )
    experience = models.CharField(
        max_length = 255,
        verbose_name = "Опыт работы"
    )
    project = models.CharField(
        max_length = 255,
        verbose_name = "Кол-во Проектов"
    )
    client = models.CharField(
        max_length = 255,
        verbose_name = "Кол-во Клиентов"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "База "
        verbose_name_plural = "База"


class Slide(models.Model):
    libary = models.CharField(
        max_length = 255,
        verbose_name = "Знание библеотек и языков"
    )
    def __str__(self):
        return self.libary
    
    class Meta:
        verbose_name = " Слайд"
        verbose_name_plural = "Слайд"


class ServicesOffering(models.Model):
    image = models.ImageField(
        upload_to="images",
        verbose_name="Фогорафия"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name  ="Название"
    )
    class Meta:
        verbose_name = "Предложение услуг"
        verbose_name_plural = "Предложение услуг"
