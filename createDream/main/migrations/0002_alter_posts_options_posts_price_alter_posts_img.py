# Generated by Django 5.0.4 on 2024-04-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='posts',
            name='price',
            field=models.TextField(blank=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.TextField(blank=True, verbose_name='Изображение'),
        ),
    ]