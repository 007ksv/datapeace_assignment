from rest_framework import pagination

class CustomUserLimitOffsetPagination(pagination.LimitOffsetPagination):

	default_limit = 5
