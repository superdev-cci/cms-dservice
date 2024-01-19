from commission.models import WeekRound
from commission.report.summary_pv import PvFromSaleInvoice, PvFromPvTransfer
from ecommerce.report import SaleSummaryReport


class RoundSummarySalesVsPvReportJSON(object):

    def __init__(self, *args, **kwargs):
        self.start = kwargs.get('start', None)
        self.end = kwargs.get('end', None)
        self.round = self.get_round()

    def get_round(self):
        queryset = WeekRound.objects.filter(fdate__gte=self.start, tdate__lte=self.end)
        return queryset

    def get_total_sales(self):
        pool = {}
        for x in self.round:
            report = SaleSummaryReport(start=x.fdate, end=x.tdate, get_type='monthly').total
            pool[x.fdate.__str__()] = next(iter(report.values()))
        return pool

    def get_total_pv(self):
        pool = {}
        for x in self.round:
            pv_si = PvFromSaleInvoice(start=x.fdate, end=x.tdate).total
            pv_tf = PvFromPvTransfer(start=x.fdate, end=x.tdate).total
            pv_1 = next(iter(pv_si.values()))['pv']
            pv_2 = next(iter(pv_tf.values()))['pv']
            pool[x.fdate.__str__()] = pv_1 + pv_2
        return pool

    @property
    def total(self):
        pool = {}
        sales = self.get_total_sales()
        pv = self.get_total_pv()

        for key, value in sales.items():
            pool[key] = {}
            pool[key]['sale'] = int(value)

        for key, value in pv.items():
            if key in pool:
                pool[key]['pv'] = int(value)
            else:
                pool[key] = {
                    'sale' : 0,
                    'pv': value
                }
        return pool
