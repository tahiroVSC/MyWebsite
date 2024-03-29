# Generated by Django 5.0.1 on 2024-02-07 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_about_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year1', models.IntegerField(verbose_name='Год')),
                ('year2', models.IntegerField(verbose_name='Год2')),
                ('direction', models.CharField(max_length=255, verbose_name='Направление')),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Настройки Путя',
                'verbose_name_plural': 'Настройка  Путя',
            },
        ),
    ]
