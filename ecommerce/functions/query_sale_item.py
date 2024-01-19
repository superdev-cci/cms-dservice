import operator
from collections import OrderedDict
from functools import reduce

from django.db.models import Q, Avg, Count, Min, Sum
from django.db.models.functions import TruncMonth
from rest_framework.filters import SearchFilter
from member.models import Member
from ..models import SaleItem


class OrgSaleItems(object):
    class Meta:
        select_fields = ('month', 'pcode', 'pdesc', 'sano_link__member__mcode', 'sano_link__member__name_t')
        filter = {
            'sano_link__sa_type__in': ('A', 'H'),
            'sano_link__cancel': 0
        }
        exclude = {
            "sano_link__bill_state": ('CA', 'OR'),
            'pcode__in': ('SE0011', 'SVC0001', 'D001')
        }
        pass

    def __init__(self, head_mcode, *args, **kwargs):
        self.ref_member = Member.objects.get(mcode=head_mcode)
        self.product = kwargs.get('pcode', None)

    def get_queryset(self, request, *args, **kwargs):
        meta = getattr(self, 'Meta')

        queryset = SaleItem.objects.filter(
            sano_link__member__line_lft__gte=self.ref_member.line_lft,
            sano_link__member__line_rgt__lte=self.ref_member.line_rgt
        )

        # Filter from meta
        queries = []
        for k, v in meta.filter.items():
            queries.append(Q(**{k: v}))
        queryset = queryset.filter(reduce(operator.and_, queries))

        # Exclude from meta
        if hasattr(meta, 'exclude'):
            queries = []
            for k, v in meta.exclude.items():
                queries.append(~Q(**{k: v}))
            queryset = queryset.filter(reduce(operator.and_, queries))
        queryset = self.get_extend_queryset(queryset, request, *args, **kwargs)

        question = request.query_params.get('q', '')
        if question != '':
            queryset = queryset.filter(
                Q(sano_link__member__name_t__icontains=question) |
                Q(sano_link__member__mcode__icontains=question) |
                Q(sano_link__sano__icontains=question) |
                Q(pdesc__icontains=question) |
                Q(sano_link__member__mobile__icontains=question)
            )

        queryset = queryset.annotate(month=TruncMonth('sano_link__sadate'))
        select_fields = list(meta.select_fields)
        if 'time_range' in kwargs:
            select_fields.append('month')
        queryset = queryset.values(*select_fields)

        return queryset.annotate(
            total_buy=Sum('amt'),
            total_qty=Sum('qty')) \
            .order_by('month', 'pcode', 'sano_link__member__name_t')

    def get_extend_queryset(self, queryset, request, *args, **kwargs):
        builder = {}
        query_params = request.query_params
        if query_params.get('pcode'):
            builder['pcode'] = query_params.get('pcode')
        if query_params.get('mcode'):
            builder['sano_link__member__mcode'] = query_params.get('mcode')
        if kwargs.get('time_range'):
            builder['sano_link__sadate__range'] = kwargs.get('time_range')

        queries = []
        for k, v in builder.items():
            queries.append(Q(**{k: v}))
        new_queryset = queryset.filter(reduce(operator.and_, queries))

        return new_queryset

    def serialized(self, queryset):
        return [OrderedDict([
            ('pcode', x['pcode']),
            ('description', x['pdesc']),
            ('member_code', x['sano_link__member__mcode']),
            ('name', x['sano_link__member__name_t']),
            ('total', x['total_buy']),
            ('qty', int(x['total_qty']))]
        ) for x in queryset]
