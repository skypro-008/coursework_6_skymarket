from django.conf import settings
from django.db import models


class Ad(models.Model):
    """Модель объявления."""

    title = models.CharField(
        max_length=150,
        verbose_name="название товара",
        help_text="напишите название товара",
    )
    price = models.PositiveIntegerField(
        verbose_name="цена товара", help_text="введите цену товара"
    )
    description = models.TextField(
        verbose_name="описание товара", help_text="напишите описание товара"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="создатель объявления",
        help_text="автор объявления",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="время и дата создания объявления",
        help_text="время и дата создания объявления",
    )
    image = models.ImageField(
        upload_to="ads",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="загрузите изображение",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]


class Comment(models.Model):
    """Модель отзыва."""

    text = models.TextField(verbose_name="текст отзыва", help_text="напишите отзыв")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="автор отзыва",
        help_text="автор отзыва",
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        verbose_name="объявление, под которым оставлен отзыв",
        help_text="объявление, под которым оставлен отзыв",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="время и дата создания отзыва",
        help_text="время и дата создания отзыва",
    )

    def __str__(self):
        return f"Отзыв от {self.author.email} на объявление {self.ad.title}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
