from django.db import models
from django.db.models import Sum

from commission.models import PvTransfer
from ecommerce.models import SaleInvoice


class WeekCommission(models.Model):
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    name_t = models.CharField(max_length=255)
    fast_bonus = models.DecimalField(max_digits=15, decimal_places=2, db_column='ambonus')
    ws_bonus = models.DecimalField(max_digits=15, decimal_places=2, db_column='bmbonus')
    dmbonus = models.DecimalField(max_digits=15, decimal_places=2)
    fmbonus = models.DecimalField(max_digits=15, decimal_places=2)
    ato = models.DecimalField(max_digits=15, decimal_places=2)
    ato1 = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    rcode = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()
    pay = models.IntegerField()
    sano_ecom = models.CharField(max_length=255)
    sano_ato = models.CharField(max_length=255)
    sano_ewallet = models.CharField(max_length=255)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    resale = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'ali_commission'

    @property
    def fast_commission(self):
        return self.fast_bonus

    @property
    def ws_commission(self):
        return self.ws_bonus

    @property
    def auto_chip(self):
        return self.ato

    @property
    def total_commission(self):
        return self.total

    @property
    def resale_commission(self):
        return self.resale

    @property
    def date_issue(self):
        return self.fdate

    @property
    def date_end(self):
        return self.tdate

    @staticmethod
    def get_cumulative_ws(start, end, member=None):
        queryset = WeekCommission.objects.filter(fdate__range=(start, end))
        if member:
            queryset = queryset.filter(mcode=member).aggregate(total_balance=Sum('ws_bonus'))
        else:
            queryset = queryset.values('mcode') \
                .annotate(total_balance=Sum('ws_bonus')).order_by('mcode').order_by('-total_balance')

        return queryset

    @staticmethod
    def get_total_pv(select_round, lft=0, rgt=0):
        current_round = WeekCommission.objects.filter(rcode=select_round).first()
        transfer_pv = PvTransfer.objects.filter(sadate__range=(current_round.fdate, current_round.tdate),
                                                sa_type__in=('A', 'AM', 'AE'), cancel=0)
        if lft != 0 and rgt != 0:
            transfer_pv = transfer_pv.filter(member__line_lft__gte=lft, member__line_rgt__lte=rgt)

        transfer_pv = transfer_pv.aggregate(total_pv=Sum('tot_pv'))

        sale_pv = SaleInvoice.objects.filter(sadate__range=(current_round.fdate, current_round.tdate),
                                             sa_type__in=('A', 'Z',), cancel=0)
        if lft != 0 and rgt != 0:
            sale_pv = sale_pv.filter(member__line_lft__gte=lft, member__line_rgt__lte=rgt)
        sale_pv = sale_pv.aggregate(total_pv=Sum('tot_pv'))

        total_pv = 0
        if sale_pv['total_pv']:
            total_pv += sale_pv['total_pv']
        if transfer_pv['total_pv']:
            total_pv += transfer_pv['total_pv']
        return total_pv

    @staticmethod
    def get_total_bonus(select_round, lft=0, rgt=0):
        current_round = WeekCommission.objects.filter(rcode=select_round)
        if lft != 0 and rgt != 0:
            current_round = current_round.filter(member__line_lft__gte=lft, member__line_rgt__lte=rgt)
        current_round = current_round.aggregate(total_fast=Sum('fast_bonus'), total_ws=Sum('ws_bonus'))

        return current_round['total_fast'], current_round['total_ws']

    @staticmethod
    def calculate_summary(select_round, lft=0, rgt=0):
        pv = WeekCommission.get_total_pv(select_round, lft, rgt)
        fast, ws = WeekCommission.get_total_bonus(select_round, lft, rgt)

        return {
            'pv': float(pv),
            'paid_percent': float(((fast + ws) / pv) * 100),
            'fast': {
                'bonus': float(fast),
                'percent': float((fast / pv) * 100)
            },
            'ws': {
                'bonus': float(ws),
                'percent': float((ws / pv) * 100)
            }
        }
