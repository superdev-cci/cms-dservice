from commission.models.cal_round.week_round import WeekRound
from commission.models.cal_round.month_round import MonthRound
from commission.serializers import WeekRoundSerializer, MonthRoundSerializer
from .pv_round import PvFromSaleInvoice, PvFromPvTransfer, BonusFromWeekCommission, BonusFromMonthCommission, \
    DiscountFromSaleInvoice


class WeekRoundReport(object):

    def __init__(self, *args, **kwargs):
        self.start = kwargs.get('start', None)
        self.end = kwargs.get('end', None)
        self.round = self.get_round()

    def get_round(self):
        queryset = WeekRound.objects.filter(fdate__gte=self.start, tdate__lte=self.end)
        round_list = WeekRoundSerializer(queryset, many=True).data
        return round_list

    @property
    def total(self):
        result = {}
        for dict_date in self.round:
            pv_si = PvFromSaleInvoice(start=dict_date['fdate'], end=dict_date['tdate']).total
            pv_tf = PvFromPvTransfer(start=dict_date['fdate'], end=dict_date['tdate']).total
            bn_wk = BonusFromWeekCommission(start=dict_date['fdate'], end=dict_date['tdate']).total
            if dict_date['fdate'] in pv_si:
                result[dict_date['fdate'] + " to " + dict_date['tdate']] = {
                    'sum_total_pv': pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv'],
                    'fast_bonus': bn_wk[dict_date['fdate']]['fast_bonus'],
                    'percent_fast': bn_wk[dict_date['fdate']]['fast_bonus'] * 100 / (
                            pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']),
                    'ws_bonus': bn_wk[dict_date['fdate']]['ws_bonus'],
                    'percent_ws': bn_wk[dict_date['fdate']]['ws_bonus'] * 100 / (
                            pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']),
                    'sum_bonus': bn_wk[dict_date['fdate']]['fast_bonus'] + bn_wk[dict_date['fdate']]['ws_bonus'],
                    'percent_baht': (bn_wk[dict_date['fdate']]['fast_bonus'] + bn_wk[dict_date['fdate']][
                        'ws_bonus']) * 100 / ((pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']) * 11)
                }
            else:
                for ky in pv_si:
                    result[dict_date['fdate'] + " to " + dict_date['tdate']] = {
                        'sum_total_pv': pv_si[ky]['pv'] + pv_tf[ky]['pv'],
                        'fast_bonus': bn_wk[ky]['fast_bonus'],
                        'percent_fast': bn_wk[ky]['fast_bonus'] * 100 / (pv_si[ky]['pv'] + pv_tf[ky]['pv']),
                        'ws_bonus': bn_wk[ky]['ws_bonus'],
                        'percent_ws': bn_wk[ky]['ws_bonus'] * 100 / (pv_si[ky]['pv'] + pv_tf[ky]['pv']),
                        'sum_bonus': bn_wk[ky]['fast_bonus'] + bn_wk[ky]['ws_bonus'],
                        'percent_baht': (bn_wk[ky]['fast_bonus'] + bn_wk[ky][
                            'ws_bonus']) * 100 / ((pv_si[ky]['pv'] + pv_tf[ky]['pv']) * 11)
                    }
        return result


class MonthRoundReport(object):

    def __init__(self, *args, **kwargs):
        self.start = kwargs.get('start', None)
        self.end = kwargs.get('end', None)
        self.round = self.get_round()

    def get_round(self):
        queryset = MonthRound.objects.filter(fdate__gte=self.start, tdate__lte=self.end)
        round_list = MonthRoundSerializer(queryset, many=True).data
        return round_list

    @property
    def total(self):
        result = {}
        for dict_date in self.round:
            pv_si = PvFromSaleInvoice(start=dict_date['fdate'], end=dict_date['tdate']).total
            pv_tf = PvFromPvTransfer(start=dict_date['fdate'], end=dict_date['tdate']).total
            bn_wk = BonusFromWeekCommission(start=dict_date['fdate'], end=dict_date['tdate']).total
            bn_mh = BonusFromMonthCommission(start=dict_date['fdate'], end=dict_date['tdate']).total
            discnt = DiscountFromSaleInvoice(start=dict_date['fdate'], end=dict_date['tdate']).total
            result[dict_date['fdate'] + " to " + dict_date['tdate']] = {
                'sum_total_pv': pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv'],
                'fast_bonus': bn_wk[dict_date['fdate']]['fast_bonus'],
                'percent_fast': bn_wk[dict_date['fdate']]['fast_bonus'] * 100 / (
                        pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']),
                'ws_bonus': bn_wk[dict_date['fdate']]['ws_bonus'],
                'percent_ws': bn_wk[dict_date['fdate']]['ws_bonus'] * 100 / (
                        pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']),
                'matching': bn_mh[dict_date['fdate']]['dmbonus'],
                'percent_matching': bn_mh[dict_date['fdate']]['dmbonus'] * 100 / (
                        pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']),
                'all_sale': bn_mh[dict_date['fdate']]['embonus'],
                'percent_all_sale': bn_mh[dict_date['fdate']]['embonus'] * 100 / (
                        pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']),
                'sum_bonus': bn_wk[dict_date['fdate']]['fast_bonus'] + bn_wk[dict_date['fdate']]['ws_bonus'] +
                             bn_mh[dict_date['fdate']]['dmbonus'] + bn_mh[dict_date['fdate']]['embonus'],
                'percent_baht': (bn_wk[dict_date['fdate']]['fast_bonus'] + bn_wk[dict_date['fdate']]['ws_bonus'] +
                                 bn_mh[dict_date['fdate']]['dmbonus'] + bn_mh[dict_date['fdate']]['embonus']) * 100 / (
                                        (pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv']) * 11),
                'discount': discnt[dict_date['fdate']]['paid'],
                'percent_discount': discnt[dict_date['fdate']]['paid'] * 100 / (
                        pv_si[dict_date['fdate']]['pv'] + pv_tf[dict_date['fdate']]['pv'])
            }
        return result
