from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор')
    created_at = models.DateField(auto_now=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление')
    created_at = models.DateField(auto_now=True, verbose_name='дата создания')
