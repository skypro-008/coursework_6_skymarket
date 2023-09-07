from django.urls import include, path
from rest_framework_nested import routers
from .apps import SalesConfig
from .views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели

app_name= SalesConfig.name

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')
comments_router = routers.NestedSimpleRouter(ads_router, 'ads', lookup='ad')
comments_router.register('comments', CommentViewSet, basename='ad_comment')

urlpatterns = [
    path('', include(ads_router.urls)),
    path('', include(comments_router.urls)),
]