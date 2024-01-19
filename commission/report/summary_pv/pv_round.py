from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice
from commission.models import PvTransfer, WeekCommission, MonthCommission


class PvFromSaleInvoice(PeriodSummaryBase):
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {'sa_type__in': ('A', 'Z')}
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(PvFromSaleInvoice, self).__init__(*args, **kwargs)
        self.get_type = 'monthly'

    def get_extend_queryset(self, queryset):
        return queryset.values('time').annotate(
            sum_pv=Sum('tot_pv')
        ).values('time', 'sum_pv')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if x['time'].strftime('%Y-%m-%d') not in pool:
                pool[x['time'].strftime('%Y-%m-%d')] = {'pv': x['sum_pv']}
            else:
                pool[x['time'].strftime('%Y-%m-%d')]['pv'] += x['sum_pv']
        return pool


class PvFromPvTransfer(PeriodSummaryBase):
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {'sa_type__in': ('A', 'AE', 'AM')}
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(PvFromPvTransfer, self).__init__(*args, **kwargs)
        self.get_type = 'monthly'

    def get_extend_queryset(self, queryset):
        return queryset.values('time').annotate(
            sum_pv=Sum('tot_pv')
        ).values('time', 'sum_pv')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if x['time'].strftime('%Y-%m-%d') not in pool:
                pool[x['time'].strftime('%Y-%m-%d')] = {'pv': x['sum_pv']}
            else:
                pool[x['time'].strftime('%Y-%m-%d')]['pv'] += x['sum_pv']
        return pool


class BonusFromWeekCommission(PeriodSummaryBase):
    class Meta:
        model = WeekCommission
        date_fields = 'fdate'

    def __init__(self, *args, **kwargs):
        super(BonusFromWeekCommission, self).__init__(*args, **kwargs)
        self.get_type = 'monthly'

    def get_extend_queryset(self, queryset):
        return queryset.values('time').annotate(
            sum_ws_bonus=Sum('ws_bonus'),
            sum_fast_bonus=Sum('fast_bonus'),
        ).values('time', 'sum_ws_bonus', 'sum_fast_bonus')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if x['time'].strftime('%Y-%m-%d') not in pool:
                pool[x['time'].strftime('%Y-%m-%d')] = {
                    'ws_bonus': x['sum_ws_bonus'],
                    'fast_bonus': x['sum_fast_bonus']
                }
            else:
                pool[x['time'].strftime('%Y-%m-%d')]['ws_bonus'] += x['sum_ws_bonus']
                pool[x['time'].strftime('%Y-%m-%d')]['fast_bonus'] += x['sum_fast_bonus']
        return pool


class BonusFromMonthCommission(PeriodSummaryBase):
    class Meta:
        model = MonthCommission
        date_fields = 'fdate'

    def __init__(self, *args, **kwargs):
        super(BonusFromMonthCommission, self).__init__(*args, **kwargs)
        self.get_type = 'monthly'

    def get_extend_queryset(self, queryset):
        return queryset.values('time').annotate(
            sum_dmbonus=Sum('dmbonus'),
            sum_embonus=Sum('embonus'),
        ).values('time', 'sum_dmbonus', 'sum_embonus')

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if x['time'].strftime('%Y-%m-%d') not in pool:
                pool[x['time'].strftime('%Y-%m-%d')] = {
                    'dmbonus': x['sum_dmbonus'],
                    'embonus': x['sum_embonus']
                }
            else:
                pool[x['time'].strftime('%Y-%m-%d')]['dmbonus'] += x['sum_dmbonus']
                pool[x['time'].strftime('%Y-%m-%d')]['embonus'] += x['sum_embonus']
        return pool


class DiscountFromSaleInvoice(PeriodSummaryBase):
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {'sa_type__in': ('H',)}
        exclude = {'cancel': 1, 'member__group__code': 'MB'}

    def __init__(self, *args, **kwargs):
        super(DiscountFromSaleInvoice, self).__init__(*args, **kwargs)
        self.get_type = 'monthly'

    def get_extend_queryset(self, queryset):
        mf = queryset.filter(member__group__code='MF', tot_pv__gte=1000)
        fr = queryset.filter(member__group__code='FR', tot_pv__gte=1000)
        ag = queryset.filter(member__group__code='AG', tot_pv__gte=3000)
        data_dict = {
            'AG': ag.values('time').annotate(
                sum_pv=Sum('tot_pv'), sum_paid=(Sum('tot_pv')*0.3)
            ).values('time', 'sum_pv', 'sum_paid'),
            'FR': fr.values('time').annotate(
                sum_pv=Sum('tot_pv'), sum_paid=(Sum('tot_pv')*0.15)
            ).values('time', 'sum_pv', 'sum_paid'),
            'MF': mf.values('time').annotate(
                sum_pv=Sum('tot_pv'), sum_paid=(Sum('tot_pv')*0.1)
            ).values('time', 'sum_pv', 'sum_paid')
        }
        return data_dict

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for gr in queryset:
            for x in queryset[gr]:
                if x['time'].strftime('%Y-%m-%d') not in pool:
                    pool[x['time'].strftime('%Y-%m-%d')] = {
                        'pv': x['sum_pv'],
                        'paid': x['sum_paid']
                    }
                else:
                    pool[x['time'].strftime('%Y-%m-%d')]['pv'] += x['sum_pv']
                    pool[x['time'].strftime('%Y-%m-%d')]['paid'] += x['sum_paid']
        return pool

