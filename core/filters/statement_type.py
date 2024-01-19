from functools import reduce
import operator
from rest_framework.filters import SearchFilter, BaseFilterBackend
from django.utils import six
from django.db.models.constants import LOOKUP_SEP
from django.db import models


class StatementGroup(BaseFilterBackend):
    select_groups = []
    query_key = ''

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        cat = request.query_params.get('groups', None)

        if cat == '':
            return None

        return cat

    def construct_search(self, field_name):
        return LOOKUP_SEP.join([field_name, 'in'])

    def filter_queryset(self, request, queryset, view):
        groups = self.get_search_terms(request)

        if not groups:
            return queryset

        if groups == self.query_key:
            orm_lookups = [self.construct_search(six.text_type('code')), ]

            conditions = []

            queries = [models.Q(**{orm_lookup: self.select_groups}) for orm_lookup in orm_lookups]
            conditions.append(reduce(operator.or_, queries))

            queryset = queryset.filter(reduce(operator.and_, conditions))

        return queryset


class StatementPvTransferGroup(StatementGroup):
    select_groups = ['PV', 'HPV', 'RMD', 'RMV']
    query_key = 'pvtransfer'

    def filter_queryset(self, request, queryset, view):
        queryset = super(StatementPvTransferGroup, self).filter_queryset(request, queryset, view)

        user_group = getattr(request, 'user_group', None)

        if user_group.name in ['Member', 'Customer']:
            queryset = queryset.exclude(code='HPV')

        return queryset


class StatementSaleOrderGroup(StatementGroup):
    select_groups = ['NL', 'HL', 'RD', ]
    query_key = 'saleorder'

