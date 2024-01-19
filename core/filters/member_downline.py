from functools import reduce
import operator

from django.db.models import Q
from rest_framework.filters import SearchFilter, BaseFilterBackend
from django.utils import six
from django.db.models.constants import LOOKUP_SEP


class MemberDownLineSelectFilter(BaseFilterBackend):
    def get_member_filed(self, view):
        search_fields = getattr(view, 'member_field', None)
        return search_fields

    def get_member_model(self, view):
        model = getattr(view, 'member_model', None)
        return model

    def filter_queryset(self, request, queryset, view):
        up_line_code = request.query_params.get('ref', None)
        down_line_code = request.query_params.get('code', None)

        if up_line_code is None:
            return queryset.none()

        member_model = self.get_member_model(view)

        try:
            up_line = member_model.objects.get(mcode=up_line_code)
            down_line = member_model.objects.get(mcode=down_line_code)
            if up_line.is_child(down_line) or up_line.id == down_line.id:
                member_field = self.get_member_filed(view)
                return queryset.filter(Q(**{member_field: down_line}))
            else:
                return queryset.none()
        except:
            return queryset.none()


class MemberDownLineFilter(MemberDownLineSelectFilter):

    def filter_queryset(self, request, queryset, view):
        up_line_code = request.query_params.get('ref', None)

        if up_line_code is None:
            return queryset.none()

        member_model = self.get_member_model(view)

        try:
            up_line = member_model.objects.get(mcode=up_line_code)
            member_field = self.get_member_filed(view)
            return queryset.filter(
                Q(**{'{}__line_lft__gte'.format(member_field): up_line.line_lft}) &
                Q(**{'{}__line_rgt__lte'.format(member_field): up_line.line_rgt})
            )
        except:
            return queryset.none()
