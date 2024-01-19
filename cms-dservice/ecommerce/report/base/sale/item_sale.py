from abc import ABC
from django.db.models import Sum
from core.mixin.report import AnnotateMixin
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleItem


class SaleItemSummary(PeriodSummaryBase, AnnotateMixin, ABC):
    sale_select = ('A', 'H', 'L', 'B', 'CF')
    # 'sano_link__sa_type__in': ('A', 'H', 'L', 'B', 'CF', 'PM'),

    class Meta:
        model = SaleItem
        date_fields = 'sano_link__sadate'
        filter = {
            'sano_link__isnull': False
        }
        exclude = {
            'sano_link__cancel': 1,
            'sano_link__sa_type': 'I'
        }

        annotate = {
            'field': ('time', 'pcode',),
            'order': ('time', 'pcode',),
            'function': {
                'total_prices': {
                    'fn': Sum,
                    'target': 'amt'
                },
                'total_qty': {
                    'fn': Sum,
                    'target': 'qty'
                }
            }
        }

    def __init__(self, *args, **kwargs):

        super(SaleItemSummary, self).__init__(*args, **kwargs)
        if 'select_bill' in kwargs:
            if kwargs.get('select_bill') is not None:
                if not isinstance(kwargs['select_bill'], (list, tuple)):
                    raise AttributeError('select_bill must be list or tuple')
                self.select_bill = kwargs['select_bill']
        else:
            self.select_bill = self.sale_select

        if 'items' in kwargs:
            if not isinstance(kwargs['items'], (list, tuple)):
                raise AttributeError('items must be list or tuple')
            self.select_item = kwargs['items']
        else:
            self.select_item = []

    def filter_queryset(self, queryset):
        queryset = super(SaleItemSummary, self).filter_queryset(queryset)
        queryset = queryset.filter(sano_link__sa_type__in=self.select_bill)

        if len(self.select_item):
            queryset = queryset.filter(pcode__in=self.select_item)
        return queryset

    def get_extend_queryset(self, queryset):

        return self.get_extend_annotate_queryset(queryset)
