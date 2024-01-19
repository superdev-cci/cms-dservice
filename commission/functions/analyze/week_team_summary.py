import operator
from collections import OrderedDict
from functools import reduce

from django.db.models import Q, Avg, Count, Min, Sum
from django.db.models.functions import TruncMonth, TruncYear
from rest_framework.filters import SearchFilter
from member.models import Member
from commission.models import WeekCommission


class WeakTeamSummary(object):
    class Meta:
        select_fields = ('time', 'mcode', 'name_t',)
        pass

    def __init__(self, head_mcode, *args, **kwargs):
        self.ref_member = Member.objects.get(mcode=head_mcode)
        self.get_type = kwargs.get('get_type', None)

    def get_queryset(self, request, *args, **kwargs):
        meta = getattr(self, 'Meta')

        queryset = WeekCommission.objects.filter(
            member__line_lft__gte=self.ref_member.line_lft,
            member__line_rgt__lte=self.ref_member.line_rgt,
            fdate__range=(kwargs.get('time_range'))
        )

        question = request.query_params.get('q', '')
        if question != '':
            queryset = queryset.filter(
                Q(member__name_t__icontains=question) |
                Q(member__mcode__icontains=question)
            )
        if kwargs.get('get_type') == 'monthly':
            queryset = queryset.annotate(time=TruncMonth('fdate'))
        elif kwargs.get('get_type') == 'yearly':
            queryset = queryset.annotate(time=TruncYear('fdate'))

        if kwargs.get('get_type') == 'round':
            return queryset.filter(ws_bonus__gt=0)

        select_fields = list(meta.select_fields)
        # queryset = queryset.values(*select_fields)
        queryset = queryset.values(*select_fields).annotate(
            total_ws=Sum('ws_bonus'))
        return queryset.filter(total_ws__gt=0)

    def serialized(self, queryset):
        try:
            if 'total_ws' in queryset[0]:
                return [OrderedDict(
                    [
                        ('date_issue', x['time']),
                        ('member_code', x['mcode']),
                        ('name', x['name_t']),
                        ('total', x['total_ws'])
                    ]
                ) for x in queryset]
        except Exception as e:
            return [OrderedDict(
                    [
                        ('date_issue', x.fdate),
                        ('member_code', x.mcode),
                        ('name', x.name_t),
                        ('total', x.ws_bonus)
                    ]
                ) for x in queryset]
