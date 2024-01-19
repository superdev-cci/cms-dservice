from django.db.models import Sum

from commission.models import FastCommission
from core.report.summary import PeriodSummaryBase


class SummaryFastCommission(PeriodSummaryBase):
    class Meta:
        model = FastCommission
        date_fields = 'fdate'

    def __init__(self, *args, **kwargs):
        super(SummaryFastCommission, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.mcode = kwargs.get('mcode', None)

    def get_extend_queryset(self, queryset):
        if self.mcode:
            queryset = queryset.filter(mcode=self.mcode)
        return queryset.values('time').annotate(
            sum_total=Sum('total'),
            sum_bonus=Sum('bonus'),
            sum_pv=Sum('tot_pv')
        ).values('time', 'mcode', 'name_t', 'sum_total', 'sum_bonus', 'sum_pv')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            member_code = x['mcode']
            if member_code not in pool:
                pool[member_code] = {
                    'mcode': x['mcode'],
                    'name': x['name_t'],
                    'data': {}
                }
            data = {
                    'total': x['sum_total'],
                    'bonus': x['sum_bonus'],
                    'tot_pv': x['sum_pv'],
                    }
            if self.get_type == 'daily':
                pool[member_code]['data'][x['time'].strftime('%Y-%m-%d')] = data
            elif self.get_type == 'monthly':
                pool[member_code]['data'][x['time'].strftime('%Y-%b')] = data
            elif self.get_type == 'quarter':
                pool[member_code]['data'][x['time'].strftime('%Y-%b')] = data
            elif self.get_type == 'yearly':
                pool[member_code]['data'][x['time'].strftime('%Y')] = data
        return pool
