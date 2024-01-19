import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter

from core.mixin import MonthMixIn
from core.report.summary import PeriodSummaryBase
from commission.models import PvTransfer
from member.models import Member


class PvTransferOutReport(PeriodSummaryBase):
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('A', 'AE', 'AM')
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(PvTransferOutReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.has_member = kwargs.get('mem_code', None)
        self.get_org = kwargs.get('get_org', False)

    def get_extend_queryset(self, queryset):
        if self.get_org and self.has_member:
            return queryset.values('time', 'member__mcode', 'uid') \
                .annotate(total=Sum('tot_pv')) \
                .order_by('time', 'member__mcode', 'uid')
        return queryset.values('time') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('time')

    def filter_queryset(self, queryset):
        queryset = super(PvTransferOutReport, self).filter_queryset(queryset)
        if self.get_org and self.has_member:
            member = Member.objects.get(mcode=self.has_member)
            return queryset.filter(member__line_rgt__lte=member.line_rgt, member__line_lft__gte=member.line_lft)
        if self.has_member:
            return queryset.filter(member__mcode=self.has_member)
        return queryset

    @property
    def total(self):
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        return self.get_default_value(queryset)

    @property
    def out_total(self):
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        return self.get_pv_value(queryset)

    def get_default_value(self, queryset):
        pool = {}
        for x in queryset:
            if self.get_type == 'daily':
                pool[x['time'].strftime('%Y-%m-%d')] = float(x['total'])
            elif self.get_type == 'monthly':
                pool[x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'quarter':
                pool[x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'yearly':
                pool[x['time'].strftime('%Y')] = float(x['total'])
        return pool

    def get_pv_value(self, queryset):
        pool = {}
        for x in queryset:
            current = x['time'].strftime('%Y-%m-%d')
            member = x['member__mcode']
            user = x['uid']
            pv = int(x['total'])
            if pool.get(current) is None:
                pool[current] = {}

            if pool[current].get(member) is None:
                pool[current][member] = {}

            if pool[current][member].get(user) is None:
                pool[current][member][user] = pv
            else:
                pool[current][member][user] += pv

        return pool
