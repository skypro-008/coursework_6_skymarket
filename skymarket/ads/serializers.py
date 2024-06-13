from rest_framework import serializers
from .models import Ad, Comment



class CommentSerializer(serializers.ModelSerializer):

    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_image = serializers.CharField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', "text", "created_at", "author_first_name", "author_last_name", "author_image"]


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'description')


class AdDetailSerializer(serializers.ModelSerializer):

    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        fields = ['id', "title", "image", "price", "phone", "description", "author_first_name", "author_last_name"]
