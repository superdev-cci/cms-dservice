from datetime import datetime

from django.db.models import Sum

from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice
from member.models import Member


class SaleInvoiceActivityAnalystReport(PeriodSummaryBase):
    """
    a class for present summary total of Sale Invoice of member in sponsor tree of member.
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): member code of start point of sponsor tree
    """
    class Meta:
        model = SaleInvoice
        date_fields = "sadate"
        exclude = {"cancel": 1}

    def __init__(self, *args, **kwargs):
        super(SaleInvoiceActivityAnalystReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.mcode = kwargs.get("mcode", None)

    def get_extend_queryset(self, queryset):
        """
        a method that overwrite from class PeriodSummaryBase to extend filter query

        :param queryset: queryset is a data set that get from model

        :return: queryset after reform
        """
        if self.mcode:
            child_list = Member.objects.get(mcode=self.mcode).sponsor_child.filter(
                status_terminate=0
            ).values_list("mcode", flat=True)
            queryset = queryset.filter(mcode__in=child_list)
        return queryset.values('time').annotate(
            sum_total=Sum('total'),
            sum_pv=Sum('tot_pv'),
        ).values('time', 'sum_total', 'sum_pv').order_by('time')

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have member code is a key and sub-key is time period

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        pool[self.mcode] = {}
        month_list = PeriodSummaryBase.month_diff_range(self.end, self.start)
        for mth in month_list:
            pool[self.mcode][datetime.strftime(mth, "%b-%Y")] = {
                'sum_total': 0,
                'sum_pv': 0
            }
        for x in queryset:
            pool[self.mcode][datetime.strftime(x["time"], "%b-%Y")] = {
                'sum_total': x['sum_total'],
                'sum_pv': x['sum_pv']
            }
        return pool

    @property
    def for_dataframe(self):
        """
        a method to process data and reform to dictionary for DataFrame

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        pool[self.mcode] = {}
        month_list = PeriodSummaryBase.month_diff_range(self.end, self.start)
        for mth in month_list:
            pool[self.mcode][datetime.strftime(mth, "%b-%Y")] = 0
        for x in queryset:
            pool[self.mcode][datetime.strftime(x["time"], "%b-%Y")] = float(x['sum_total'])
        return pool

