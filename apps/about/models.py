from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(
        upload_to="images",
        verbose_name= "Фотография"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Язык програмиравание"
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

class Skills(models.Model):
      title = models.CharField(
        max_length = 255,
        verbose_name = "Скиллы"
    )
      def __str__(self):
            return self.title
    
      class Meta:
          verbose_name = "Настройки скиллов"    
          verbose_name_plural = "Настройка склиллов"

class Path(models.Model):
    year1 = models.IntegerField(
        verbose_name = "Год"
    )
    year2 = models.CharField(
        max_length = 255,
        verbose_name = "Год2"
    )
    direction = models.CharField(
        max_length = 255,
        verbose_name = "Направление"    
    )
    company = models.CharField(
        max_length = 255,
        verbose_name = "Компания"
    )
    def __str__(self):
            return self.company
    
    class Meta:
          verbose_name = "Настройки Путя"    
          verbose_name_plural = "Настройка  Путя"

class Education(models.Model):
    year1 = models.IntegerField(
        verbose_name = "Год1"
    )
    year2 = models.IntegerField(
        verbose_name = "Год2"
    )
    direction = models.CharField(
        max_length = 255,
        verbose_name = "Направлние"
    )
    company = models.CharField(
        max_length = 255,
        verbose_name = "Обучение"
    )
    def __str__(self):
            return self.company
    
    class Meta:
          verbose_name = "Настройки Оброзавания"    
          verbose_name_plural = "Настройка Оброзавания"

