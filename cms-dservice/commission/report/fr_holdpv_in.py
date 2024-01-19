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
from member.models import Member


class FrPvTransferInReport(PeriodSummaryBase):
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('Y',),
            'member__group__code__in': ('FR', 'MF')
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(FrPvTransferInReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.has_member = kwargs.get('mem_code', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('time', 'member__mcode', 'member__name_t') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('-member')

    def filter_queryset(self, queryset):
        queryset = super(FrPvTransferInReport, self).filter_queryset(queryset)
        if self.has_member:
            return queryset.filter(member__mcode=self.has_member)
        return queryset

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
