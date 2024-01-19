import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce
from django.db.models import Sum
from core.filters import MemberDownLineSelectFilter
from core.report.summary import PeriodSummaryBase
from commission.models import WeakStrongSummary
from commission.functions.honor import HonorQualify


class WeakStrongBalanceJsonReport(PeriodSummaryBase):
    class Meta:
        model = WeakStrongSummary
        date_fields = 'date_issue'

    def __init__(self, *args, **kwargs):
        super(WeakStrongBalanceJsonReport, self).__init__(*args, **kwargs)
        self.group = kwargs.get('member_group', None)
        self.members = kwargs.get('members', None)

    def get_extend_queryset(self, queryset):
        return queryset.values('time', 'member__mcode', 'member__name_t', 'member__honor') \
            .annotate(total_balance=Sum('balance')) \
            .order_by('time', '-member__mcode').order_by('-total_balance')

    def filter_queryset(self, queryset):
        queryset = super(WeakStrongBalanceJsonReport, self).filter_queryset(queryset)
        if 'view' in self.context and 'request' in self.context:
            view = self.context.get('view')
            request = self.context.get('request')
            return MemberDownLineSelectFilter().filter_queryset(request, queryset, view)

        if self.group is not None:
            queryset = queryset.filter(member__honor=self.group)

        if self.members is not None:
            queryset = queryset.filter(member__mcode__in=self.members)

        return queryset

    @property
    def total(self):
        pool = {}
        queryset = self.get_query_set(self.start, self.end, 'monthly')
        for x in queryset.filter(total_balance__gt=0):
            member_code = x['member__mcode']
            if member_code not in pool:
                pool[member_code] = {
                    'name': x['member__name_t'],
                    'honor': x['member__honor'],
                }
            balance = float(x['total_balance'])
            pool[member_code][x['time'].strftime('%Y-%b')] = {
                'balance': balance,
                'qualify': HonorQualify.check_qualify(balance)
            }

        return pool

