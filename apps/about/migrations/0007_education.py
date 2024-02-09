# Generated by Django 5.0.1 on 2024-02-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_alter_path_year2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year1', models.IntegerField(verbose_name='Год1')),
                ('year2', models.IntegerField(verbose_name='Год2')),
                ('direction', models.CharField(max_length=255, verbose_name='Направлние')),
                ('company', models.CharField(max_length=255, verbose_name='Обучение')),
            ],
            options={
                'verbose_name': 'Настройки Оброзавания',
                'verbose_name_plural': 'Настройка Оброзавания',
            },
        ),
    ]