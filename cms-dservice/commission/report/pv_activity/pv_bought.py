from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class PvHoldInReport(PeriodSummaryBase):
    """
    a class represent member's Hold PV from Sale Invoice
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        group :obj:`list`): (Optional) list of member code that interest
    """
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('H',)
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(PvHoldInReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.member_group = kwargs.get('group', None)

    def get_extend_queryset(self, queryset):
        """
        a method for `group by` queryset

        :param queryset: filtered queryset

        :return: grouped queryset
        """
        return queryset.values('time', 'member__mcode', 'member__honor', 'member__name_t') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('-time', 'member__mcode')

    def filter_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        queryset = super(PvHoldInReport, self).filter_queryset(queryset)
        return queryset.filter(member__mcode__in=self.member_group)

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if x['member__mcode'] not in pool:
                pool[x['member__mcode']] = {
                    'name': x['member__name_t'],
                    'honor': x['member__honor'],
                    'data': {}
                }
            if self.get_type == 'daily':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y-%m-%d')] = float(x['total'])
            elif self.get_type == 'monthly':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'quarter':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'yearly':
                pool[x['member__mcode']]['data'][x['time'].strftime('%Y')] = float(x['total'])
        return pool
