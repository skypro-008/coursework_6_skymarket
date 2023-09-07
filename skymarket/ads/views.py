from rest_framework import pagination, viewsets
from .models import Ad, Comment
from .serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    #serializer_class = CommentSerializer
