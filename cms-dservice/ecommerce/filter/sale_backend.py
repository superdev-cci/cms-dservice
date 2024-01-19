from rest_framework.filters import BaseFilterBackend
from django.db.models import Q
from django.db import models


class BillTypeBackendFilter(BaseFilterBackend):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter statement (SaleInvoice, PvTransfer) by `sa_type`
    """
    select = 'bill_type'
    filed = 'sa_type'

    def filter_queryset(self, request, queryset, view):
        q_select = request.query_params.get(self.select, None)
        if q_select:
            select__in = q_select
            if select__in:
                queryset = queryset.filter(Q(**{self.filed: select__in}))
        return queryset


class BillStateBackendFilter(BillTypeBackendFilter):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter statement (SaleInvoice, PvTransfer) by `bill_state`
    """
    select = 'bill_state'
    filed = 'bill_state'


class SendBackendFilter(BillTypeBackendFilter):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter statement (SaleInvoice, PvTransfer) by `send` status
    """
    select = 'send_status'
    filed = 'send'


class BillGroupBackendFilter(BaseFilterBackend):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter statement (SaleInvoice, PvTransfer) by `bill_group`
    """
    def get_group_filed(self, view):
        search_fields = getattr(view, 'group_field', None)
        return search_fields

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_group_filed(view)
        if view.action in ('list',):
            bgroup = request.query_params.get('bill_group', None)
            if bgroup is not None:
                q = {
                    '{}'.format(search_fields): bgroup
                }
                queryset = queryset.filter(models.Q(**q))
        return queryset