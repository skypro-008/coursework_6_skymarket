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

'''Ad - ОБЪЯВЛЕНИЯ'''
# ----------------------------------------------------------------


class AdViewSet(viewsets.ModelViewSet):
    '''
    Ad, viewset, Объявления.
    '''

    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_serializer_class(self):
        '''
        Выбор сериализатора зависит от self.action.
        '''

        if self.action in ['list', 'personal_list']:
            return AdSerializer
        return AdDetailSerializer

    def get_permissions(self):
        '''
        Права доступа.
        Неавторизированный пользователь может:
        - видеть список объявлений.

        Авторизированный (IsAuthenticated) пользователь (IsOwner) может:
        - видеть список объявлений,
        - видеть одно объявление (детально),
        - создавать объявления,
        - редактировать свои объявления,
        - удалять свои объявления.

        Авторизированный (IsAuthenticated) пользователь (IsAdmin) может:
        - видеть список объявлений,
        - видеть одно объявление (детально),
        - создавать объявления,
        - редактировать свои и чужие объявления,
        - удалять свои и чужие объявления.
        '''

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
        '''
        Создание объявления и установление автора.
        '''
        ad = serializer.save()
        ad.author = get_object_or_404(User, id=self.request.user.id)
        ad.save()

    @action(methods=['get'], detail=False, url_path='me')
    def personal_list(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


'''Comment - КОММЕНТАРИИ'''
# ----------------------------------------------------------------


class CommentViewSet(viewsets.ModelViewSet):
    '''
    Comment, viewset, Комментарии.
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        '''
        Права доступа.
        Неавторизированный пользователь может читать комментарии.

        Авторизированный (IsAuthenticated) пользователь (IsOwner) может:
        - читать комментарии к объявлениям,
        - писать комментарии,
        - редактировать свои комментарии,
        - удалять свои комментарии.

        Авторизированный (IsAuthenticated) пользователь (IsAdmin) может:
        - читать комментарии к объявлениям,
        - писать комментарии,
        - редактировать свои и чужие комментарии,
        - удалять свои и чужие комментарии.
        '''

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
        '''
        Создание комментария и установление автора.
        '''
        comment = serializer.save()
        comment.author = get_object_or_404(User, id=self.request.user.id)
        comment.save()

    def get_queryset(self):
        return self.queryset.filter(ad=self.kwargs['ad_pk']).select_related("author")


'''Ad - СВОИ ОБЪЯВЛЕНИЯ'''
# ----------------------------------------------------------------


class UserAdsListView(ListAPIView):
    '''
    Ad, generics, Объявления пользователя.
    '''
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        '''
        Список всех объявлений выбранного пользователя.
        '''
        self.queryset = self.queryset.filter(auhtor=request.user)
        return super().list(request, *args, *kwargs)
