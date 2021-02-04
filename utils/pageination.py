from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    # 默认条件下，每一页显示的条数为2
    page_size = 2
    page_size_query_param = 's'
    # 指定前端能分页的最大page_size
    max_page_size = 50