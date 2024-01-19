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


class PvTransferInReport(PeriodSummaryBase):

    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('Y',)
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(PvTransferInReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.has_member = kwargs.get('mem_code', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('time') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('time')

    def filter_queryset(self, queryset):
        queryset = super(PvTransferInReport, self).filter_queryset(queryset)
        if self.has_member:
            return queryset.filter(member__mcode=self.has_member)
        return queryset

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
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


class SaleInvoiceInReport(PeriodSummaryBase):

    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('H',)
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(SaleInvoiceInReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.has_member = kwargs.get('mem_code', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('time') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('time')

    def filter_queryset(self, queryset):
        queryset = super(SaleInvoiceInReport, self).filter_queryset(queryset)
        if self.has_member:
            return queryset.filter(member__mcode=self.has_member)
        return queryset

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
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