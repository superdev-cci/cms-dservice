from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from commission.models import PvTransfer


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
        self.member_group = kwargs.get('group', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('time', 'member__mcode', 'member__honor', 'member__name_t') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('-time', 'member__mcode')

    def filter_queryset(self, queryset):
        queryset = super(PvTransferInReport, self).filter_queryset(queryset)
        return queryset.filter(member__honor=self.member_group)

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if x['member__mcode'] not in pool:
                pool[x['member__mcode']] = {
                    'name': x['member__name_t'],
                    'honor': x['member__honor'],
                    'data': {}
                }
            if self.get_type == 'daily':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y-%m-%d')] = float(x['total'])
            elif self.get_type == 'monthly':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'quarter':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'yearly':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y')] = float(x['total'])
        return pool
