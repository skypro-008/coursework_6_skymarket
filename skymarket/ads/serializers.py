from rest_framework import serializers
from .models import Comment, Ad

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Comment(Комментарии).
    Реализованы поля - имя и фамилия автора.
    '''
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)

    class Meta:
        model = Comment
        exclude = ('id', 'author')


class AdSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Ad(Объявления).
    '''
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'image', 'price', 'description')


class AdDetailSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Ad(Объявления).
    Детальный вид объявления.
    Реализованы поля - имя, фамилия и электронная почта автора.
    '''
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_email = serializers.CharField(source="author.email", read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
