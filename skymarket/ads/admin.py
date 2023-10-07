from django.contrib import admin

from .models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author', 'created_at')    #Поля, которые вы хотите отображать в списке объявлений
    list_filter = ('author',)    #Фильтры для удобства поиска
    search_fields = ('title', 'description')    #Поиск по названию и описанию

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'ad', 'author', 'created_at')    #Поля, которые вы хотите отображать в списке комментариев
    list_filter = ('author',)  #Фильтры для удобства поиска
