from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter
from datetime import datetime, timedelta, date
# import datetime
# from dateutil.relativedelta import relativedelta
from commission.functions.analyze.week_team_summary import WeakTeamSummary
from core.authentication.legacy import BasicAuthDefault
from core.pagination import StandardResultsSetPagination
from ..serializers import WeekCommissionSerializer
from ..models import WeekCommission
from member.models import Member
from commission.report import PvActivityReport, WeekCommissionMemberReport


class MemberOrgReportView(viewsets.ModelViewSet):
    queryset = WeekCommission.objects.all()
    serializer_class = WeekCommissionSerializer
    ordering_fields = ('time', 'mcode', 'name_t', 'total_ws', 'ws_bonus', 'fdate')
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    member_field = 'member'
    member_model = Member

    def list(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def get_weak_team(self, request, *args, **kwargs):
        data = request.query_params
        period = data.get('period', 'monthly')
        # mem_code = data.get('mcode', None)
        end = data.get('end')
        start = data.get('start')
        try:
            if start is None or end is None:
                start = date.today().replace(month=1, day=1).strftime('%Y-%m-%d')
                end = date.today().replace(month=12, day=31).strftime('%Y-%m-%d')

            time_range = (start, end)
            builder = WeakTeamSummary(head_mcode=data.get('ref'))
            queryset = builder.get_queryset(request, **{
                'time_range': time_range,
                'get_type': period
            })
            queryset = OrderingFilter().filter_queryset(self.request, queryset, self)
            page = self.paginate_queryset(queryset)
            if page is not None:
                return self.get_paginated_response(builder.serialized(page))

            return Response(queryset, status.HTTP_200_OK)
        except Member.DoesNotExist as e:
            result = {"message": "wrong request pls identify \"ref\""}
            return Response(result, status.HTTP_503_SERVICE_UNAVAILABLE)
