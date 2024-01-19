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
from ..filter import TravelPointStatementMemberAccessFilter
from ..functions.travel_point_stack import TravelPointStackOperator
from ..serializers import TravelPointUseStatementSerializer
from ..models import TravelPointUseStatement


class TravelPointUseStatementView(viewsets.ReadOnlyModelViewSet):
    queryset = TravelPointUseStatement.objects.all().select_related('member', 'trip')
    serializer_class = TravelPointUseStatementSerializer
    pagination_class = AdaptivePagination
    authentication_classes = (BasicAuthDefault, MemberTokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    filter_backends = (
        SearchFilter, OrderingFilter, TravelPointStatementMemberAccessFilter
    )
    ordering_fields = ('issue_date',)
    search_fields = ('member__name_t', 'trip__name',)

    @action(detail=True, methods=['PUT'], authentication_classes=(BasicAuthDefault,),
            permission_classes=(IsAuthenticated,))
    def cancel(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        if instance.state == "CM":
            stack = TravelPointStackOperator(member=instance.member)
            if instance.gold_coin > 0:
                stack.push_gold_stack(instance.gold_coin)
            if instance.silver_coin > 0:
                stack.push_silver_stack(instance.silver_coin)
            instance.state = "CA"
            instance.save()
        else:
            Response(status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_200_OK)
