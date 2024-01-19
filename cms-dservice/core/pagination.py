import copy

from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response
# from cci.group_auth import GroupAuthentication
from core.language import LanguageHeader


class AdaptivePagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_size = 20
    max_page_size = 50


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'


class TableResultsPagination(PageNumberPagination,
                             # GroupAuthentication,
                             LanguageHeader):
    page_size = 20
    page_size_query_param = 'page_size'
    lang_dict = {}

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('meta', self.get_meta()),
            ('results', data),
        ]))

    def get_meta(self):
        assert hasattr(self, 'Meta'), 'Meta must be defined'
        meta = {
            'action': copy.deepcopy(self.Meta.action),
            'fields': copy.deepcopy(self.Meta.fields),
            'filter': getattr(self.Meta, 'filter', None)
        }

        # Format field name
        self.format_field_language(meta['fields'], self.lang_dict, self.get_lang())

        return meta

    def format_field_language(self, pool, lang_dict, selector):
        for k, v in lang_dict.items():
            instance = pool.get(k, None)

            if instance:
                field_name = v.get(selector, None)
                if field_name:
                    instance['name'] = field_name

        return
