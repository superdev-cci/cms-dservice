import datetime
import operator
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Sum
from django.db import models

from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice, \
    SaleItem, \
    Product, \
    Promotion, \
    PromotionItem


class BranchSaleItemSummaryReport(PeriodSummaryBase):
    sale_select = ('A', 'H', 'L', 'B', 'CF')

    class Meta:
        model = SaleItem
        date_fields = 'sano_link__sadate'
        filter = {
            # 'sano_link__sa_type__in': ('A', 'H', 'L', 'B', 'CF', 'PM'),
            'sano_link__isnull': False
        }
        exclude = {
            'sano_link__cancel': 1,
            'sano_link__sa_type': 'I'
        }

    def __init__(self, *args, **kwargs):
        super(BranchSaleItemSummaryReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.use_only_value = kwargs.get('only_value', False)

        if isinstance(self.use_only_value, str):
            self.use_only_value = True if self.use_only_value == 'true' else False

        self.select_bill = kwargs.get('bill', self.sale_select)
        if self.select_bill is not None:
            self.select_bill = self.select_bill.split(',')
        self.select_item = kwargs.get('item', None)
        if self.select_item is not None:
            self.select_item = self.select_item.split(',')

    def filter_queryset(self, queryset):
        queryset = super(BranchSaleItemSummaryReport, self).filter_queryset(queryset)
        if self.use_only_value:
            queryset = queryset.filter(sano_link__sa_type__in=self.select_bill)
        if self.select_item:
            queryset = queryset.filter(pcode__in=self.select_item)
        return queryset

    def get_extend_queryset(self, queryset):
        return queryset.values('time', 'pcode', 'sano_link__inv_code') \
            .annotate(total_prices=Sum('amt'), total_qty=Sum('qty')) \
            .order_by('time', 'pcode', 'sano_link__inv_code')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            dt = x['time'].strftime('%Y-%m-%d')
            pcode = x['pcode']
            if pool.get(dt) is None:
                pool[dt] = {}

            # pool[dt][x['pcode']] = {
            #     'total_prices': float(x['total_prices']),
            #     'total_qty': float(x['total_qty']),
            #     # 'price': float(x['price'])
            # }

            if pcode not in pool[dt]:
                pool[dt][pcode] = {}

            branch = x['sano_link__inv_code']
            pool[dt][pcode][branch] = {
                'total_prices': float(x['total_prices']),
                'total_qty': float(x['total_qty']),
            }

            # if branch not in pool[dt][pcode]:
            #
            # pool[dt][x['pcode']] = {
            #     'total_prices': float(x['total_prices']),
            #     'total_qty': float(x['total_qty']),
            #     # 'price': float(x['price'])
            # }
            # print(x['pcode'], pool[dt][x['pcode']])
        return pool
