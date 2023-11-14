from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializers import CommentSerializer, AdSerializer, AdDetailSerializer
from .paginators import AdPagination
from .models import Ad, Comment
from users.models import User
from .permissions import IsAdmin, IsOwner
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою

# ----------------------------------------------------------------
class AdViewSet(viewsets.ModelViewSet):
    '''Ad viewset Объявления'''

    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_serializer_class(self):
        '''Выбор сериализатора'''

        if self.action in ['list', 'personal_list']:
            return AdSerializer
        return AdDetailSerializer

    def get_permissions(self):
        '''Права доступа'''

        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        '''Создание объявления'''
        ad = serializer.save()
        ad.author = get_object_or_404(User, id=self.request.user.id)
        ad.save()

    @action(methods=['get'], detail=False, url_path='me')
    def personal_list(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


# ----------------------------------------------------------------

class CommentViewSet(viewsets.ModelViewSet):
    '''Comment viewset Отзывы'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        '''Права доступа'''

        if self.action == 'retrieve':
            permission_classes = [IsAdmin]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        '''Создание комментария'''
        comment = serializer.save()
        comment.author = get_object_or_404(User, id=self.request.user.id)
        comment.save()

    def get_queryset(self):
        return self.queryset.filter(ad=self.kwargs['ad_pk']).select_related("author")
