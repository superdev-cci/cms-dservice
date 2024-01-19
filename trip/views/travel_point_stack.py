from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import datetime

from core.authentication import MemberTokenAuthentication
from core.authentication.legacy import BasicAuthDefault
from core.pagination import AdaptivePagination
from ..filter import TravelPointStackMemberAccessFilter
from ..serializers import TravelPointStackSerializer
from ..models import TravelPointStack


class TravelPointStackView(viewsets.ReadOnlyModelViewSet):
    queryset = TravelPointStack.objects.all().select_related('member',)
    serializer_class = TravelPointStackSerializer
    pagination_class = AdaptivePagination
    authentication_classes = (BasicAuthDefault, MemberTokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    filter_backends = (
        SearchFilter, OrderingFilter, TravelPointStackMemberAccessFilter
    )
    ordering_fields = ('stamp_date',)
    search_fields = ('member__name_t', 'member__mcode',)
