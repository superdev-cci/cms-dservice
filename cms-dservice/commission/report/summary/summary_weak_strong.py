from django.db.models import Sum

from commission.models import WeakStrongSummary
from core.report.summary import PeriodSummaryBase


class SummaryWeakStrong(PeriodSummaryBase):
    class Meta:
        model = WeakStrongSummary
        date_fields = 'date_issue'

    def __init__(self, *args, **kwargs):
        super(SummaryWeakStrong, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.mcode = kwargs.get('mcode', None)
        self.honor = kwargs.get('honor', [])

    def get_extend_queryset(self, queryset):
        if self.mcode:
            queryset = queryset.filter(mcode=self.mcode)
        else:
            if len(self.honor) != 0:
                queryset = queryset.filter(member__honor__in=self.honor)
        return queryset.values('time') \
            .annotate(
            sum_total=Sum('total'),
            sum_balance=Sum('balance'),
            sum_current_left=Sum('current_left'),
            sum_current_right=Sum('current_right')
        ).values('time', 'mcode', 'member_name', 'sum_total', 'sum_balance', 'sum_current_left', 'sum_current_right')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            member_code = x['mcode']
            if member_code not in pool:
                pool[member_code] = {
                    'mcode': x['mcode'],
                    'name': x['member_name'],
                    'data': {}
                }
            data = {
                    'total': x['sum_total'],
                    'balance': x['sum_balance'],
                    'current_left': x['sum_current_left'],
                    'current_right': x['sum_current_right'],
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
