from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from core.authentication.legacy import BasicAuthDefault
from core.pagination import AdaptivePagination
from ..models import LogHpv
from ..serializers import LogHpvSerializer


class LogHpvView(viewsets.ReadOnlyModelViewSet):
    queryset = LogHpv.objects.all()
    serializer_class = LogHpvSerializer
    filter_backends = (
        SearchFilter, OrderingFilter,)
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination
    ordering_fields = ('mcode', 'inv_code', 'sano',)
    search_fields = ('mcode', 'inv_code', 'sano')
