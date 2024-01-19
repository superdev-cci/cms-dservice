from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from commission.models import PvTransfer
from member.models import Member


class PvTransferOutReport(PeriodSummaryBase):
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {
            'sa_type__in': ('Y', 'A')
        }
        exclude = {
            'cancel': 1
        }

    def __init__(self, *args, **kwargs):
        super(PvTransferOutReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.member_group = kwargs.get('group', None)
        self.members = {x.code: x for x in Member.objects.filter(mcode__in=self.member_group)}

    def get_extend_queryset(self, queryset):
        return queryset.values('time', 'uid') \
            .annotate(total=Sum('tot_pv')) \
            .order_by('-time', 'uid')

    def filter_queryset(self, queryset):
        queryset = super(PvTransferOutReport, self).filter_queryset(queryset)
        return queryset.filter(uid__in=self.member_group)

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            if x['uid'] not in pool:
                pool[x['uid']] = {
                    'name': self.members[x['uid']].full_name,
                    'honor': self.members[x['uid']].honor,
                    'data': {}
                }
            if self.get_type == 'daily':
                pool[x['uid']]['data'][x['time'].strftime('%Y-%m-%d')] = float(x['total'])
            elif self.get_type == 'monthly':
                pool[x['uid']]['data'][x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'quarter':
                pool[x['uid']]['data'][x['time'].strftime('%Y-%b')] = float(x['total'])
            elif self.get_type == 'yearly':
                pool[x['uid']]['data'][x['time'].strftime('%Y')] = float(x['total'])
        return pool
