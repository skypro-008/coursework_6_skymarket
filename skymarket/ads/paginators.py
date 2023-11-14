from rest_framework.pagination import PageNumberPagination


class AdPagination(PageNumberPagination):
    '''Пагинация для списка объявлений'''
    page_size = 4
    page_size_query_param = 'page_size'
