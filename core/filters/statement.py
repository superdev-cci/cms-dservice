from functools import reduce
import operator
from rest_framework.filters import SearchFilter, BaseFilterBackend
from django.utils import six
from django.db.models.constants import LOOKUP_SEP
from django.db import models


class StatementDateTime(BaseFilterBackend):
    search_param = ('start', 'end')

    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        return start, end

    def construct_search(self, field_name):
        return LOOKUP_SEP.join([field_name, 'range'])

    def filter_queryset(self, request, queryset, view):
        search_fields = getattr(view, 'date_range_fields', None)
        start, end = self.get_search_terms(request)

        if not search_fields or not start or not end:
            return queryset

        start = start[:10]
        end = end[:10]

        orm_lookups = [
            self.construct_search(six.text_type(search_field))
            for search_field in search_fields
        ]

        base = queryset
        conditions = []

        queries = [
            models.Q(**{orm_lookup: (start, end)})
            for orm_lookup in orm_lookups
        ]
        conditions.append(reduce(operator.or_, queries))

        queryset = queryset.filter(reduce(operator.and_, conditions))

        return queryset
