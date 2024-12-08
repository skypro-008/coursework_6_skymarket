from ads.models import Ad, Comment
from django.contrib import admin


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Просмотр объявлений."""

    list_display = ("pk", "author", "title", "price", "created_at")
    list_filter = (
        "author",
        "title",
    )
    search_fields = ("title", "description")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Просмотр отзывов."""

    list_display = ("pk", "ad", "author", "text", "created_at")
    list_filter = ("author",)
