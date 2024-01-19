from core.report.summary import PeriodSummaryBase
from django.db.models import Sum
from ecommerce.models.sale_invoice import SaleInvoice


class SaleSummaryReport(PeriodSummaryBase):

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
        super(SaleSummaryReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('time') \
            .annotate(total=Sum('total'), premium=Sum('txtpremium')) \
            .order_by('time')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if self.get_type == 'daily':
                pool[x['time'].strftime('%Y-%m-%d')] = float(x['total']) - float(x['premium'])
            elif self.get_type == 'monthly':
                pool[x['time'].strftime('%Y-%b')] = float(x['total']) - float(x['premium'])
            elif self.get_type == 'quarter':
                pool[x['time'].strftime('%Y-%b')] = float(x['total']) - float(x['premium'])
            elif self.get_type == 'yearly':
                pool[x['time'].strftime('%Y')] = float(x['total']) - float(x['premium'])
        return pool

    @property
    def total_without_vat(self):
        pool = {}
        for k, v in self.total.items():
            pool[k] = (v * 100) / 107
        return pool
