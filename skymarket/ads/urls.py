from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

app_name = SalesConfig.name

ads_router = SimpleRouter()
ads_router.register(r"ads", AdViewSet)
ads_router.register("ads", AdViewSet, basename="ads")
comments_router = routers.NestedSimpleRouter(ads_router, r"ads", lookup="ad")
comments_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),
]
