from rest_framework.filters import BaseFilterBackend
from django.db.models import Q
from django.db import models


class PaidStateBackendFilter(BaseFilterBackend):
    select = 'paid_state'
    filed = 'paid_state'

    def filter_queryset(self, request, queryset, view):
        q_select = request.query_params.get(self.select, None)
        if q_select:
            select__in = q_select
            if select__in:
                queryset = queryset.filter(Q(**{self.filed: select__in}))
        return queryset


# class SendBackendFilter(PaidStateBackendFilter):
#     select = 'send_status'
#     filed = 'send'
