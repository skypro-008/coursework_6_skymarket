from rest_framework import serializers

from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'author', 'created_at']
        read_only_fields = ['id', 'created_at', 'author']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной.")
        return value


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
