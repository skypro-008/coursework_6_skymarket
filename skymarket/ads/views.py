from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsAdmin, IsOwner
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated


class AdPagination(pagination.PageNumberPagination):
    """Пагинация."""
    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели объявления."""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    def get_serializer_class(self):
        """Выбор сериалайзера."""
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer

    def get_permissions(self):
        """Выбор прав доступа."""
        if self.action == "list":
            permission_classes = [AllowAny]
        elif self.action in ["retrieve", "create", "me"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Сохранение автора объявления."""
        ad = serializer.save()
        ad.author = self.request.user
        ad.save()

    def get_queryset(self):
        """Вывод только своих объявлений или всех."""
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(
        detail=False,
        methods=[
            "get",
        ],
    )
    def me(self, request, *args, **kwargs):
        """Описание действия me."""
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели отзыва."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получение отзывов для определенного объявления."""
        ad_id = self.kwargs.get("ad_pk")
        return self.queryset.filter(ad=ad_id)

    def perform_create(self, serializer):
        """Сохранение автора отзыва и связывание с объявлением."""
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_permissions(self):
        """Выбор прав доступа."""
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAdmin | IsOwner]
        return [permission() for permission in permission_classes]
