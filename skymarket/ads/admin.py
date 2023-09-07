from django.contrib import admin

from .models import Ad, Comment

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
admin.site.register(Ad)
admin.site.register(Comment)
