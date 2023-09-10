from django.utils import timezone
from django.conf import settings
from django.db import models


#from skymarket.users.models import User


NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    """
    Модель объявления
    """
    title = models.CharField(verbose_name='название', max_length=200, default= " ")
    price = models.PositiveIntegerField(verbose_name='цена', **NULLABLE)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(verbose_name='изображение', upload_to='ads', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', related_name='ads')
    created_at = models.DateTimeField(verbose_name='время создания', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    """
    Модель комментарии
    """
    text = models.CharField(verbose_name='текст', max_length=1000, default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE,  null=True, verbose_name='объявление')
    created_at = models.DateTimeField(verbose_name='время создания', default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
