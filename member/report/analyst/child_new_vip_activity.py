from datetime import datetime

from django.db.models import Count, Q

from core.report.summary import PeriodSummaryBase
from member.models import Member
from system_log.models import PositionChangeLog


class NewVipActivityAnalystReport(PeriodSummaryBase):
    """
    a class for present number of persons who distributed in sponsor tree of member.
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        head_mcode (str): member code of start point of sponsor tree
        exclude_mcode (str): member code of start point of sponsor tree that exclude tree from head_mcode's sponsor tree
        include_mcode (str): member code of start point of sponsor tree that include tree from exclude_mcode's sponsor tree
    """
    class Meta:
        model = PositionChangeLog
        date_fields = "date_change"
        filter = {"pos_after__in": ["VIP", "DIS", "PRO"]}

    def __init__(self, *args, **kwargs):
        super(NewVipActivityAnalystReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.head_mcode = kwargs.get("mcode", None)
        self.exclude_mcode = kwargs.get("exclude_mcode", None)
        self.include_mcode = kwargs.get("include_mcode", None)

    def get_extend_queryset(self, queryset):
        """
        a method that overwrite from class PeriodSummaryBase to extend filter query and group data by time period

        :param queryset: queryset is a data set that get from model

        :return: queryset after reform
        """
        if self.head_mcode and not self.exclude_mcode and not self.include_mcode:
            child_list = Member.objects.get(mcode=self.head_mcode).sponsor_child.filter(
                status_terminate=0
            ).values_list("mcode", flat=True)
            queryset = queryset.filter(mcode__in=child_list)
        elif self.head_mcode and self.exclude_mcode and not self.include_mcode:
            ex_obj = Member.objects.get(mcode=self.exclude_mcode)
            child_list = Member.objects.get(mcode=self.head_mcode).sponsor_child.filter(
                Q(status_terminate=0),
                Q(sponsor_lft__lte=ex_obj.sponsor_lft) | Q(sponsor_rgt__gte=ex_obj.sponsor_rgt),
            ).values_list("mcode", flat=True)
            queryset = queryset.filter(mcode__in=child_list)
        elif self.head_mcode and self.exclude_mcode and self.include_mcode:
            ex_obj = Member.objects.get(mcode=self.exclude_mcode)
            in_obj = Member.objects.get(mcode=self.include_mcode)
            child_list = Member.objects.get(mcode=self.head_mcode).sponsor_child.filter(
                Q(status_terminate=0),
                ~Q(sponsor_lft__range=(ex_obj.sponsor_lft, in_obj.sponsor_lft)),
                ~Q(sponsor_rgt__range=(ex_obj.sponsor_rgt, in_obj.sponsor_rgt))
            ).values_list("mcode", flat=True)
            queryset = queryset.filter(mcode__in=child_list)
        return queryset.values('time').annotate(
            count=Count('mcode'),
        ).values('time', 'count').order_by('time')

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have member code is a key and sub-key is time period

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        pool[self.head_mcode] = {}
        month_list = PeriodSummaryBase.month_diff_range(self.end, self.start)
        for mth in month_list:
            pool[self.head_mcode][datetime.strftime(mth, "%b-%Y")] = 0
        for x in queryset:
            pool[self.head_mcode][datetime.strftime(x["time"], "%b-%Y")] = x["count"]
        return pool

