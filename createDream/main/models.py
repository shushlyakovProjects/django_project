from django.db import models

class Posts(models.Model):
    title = models.CharField('Название', max_length=50)
    body = models.TextField('Описание')
    img = models.TextField('Изображение', blank=True)
    price = models.TextField('Цена', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



