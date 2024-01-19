import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter

from core.mixin import MonthMixIn
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class SalesAgFrSummaryReport(PeriodSummaryBase):
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('H',),
            'member__group__code__in': ('FR', 'MF'),
            'member__status_terminate': 0
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(SalesAgFrSummaryReport, self).__init__(*args, **kwargs)
        self.get_type = 'monthly'
        self.member_group = kwargs.get('type', ('AG',))
        self.Meta.filter['member__group__code__in'] = self.member_group

    def get_extend_queryset(self, queryset):
        return queryset.values('time', 'member__mcode', 'member__name_t') \
            .annotate(total=Sum('total')) \
            .order_by('-member')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)

        for x in queryset:
            time_index = x['time'].strftime('%Y-%b')
            member = x['member__mcode']
            if member in pool:
                pool[member]['data'][time_index] = int(x['total'])
            else:
                pool[member] = {
                    "code": member,
                    "name": x['member__name_t'],
                    "data": {
                        time_index: int(x['total'])
                    }
                }
        return pool
