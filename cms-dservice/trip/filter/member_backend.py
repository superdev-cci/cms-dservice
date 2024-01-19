from rest_framework.filters import BaseFilterBackend
from django.db.models import Q


class TravelPointStatementMemberAccessFilter(BaseFilterBackend):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter Member by `mtype` Ex. 0 is Person, 1 is Juristic person(Corporation)
    """

    def filter_queryset(self, request, queryset, view):
        if hasattr(request, 'member'):
            queryset = queryset.filter(member=request.member, state='CM', )
        return queryset


class TravelPointStackMemberAccessFilter(BaseFilterBackend):
    """
    a Filter class for `Backend Filter` use to filter in ViewAPI
    filter Member by `mtype` Ex. 0 is Person, 1 is Juristic person(Corporation)
    """

    def filter_queryset(self, request, queryset, view):
        if hasattr(request, 'member'):
            queryset = queryset.filter(
                Q(remaining_gold_point__gt=0) | Q(remaining_silver_point__gt=0),
                member=request.member)
        return queryset
