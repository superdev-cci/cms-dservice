from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from core.authentication.legacy import BasicAuthDefault
from core.pagination import AdaptivePagination
from ..models import Log
from ..serializers import LogSerializer


class LogView(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_backends = (
        SearchFilter, OrderingFilter,)
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination
    ordering_fields = ('sys_id',)
    search_fields = ('subject', 'detail',)
