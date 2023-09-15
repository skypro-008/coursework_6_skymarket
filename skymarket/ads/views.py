from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from .filters import AdsFilter
from .models import Ad, Comment
from .permissions import CustomPermission
from .serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    """
    Пагинация
    """
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    """
    Объявления
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)   #Бэкенд для обработки фильтра
    filterset_class = AdsFilter    #Набор полей для фильтрации
    pagination_class = AdPagination  # Используем PageNumberPagination
    #permission_classes = [CustomPermission]
    serializers = {
        "list": AdSerializer,
    }
    default_serializer = AdDetailSerializer

    permissions = {
        "create": [IsAuthenticated()],
        "retrieve": [IsAuthenticated()],
        "update": [IsAuthenticated(), CustomPermission()],
        "partial_update": [IsAuthenticated(), CustomPermission()],
        "destroy": [IsAuthenticated(), CustomPermission()],
    }
    default_permissions = [AllowAny()]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permissions)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Комментарии
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]

    def perform_create(self, serializer):
        user = self.request.user
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        serializer.save(author=user, ad=ad)

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, id=ad_id)
        return Comment.objects.filter(ad=ad)