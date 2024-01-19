import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter

from core.filters import MemberDownLineSelectFilter
from core.report.summary import PeriodSummaryBase
from commission.models import WeekCommission
from member.models import Member


class WeekCommissionMemberReport(PeriodSummaryBase):
    class Meta:
        model = WeekCommission
        date_fields = 'fdate'

    def __init__(self, *args, **kwargs):
        super(WeekCommissionMemberReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        query_params = kwargs['request'].query_params
        try:
            self.member = Member.objects.get(mcode=query_params.get('code'))
        except:
            self.member = None

    def get_extend_queryset(self, queryset):
        return queryset.values('time') \
            .annotate(total_fast=Sum('fast_bonus'),
                      total_ws=Sum('ws_bonus'),
                      total_resale=Sum('resale')) \
            .order_by('time')

    def filter_queryset(self, queryset):
        view = self.context.get('view')
        request = self.context.get('request')
        queryset = super(WeekCommissionMemberReport, self).filter_queryset(queryset)
        return MemberDownLineSelectFilter().filter_queryset(request, queryset, view)

    @property
    def total(self):
        pool = {
            'member': self.member.full_name if self.member is not None else '-',
            'count': 0,
            'items': {},
            'total': {
                'fast': 0,
                'ws': 0,
                'resale': 0,
            }
        }
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if self.get_type == 'daily':
                pool['items'][x['time'].strftime('%Y-%m-%d')] = self.create_response(x)
            elif self.get_type == 'monthly':
                pool['items'][x['time'].strftime('%Y-%b')] = self.create_response(x)
            elif self.get_type == 'quarter':
                pool['items'][x['time'].strftime('%Y-%b')] = self.create_response(x)
            elif self.get_type == 'yearly':
                pool['items'][x['time'].strftime('%Y')] = self.create_response(x)

            pool['total']['fast'] += float(x['total_fast'])
            pool['total']['ws'] += float(x['total_ws'])
            pool['total']['resale'] += float(x['total_resale'])
            pool['count'] += 1

        return pool

    def create_response(self, obj):
        return {
            'fast': float(obj['total_fast']),
            'ws': float(obj['total_ws']),
            'resale': float(obj['total_resale']),
        }
