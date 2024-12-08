from ads.models import Ad, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для комментария."""

    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_image = serializers.ImageField(source="author.image", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    """Сериалайзер для объявления."""

    class Meta:
        model = Ad
        fields = (
            "id",
            "title",
            "price",
            "description",
            "image",
        )


class AdDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для детального представления объявления."""

    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_phone = serializers.CharField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        exclude = ("created_at",)
