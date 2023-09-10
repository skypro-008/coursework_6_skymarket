import django_filters
from .models import Ad


class AdsFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название товара')
    class Meta:
        model = Ad
        fields = ["title"]