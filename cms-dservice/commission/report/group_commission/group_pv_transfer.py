from core.report.summary import PeriodSummaryBase
from commission.models import PvTransfer
from member.models import Member


class GroupPvTransfer(PeriodSummaryBase):
    """
    a class represent PvTransfer Activity under Reference Member (Downline tree)
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): member code identify start point of Downline tree
    """
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {'sa_type__in': ('A',)}
        exclude = {'cancel': 1}

    def __init__(self, *args, **kwargs):
        super(GroupPvTransfer, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', 'daily')
        self.ref = kwargs.get('mcode', None)

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        ref_member = Member.objects.get(mcode=self.ref)
        queryset = queryset.filter(member__line_rgt__lte=ref_member.line_rgt, member__line_lft__gte=ref_member.line_lft)
        return queryset

    @property
    def total(self):
        """
        a method to process data and reform to list

        :return: (:obj:`list`)
        """
        pool = []
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            actor = Member.objects.get(mcode=x.uid)
            pool.append({
                'level_actor': actor.line_depth,
                'actor_mcode': x.uid,
                'actor_name': actor.name_t,
                'sponsor_mcode': actor.sp_code,
                'sponsor_name': actor.sp_name,
                'receive_mcode': x.mcode,
                'receive_name': x.name_t,
                'total_pv': x.tot_pv,
                'remark': x.remark
            })
        pool.sort(key=lambda i: i['level_actor'])
        return pool
