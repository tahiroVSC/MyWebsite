# Generated by Django 5.0.1 on 2024-02-05 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_slide_alter_index_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='languages',
        ),
        migrations.AlterField(
            model_name='slide',
            name='libary',
            field=models.CharField(max_length=255, verbose_name='Знание библеотек и языков'),
        ),
    ]