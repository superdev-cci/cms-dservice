from django.db.models import Sum

from commission.models import WeekCommission
from core.report.summary import PeriodSummaryBase


class SummaryWeekCommission(PeriodSummaryBase):
    """
    a class represent summary of each member's week commission
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): (Optional) member code of interested person
        honor (list): (Optional) member honor of interested group's member
    """
    class Meta:
        model = WeekCommission
        date_fields = 'fdate'

    def __init__(self, *args, **kwargs):
        super(SummaryWeekCommission, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.mcode = kwargs.get('mcode', None)
        self.honor = kwargs.get('honor', [])

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        if self.mcode:
            queryset = queryset.filter(mcode=self.mcode)
        else:
            if len(self.honor) != 0:
                queryset = queryset.filter(member__honor__in=self.honor)
        return queryset.values('time').annotate(
            sum_total=Sum('total'),
            sum_ws_bonus=Sum('ws_bonus'),
            sum_fast_bonus=Sum('fast_bonus'),
            sum_resale=Sum('resale')
        ).values('time', 'mcode', 'name_t', 'sum_total', 'sum_ws_bonus', 'sum_fast_bonus', 'sum_resale')

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
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
                    'fast': x['sum_fast_bonus'],
                    'ws': x['sum_ws_bonus'],
                    'resale': x['sum_resale'],
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

    @property
    def for_dataframe(self):
        """
        a method to process data and reform to dictionary for process in pandas DataFrame

        :return: (:obj:`dictionary`)
        """
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        pool = {}
        for x in queryset:
            if (x['mcode'], x['name_t']) not in pool:
                pool[(x['mcode'], x['name_t'])] = {
                    (x['time'], 'total'): float(x['sum_total']),
                    (x['time'], 'fast'): float(x['sum_fast_bonus']),
                    (x['time'], 'ws'): float(x['sum_ws_bonus']),
                    (x['time'], 'resale'): float(x['sum_resale']),
                }
            else:
                if (x['time'], 'name') not in pool[(x['mcode'], x['name_t'])]:
                    pool[(x['mcode'], x['name_t'])][(x['time'], 'total')] = float(x['sum_total'])
                    pool[(x['mcode'], x['name_t'])][(x['time'], 'fast')] = float(x['sum_fast_bonus'])
                    pool[(x['mcode'], x['name_t'])][(x['time'], 'ws')] = float(x['sum_ws_bonus'])
                    pool[(x['mcode'], x['name_t'])][(x['time'], 'resale')] = float(x['sum_resale'])
        return pool
