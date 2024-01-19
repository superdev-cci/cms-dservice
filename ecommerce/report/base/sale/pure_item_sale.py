from abc import ABC
from django.db.models import Sum
from core.mixin.report import AnnotateMixin
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleItem, PromotionItem
from .item_sale import SaleItemSummary


class PureSaleItemSummary(SaleItemSummary):
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

    def filter_queryset(self, queryset):
        # self.select_item
        promotion = [x.promotion.pcode for x in
                     PromotionItem.objects.filter(pcode__in=self.select_item)]
        self.select_item = [*list(set(promotion)), *self.select_item]
        queryset = super(PureSaleItemSummary, self).filter_queryset(queryset)
        return queryset


