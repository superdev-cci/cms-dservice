from rest_framework.filters import BaseFilterBackend
from django.db import models
from core.group_auth import staff_group


class ProductFilter(BaseFilterBackend):
    def get_product_filed(self, view):
        search_fields = getattr(view, 'product_field', None)
        return search_fields

    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_product_filed(view)
        pd = request.query_params.get('product', None)
        if pd:
            pds = list(map(lambda x: x, pd.split(',')))
            q = {'{}__in'.format(search_fields): pds}

            queryset = queryset.filter(models.Q(**q))
        return queryset

