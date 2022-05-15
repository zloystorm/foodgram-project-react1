from rest_framework.pagination import PageNumberPagination
from foodgram.settings import SIZE_PAGE

class LimitPageNumberPagination(PageNumberPagination):
    page_size = SIZE_PAGE
    page_size_query_param = 'limit'
