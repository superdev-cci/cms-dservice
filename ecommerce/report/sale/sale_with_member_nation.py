from django.db.models import Sum, Q

from ecommerce.report.base.sale import SaleInvoiceSummaryBase


class SaleInvoiceSummaryWithNation(SaleInvoiceSummaryBase):
    class Meta(SaleInvoiceSummaryBase.Meta):
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
        super(SaleInvoiceSummaryWithNation, self).__init__(*args, **kwargs)
        self.nation = kwargs.get('nation', None)

    @property
    def total(self):
        pool = {}
        for x, y in self.nation:
            queryset = self.get_query_set(self.start, self.end, 'monthly')
            queryset = queryset.filter(Q(mcode__startswith=x) | Q(member__national=y))
            for instance in queryset:

                if instance['time'].strftime('%Y-%b') not in pool:
                    pool[instance['time'].strftime('%Y-%b')] = {}

                pool[instance['time'].strftime('%Y-%b')][x] = {
                    'prices': float(instance['total_prices']),
                    'pv': float(instance['total_pv'])
                }
        return pool
