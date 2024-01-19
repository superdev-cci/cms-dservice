from django.db.models import Sum, Count
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice
from ecommerce.report.base.sale import SaleInvoiceSummaryBase


class SaleSummaryByWeekDayReportJSON(SaleInvoiceSummaryBase):
    """
        a class represent summary sales by daily
        This class inherit class `PeriodSummaryBase` also you can use a method in SaleInvoiceSummaryBase or overwrite method
        and receive attribute from `PeriodSummaryBase`

        Attributes:
            start (:obj:`date`): a start date of interested data.
            end (:obj:`date`): a end date of interested data.
            get_type (str): time period option [daily, monthly, quarter, yearly]
            return_value (str) : return type [sales, count]
    """

    class Meta(SaleInvoiceSummaryBase.Meta):
        annotate = {
            'field': ('time',),
            'order': ('time',),
            'function': {
                'total_prices': {
                    'fn': Sum,
                    'target': 'total'
                },
                'total_count': {
                    'fn': Count,
                    'target': 'sano'
                },
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', 'daily')
        self.return_value = kwargs.get('return_value', 'sales')
        return

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have weekday is a primary key and sub-key is date string

        :return: (:obj:`dictionary`)
        """

        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        if self.return_value == 'count':
            queryset = queryset.filter(total__gt=10)

        for instance in queryset:
            time_key = instance['time'].strftime('%Y-%b')
            day_key = instance['time'].strftime('%A')

            if day_key not in pool:
                pool[day_key] = {}

            if time_key not in pool[day_key]:
                if self.return_value == 'sales':
                    pool[day_key][time_key] = float(instance['total_prices'])
                else:
                    pool[day_key][time_key] = float(instance['total_count'])
            else:
                if self.return_value == 'sales':
                    pool[day_key][time_key] += float(instance['total_prices'])
                else:
                    pool[day_key][time_key] += float(instance['total_count'])

        return pool
