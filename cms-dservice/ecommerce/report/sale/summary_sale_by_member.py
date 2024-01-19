import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter

from core.mixin import MonthMixIn
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class SummarySaleByMemberReport(PeriodSummaryBase):

    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('A', 'H', 'L', 'B', 'PM')
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(SummarySaleByMemberReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('mcode', 'name_t') \
            .annotate(sum_total=Sum('total'), sum_pv=Sum('tot_pv')) \
            .order_by('-sum_total')

    @property
    def total(self):
        return self.get_query_set(self.start, self.end, self.get_type)[0:20]

