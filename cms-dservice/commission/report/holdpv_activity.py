import operator
from collections import OrderedDict
from datetime import date, datetime
from functools import reduce

from django.db.models import Sum
from django.db import models

from core.mixin import MonthMixIn
from core.report.summary import PeriodSummaryBase
from .holdpv_in import PvTransferInReport, SaleInvoiceInReport
from .holdpv_out import PvTransferOutReport
from .holdpv_out_with_out_expired import PvTransferOutWithOutExpiredReport


class PvActivityReport(PeriodSummaryBase):

    def __init__(self, *args, **kwargs):
        super(PvActivityReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.has_member = kwargs.get('mem_code', None)
        self.expired_pv = kwargs.get('expired_pv', True)

    @property
    def result(self):
        pool = {}
        pvin1 = PvTransferInReport(start=self.start, end=self.end, get_type=self.get_type,
                                   mem_code=self.has_member).total
        pvin2 = SaleInvoiceInReport(start=self.start, end=self.end, get_type=self.get_type,
                                    mem_code=self.has_member).total
        if self.expired_pv:
            pvout = PvTransferOutReport(start=self.start, end=self.end, get_type=self.get_type,
                                        mem_code=self.has_member).total
        else:
            pvout = PvTransferOutWithOutExpiredReport(start=self.start, end=self.end, get_type=self.get_type,
                                                      mem_code=self.has_member).total

        keys = list({
            *list(pvin1.keys()),
            *list(pvin2.keys()),
            *list(pvout.keys())})
        try:
            keys = sorted([datetime.strptime(x, '%Y-%b') for x in keys])
            keys = [x.strftime('%Y-%b') for x in keys]
        except ValueError:
            keys = sorted([datetime.strptime(x, '%Y-%m-%d') for x in keys])
            keys = [x.strftime('%Y-%m-%d') for x in keys]
        for key in keys:
            pv = 0 + pvin2.get(key, 0)

            # pvin1.get(key, 0) \
            pool[key] = {
                'in': pv,
                'out': pvout.get(key, 0),
                'transfer': pvin1.get(key, 0)
            }
        return pool
