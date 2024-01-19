from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class SalesWithSponsorStructureJSONReport(PeriodSummaryBase):
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('H', 'A')
        }
        exclude = {
            'cancel': 1,
        }

    def __init__(self, *args, **kwargs):
        super(SalesWithSponsorStructureJSONReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.member = kwargs.get('member', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('time',) \
            .annotate(total_sales=Sum('total')) \
            .order_by('-time', )

    def filter_queryset(self, queryset):
        queryset = super(SalesWithSponsorStructureJSONReport, self).filter_queryset(queryset)
        return queryset.filter(member__sponsor_lft__gte=self.member.sponsor_lft,
                               member__sponsor_rgt__lte=self.member.sponsor_rgt)

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if self.get_type == 'daily':
                pool[x['time'].strftime('%Y-%m-%d')] = float(x['total_sales'])
            elif self.get_type == 'monthly':
                pool[x['time'].strftime('%Y-%b')] = float(x['total_sales'])
            elif self.get_type == 'quarter':
                pool[x['time'].strftime('%Y-%b')] = float(x['total_sales'])
            elif self.get_type == 'yearly':
                pool[x['time'].strftime('%Y')] = float(x['total_sales'])
        return pool
