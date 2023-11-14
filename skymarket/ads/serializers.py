from rest_framework import serializers
from .models import Comment, Ad

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)

    class Meta:
        model = Comment
        exclude = ('id', 'author')


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'image', 'price', 'description')


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    phone = serializers.CharField(source='author.phone')

    class Meta:
        model = Ad
        fields = '__all__'
