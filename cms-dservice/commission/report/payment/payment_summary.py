from commission.report.payment import WeekPaymentReport, MonthPaymentReport
from core.mixin import MonthMixIn


class PaymentReport(MonthMixIn):
    """
    a class represent member's commission payment
    This class inherit class `MonthMixIn` also you can use a method in MonthMixIn or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): (Optional) member code of interested person
    """
    def __init__(self, *args, **kwargs):
        self.get_type = kwargs.get('get_type', 'monthly')
        self.week = WeekPaymentReport(sum=True, **kwargs)
        self.month = MonthPaymentReport(sum=True, **kwargs)

    @property
    def start(self):
        """
        a method return a start date of interested data.
        """
        return self.week.start

    @property
    def end(self):
        """
        a method return a end date of interested data.
        """
        return self.week.end

    @property
    def total(self):
        """
        a method to process data from `WeekPaymentReport` and `MonthPaymentReport`
        combine two dictionary to one dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        for k, v in self.week.summary.items():
            pool[k] = {
                'mcode': v['mcode'],
                'name': v['name'],
                'data': {
                    'week': v['data'],
                    'month': {}
                }
            }

        for k, v in self.month.summary.items():
            if k in pool:
                pool[k]['data']['month'] = v['data']
            else:
                pool[k] = {
                    'mcode': v['mcode'],
                    'name': v['name'],
                    'data': {
                        'week': {},
                        'month': v['data']
                    }
                }

        return pool
