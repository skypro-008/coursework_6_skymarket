from django.contrib import admin

from .models import Ad, Comment

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    '''
    Объявления - отображение в админ-панели Jango.
    Фильтрует по ФИ автора и названию товара.
    Поиск в названии товара и его описании.
    '''
    list_display = ('pk', 'author', 'title', 'price', 'created_at')
    list_filter = ('author', 'title',)
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Комментарии - отображение в админ-панели Jango.
    Фильтрует по ФИ автора.
    '''
    list_display = ('pk', 'ad', 'author', 'text', 'created_at')
    list_filter = ('author',)
