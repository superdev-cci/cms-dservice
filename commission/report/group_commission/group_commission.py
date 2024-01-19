from core.report.summary import PeriodSummaryBase
from commission.models import WeekCommission
from member.models import Member
from django.db.models import Q


class GroupCommission(PeriodSummaryBase):
    """
    a class represent Commission Activity under Reference Member (Downline tree)
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): member code identify start point of Downline tree
    """
    class Meta:
        model = WeekCommission
        date_fields = 'fdate'
        exclude = {'ws_bonus': 0}

    def __init__(self, *args, **kwargs):
        super(GroupCommission, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', 'daily')
        self.ref = kwargs.get('mcode', None)

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        ref_member = Member.objects.get(mcode=self.ref)
        queryset = queryset.filter(
            Q(member__line_rgt__gte=ref_member.line_rgt, member__line_lft__lte=ref_member.line_lft) | Q(
                member__line_rgt__lte=ref_member.line_rgt, member__line_lft__gte=ref_member.line_lft))
        return queryset

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = []
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            pool.append({
                'level': x.member.line_depth,
                'mcode': x.mcode,
                'name': x.name_t,
                'fast_bonus': x.fast_bonus,
                'ws_bonus': x.ws_bonus,
                'total': x.total
            })
        pool.sort(key=lambda i: i['level'])
        return pool
