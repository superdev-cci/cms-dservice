from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class PvHoldInWithSponsorStructureReport(PeriodSummaryBase):
    """
    a class represent Hold PV from Sale Invoice of member in sponsor tree.
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        member (:obj:`Member`): Member instance is a start point of sponsor tree
    """
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('H',)
        }
        exclude = {
            'cancel': 1,
        }

    def __init__(self, *args, **kwargs):
        super(PvHoldInWithSponsorStructureReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.member = kwargs.get('member', None)

    def get_extend_queryset(self, queryset):
        """
        a method for `group by` queryset

        :param queryset: filtered queryset

        :return: grouped queryset
        """
        return queryset.values('time',) \
            .annotate(total=Sum('tot_pv')) \
            .order_by('-time', )

    def filter_queryset(self, queryset):
        """
        a method for filter queryset data with Member's sponsor tree

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        queryset = super(PvHoldInWithSponsorStructureReport, self).filter_queryset(queryset)
        return queryset.filter(member__sponsor_lft__gte=self.member.sponsor_lft,
                               member__sponsor_rgt__lte=self.member.sponsor_rgt)

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if self.get_type == 'daily':
                pool[x['time'].strftime('%Y-%m-%d')] = float(x['total'])
            elif self.get_type == 'monthly':
                pool[x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'quarter':
                pool[x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'yearly':
                pool[x['time'].strftime('%Y')] = float(x['total'])
        return pool
