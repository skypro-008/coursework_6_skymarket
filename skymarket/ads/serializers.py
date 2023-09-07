from rest_framework import serializers
from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    model = Comment
    fields = ('text')


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = '__all__'

class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass
