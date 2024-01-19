from abc import ABC
from django.db.models import Sum
from core.mixin.report import AnnotateMixin
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class SaleInvoiceSummaryBase(PeriodSummaryBase, AnnotateMixin, ABC):
    sale_select = ('A', 'H', 'L', 'B', 'CF')
    # 'sano_link__sa_type__in': ('A', 'H', 'L', 'B', 'CF', 'PM'),

    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        exclude = {
            'cancel': 1,
            'sa_type': 'I'
        }

        annotate = {
            'field': ('time',),
            'order': ('time',),
            'function': {
                'total_prices': {
                    'fn': Sum,
                    'target': 'total'
                },
                'total_pv': {
                    'fn': Sum,
                    'target': 'tot_pv'
                }
            }
        }

    def __init__(self, *args, **kwargs):

        super(SaleInvoiceSummaryBase, self).__init__(*args, **kwargs)
        if 'select_bill' in kwargs:
            if kwargs.get('select_bill') is not None:
                if not isinstance(kwargs['select_bill'], (list, tuple)):
                    raise AttributeError('select_bill must be list or tuple')
                self.select_bill = kwargs['select_bill']
        else:
            self.select_bill = self.sale_select

    def get_extend_queryset(self, queryset):
        return self.get_extend_annotate_queryset(queryset)
