from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from commission.models import PvTransfer


class SummaryPVTransferByMemberReport(PeriodSummaryBase):

    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        # filter = {
        #     'sa_type__in': ('A', 'H', 'L', 'B', 'PM')
        # }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(SummaryPVTransferByMemberReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('mcode', 'name_t') \
            .annotate(sum_pv=Sum('tot_pv')) \
            .order_by('-sum_pv')

    @property
    def total(self):
        return self.get_query_set(self.start, self.end, self.get_type)[0:20]

