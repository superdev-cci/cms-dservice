from rest_framework.filters import BaseFilterBackend
from django.db import models
from django.db.models import Q

class MemberGroupFilter(BaseFilterBackend):
    def get_group_filed(self, view):
        search_fields = getattr(view, 'group_field', None)
        return search_fields

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_group_filed(view)
        if view.action in ('list',):
            mgroup = request.query_params.get('mem_group', None)
            if mgroup is not None:
                q = {
                    '{}__code'.format(search_fields): mgroup
                }
                queryset = queryset.filter(models.Q(**q))
        return queryset


# class MemberNameFilter(BaseFilterBackend):
#     def get_name_filed(self, view):
#         search_fields = getattr(view, 'name_field', None)
#         return search_fields

#     def filter_queryset(self, request, queryset, view):
#         search_fields = self.get_name_filed(view)
#         if view.action in ('list',):
#             namet = request.query_params.get('name', None)
#             q = {
#                 '{}'.format(search_fields): namet
#             }
#             queryset = queryset.filter(models.Q(**q))
#         return queryset

class MemberLevelFilter(BaseFilterBackend):
    select = 'level'
    filed = 'level__in'

    def filter_queryset(self, request, queryset, view):
        q_select = request.query_params.get(self.select)

        if q_select:
            select__in = q_select.split(',')
            if select__in:
                queryset = queryset.filter(Q(**{self.filed: select__in}))

        return queryset


class MemberHonorFilter(MemberLevelFilter):
    select = 'honor'
    filed = 'honor__in'