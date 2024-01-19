from datetime import datetime

from django.db.models import Count

from commission.models import HonorChangeLog
from core.report.summary import PeriodSummaryBase
from member.models import Member


class HonorActivityAnalystReport(PeriodSummaryBase):
    """
    a class for present number of persons who have been promoted honor in sponsor tree of member.
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): member code of start point of sponsor tree
    """
    class Meta:
        model = HonorChangeLog
        date_fields = "date_change"

    def __init__(self, *args, **kwargs):
        super(HonorActivityAnalystReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.mcode = kwargs.get("mcode", None)

    def get_extend_queryset(self, queryset):
        """
        a method that overwrite from class PeriodSummaryBase to extend filter query and group data by time period

        :param queryset: queryset is a data set that get from model

        :return: queryset after reform
        """
        if self.mcode:
            child_list = Member.objects.get(mcode=self.mcode).sponsor_child.filter(
                status_terminate=0
            ).values_list("mcode", flat=True)
            queryset = queryset.filter(mcode__in=child_list)
        return queryset.values('time').annotate(
            count=Count('mcode'),
        ).values('time', 'count', 'pos_after').order_by('time')

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
                'SI': 0, 'GL': 0, 'PE': 0, 'SE': 0, 'EE': 0, 'DE': 0, 'CE': 0
            }
        for x in queryset:
            pool[self.mcode][datetime.strftime(x["time"], "%b-%Y")][x["pos_after"]] = x["count"]
        return pool

    @property
    def for_dataframe(self):
        """
        a method to process data and reform to dictionary for DataFrame

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        if queryset:
            pool[self.mcode] = {}
        else:
            pool[self.mcode] = {}
            for mth in self.month_diff_range(self.end, self.start):
                pool[self.mcode][datetime.strftime(mth, "%b-%Y")] = {}
        for x in queryset:
            if datetime.strftime(x["time"], "%b-%Y") not in pool[self.mcode]:
                pool[self.mcode][datetime.strftime(x["time"], "%b-%Y")] = {
                    x["pos_after"]: x["count"]
                }
            else:
                pool[self.mcode][datetime.strftime(x["time"], "%b-%Y")][x["pos_after"]] = x["count"]
        return pool

