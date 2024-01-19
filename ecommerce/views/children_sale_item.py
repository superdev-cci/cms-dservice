from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ecommerce.functions import OrgSaleItems
from ..models import SaleItem
from ..serializers import SaleItemSerializer
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ChildrenSaleItemView(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer

    def list(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def get_children_sale_item(self, request, *args, **kwargs):
        data = request.query_params
        head_mcode = data.get('hmcode', None)
        if head_mcode:
            child_mcode = data.get('cmcode', None)
            start = data.get('start', None)
            end = data.get('end', None)
            if start and end:
                time_range = (start, end)
            elif not start and end:  # request only 'end'
                if datetime.now() < datetime.strptime(end, '%Y-%m-%d'):
                    end = datetime.now().strftime('%Y-%m-%d')
                    start = (datetime.now() - relativedelta(months=1)).strftime('%Y-%m-%d')
                else:
                    start = (datetime.strptime(end, '%Y-%m-%d') - relativedelta(months=1)).strftime('%Y-%m-%d')
                time_range = (start, end)
            elif not end and start:  # request only 'start'
                if datetime.now() < datetime.strptime(start, '%Y-%m-%d'):
                    end = datetime.now().strftime('%Y-%m-%d')
                    start = (datetime.now() - relativedelta(months=1)).strftime('%Y-%m-%d')
                else:
                    end = (datetime.strptime(start, '%Y-%m-%d') + relativedelta(months=1))  # .strftime('%Y-%m-%d')
                    end = datetime.now().strftime('%Y-%m-%d') if datetime.now() < end else end
                time_range = (start, end)
            else:
                time_range = None
            builder = OrgSaleItems(head_mcode)
            queryset = builder.get_queryset(request, **{
                'time_range': time_range,
                'child_mcode': child_mcode,
                'pcode': data.get('pcode', None)
            })
            page = self.paginate_queryset(queryset)
            if page is not None:
                return self.get_paginated_response(builder.serialized(page))

            return Response(queryset, status.HTTP_200_OK)
        else:
            result = {"message": "wrong request pls identify \"hmcode\""}
        return Response(result, status.HTTP_200_OK)
