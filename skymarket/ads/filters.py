import django_filters
from .models import Ad


class AdsFilter(django_filters.rest_framework.FilterSet):
    """
    Фильтр поиска по названию
    """
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains', label='Название товара')
    class Meta:
        model = Ad
        fields = ["title"]