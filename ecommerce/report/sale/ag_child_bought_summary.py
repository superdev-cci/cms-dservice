import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter

from core.mixin import MonthMixIn
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class AgChildBoughtSummaryReport(PeriodSummaryBase):
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('H',),
        }
        exclude = {
            'cancel': 1,
            'member__agency_ref__isnull': True
        }

    def __init__(self, *args, **kwargs):
        super(AgChildBoughtSummaryReport, self).__init__(*args, **kwargs)
        self.get_type = 'monthly'
        self.member_group = kwargs.get('type', ('AG',))

    def get_extend_queryset(self, queryset):
        return queryset.values('time', 'member__agency_ref__mcode', 'member__agency_ref__name_t') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('-member__agency_ref')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)

        for x in queryset:
            time_index = x['time'].strftime('%Y-%b')
            member = x['member__agency_ref__mcode']

            if member in pool:
                pool[member]['data'][time_index] = int(x['total'])
            else:
                pool[member] = {
                    "code": member,
                    "name": x['member__agency_ref__name_t'],
                    "data": {
                        time_index: int(x['total'])
                    }
                }
        return pool
