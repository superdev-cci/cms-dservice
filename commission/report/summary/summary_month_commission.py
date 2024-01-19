from django.db.models import Sum

from commission.models import MonthCommission
from core.report.summary import PeriodSummaryBase


class SummaryMonthCommission(PeriodSummaryBase):
    """
    a class represent summary of each member's month commission
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
        model = MonthCommission
        date_fields = 'fdate'

    def __init__(self, *args, **kwargs):
        super(SummaryMonthCommission, self).__init__(*args, **kwargs)
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
            if isinstance(self.mcode, list):
                queryset = queryset.filter(mcode__in=self.mcode)
            else:
                queryset = queryset.filter(mcode=self.mcode)
        else:
            if len(self.honor) != 0:
                queryset = queryset.filter(member__honor__in=self.honor)
        return queryset.values('time') \
            .annotate(
                sum_total=Sum('total'),
                sum_dmbonus=Sum('dmbonus'),
                sum_embonus=Sum('embonus')
            ).values('time', 'mcode', 'name_t', 'sum_total', 'sum_dmbonus', 'sum_embonus')

    @property
    def queryset(self):
        return self.get_query_set(self.start, self.end, self.get_type)

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
                'matching': x['sum_dmbonus'],
                'all_sales': x['sum_embonus'],
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
                    (x['time'], 'matching'): float(x['sum_dmbonus']),
                    (x['time'], 'all_sales'): float(x['sum_embonus']),
                }
            else:
                if (x['time'], 'name') not in pool[(x['mcode'], x['name_t'])]:
                    pool[(x['mcode'], x['name_t'])][(x['time'], 'total')] = float(x['sum_total'])
                    pool[(x['mcode'], x['name_t'])][(x['time'], 'matching')] = float(x['sum_dmbonus'])
                    pool[(x['mcode'], x['name_t'])][(x['time'], 'all_sales')] = float(x['sum_embonus'])
        return pool

