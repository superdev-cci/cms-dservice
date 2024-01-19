import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter

from core.mixin import MonthMixIn
from core.report.summary import PeriodSummaryBase
from commission.models import PvTransfer
from ecommerce.models import SaleInvoice


class PvExpiredReport(PeriodSummaryBase):
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('AE',)
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(PvExpiredReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', 'daily')
        self.group_by = kwargs.get('group', 'member__mtype1')

    def get_extend_queryset(self, queryset):
        return queryset.values('time', self.group_by) \
            .annotate(total=Sum('tot_pv')) \
            .order_by('time')

    def filter_queryset(self, queryset):
        queryset = super(PvExpiredReport, self).filter_queryset(queryset)
        return queryset

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            current = x['time'].strftime('%Y-%m-%d')
            member_type = x[self.group_by]
            if pool.get(current) is None:
                pool[current] = {}
            method = getattr(self, 'get_by_{}'.format(self.group_by))
            if method is not None:
                method(pool, current, member_type, x)
        return pool

    def get_by_member__level(self, pool, key, member_type, data):
        if member_type == 'DIS':
            pool[key]['DIS'] = int(data['total'])
        elif member_type == 'PRO':
            pool[key]['PRO'] = int(data['total'])
        else:
            pool[key]['VIP'] = int(data['total'])

    def get_by_member__mtype1(self, pool, key, member_type, data):
        if member_type == 'MB':
            pool[key]['MB'] = int(data['total'])
        elif member_type == 'FR':
            pool[key]['FR'] = int(data['total'])
        else:
            pool[key]['AG'] = int(data['total'])
