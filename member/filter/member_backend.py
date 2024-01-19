from rest_framework.filters import BaseFilterBackend
from django.db.models import Q


class MemberBusinessTypeFilter(BaseFilterBackend):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter Member by `mtype` Ex. 0 is Person, 1 is Juristic person(Corporation)
    """
    select = 'business_type'
    filed = 'mtype'

    def filter_queryset(self, request, queryset, view):
        q_select = request.query_params.get(self.select, None)
        if q_select:
            select__in = q_select
            if select__in:
                queryset = queryset.filter(Q(**{self.filed: select__in}))
        return queryset


class TerminateBackendFilter(MemberBusinessTypeFilter):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter Member by `status_terminate` Ex. 0 is normal, 1 is terminated
    """
    select = 'terminate'
    filed = 'status_terminate'


class SuspendBackendFilter(MemberBusinessTypeFilter):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter Member by `status_suspend` EX. 0 is normal, 1 is suspend
    """
    select = 'suspend'
    filed = 'status_suspend'
