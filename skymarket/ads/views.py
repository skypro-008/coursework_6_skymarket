from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets

from .filters import AdsFilter
from .models import Ad, Comment
from .serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)   #Бэкенд для обработки фильтра
    filterset_class = AdsFilter    #Набор полей для фильтрации


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    #serializer_class = CommentSerializer
