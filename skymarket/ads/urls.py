from django.urls import include, path

# TODO настройка роутов для модели
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import AdViewSet, CommentViewSet, UserAdsListView

ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')

comments_router = NestedSimpleRouter(ads_router, 'ads', lookup='ad')
comments_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    # просмотр своих объявлений
    path('me/', UserAdsListView.as_view(), name='user_ads'),
    # объявления
    path('', include(ads_router.urls)),
    # комментарии
    path('', include(comments_router.urls)),

]
