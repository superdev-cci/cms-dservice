from .summary_month_commission import SummaryMonthCommission
from .summary_week_commission import SummaryWeekCommission


class SummaryCommission(object):
    """
    a class represent summary of each member's commission (combine WeekCommission and MonthCommission)

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): (Optional) member code of interested person
        honor (list): (Optional) member honor of interested group's member
    """
    def __init__(self, *args, **kwargs):
        self.week = SummaryWeekCommission(*args, **kwargs)
        self.month = SummaryMonthCommission(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)

    @property
    def total(self):
        """
        a method to process data from `SummaryWeekCommission` and `SummaryMonthCommission`
        combine two dictionary to one dictionary

        :return: (:obj:`dictionary`)
        """
        pool = self.week.total
        # Fill default data for week commission
        for k, v in pool.items():
            for k_time, v_time in v['data'].items():
                v_time['matching'] = 0
                v_time['all_sales'] = 0
        # Fill data for month commission
        for k, v in self.month.total.items():
            for k_time, v_time in v['data'].items():
                bonus_data = pool[v['mcode']]['data']
                try:
                    bonus_data[k_time]['matching'] = float(v_time['matching'])
                    bonus_data[k_time]['all_sales'] = float(v_time['all_sales'])
                    bonus_data[k_time]['total'] += float(v_time['total'])
                except:
                    bonus_data[k_time] = {
                        'matching': float(v_time['matching']),
                        'all_sales': float(v_time['all_sales']),
                        'total': float(v_time['total']),
                        'fast': 0,
                        'ws': 0,
                        'resale': 0,
                    }
        return pool
