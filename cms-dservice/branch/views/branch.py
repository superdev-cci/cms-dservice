from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ecommerce.models import Product
from ..models import Branch, BranchStock
from ..serializers import BranchSerializer, BranchItemStockSerializer, BranchItemStockHQSerializer


class BranchView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    # @action(detail=False, methods=['GET'])
    # def get_stock(self, request, *args, **kwargs):
    #     data = request.query_params
    #     branch_code = data.get('branch', '')
    #     if branch_code == '':
    #         queryset = Product.objects.filter(activated=True)
    #         hq_serializer = BranchItemStockHQSerializer(queryset, many=True)
    #         queryset = BranchStock.objects.filter(product__activated=True)\
    #             .exclude(branch__inv_code='STHQ') \
    #             .select_related('product', 'branch')
    #         branch_serializer = BranchItemStockSerializer(queryset, many=True)
    #         return Response((*hq_serializer.data, *branch_serializer.data), status.HTTP_200_OK)
    #     elif branch_code.upper() == 'HQ':
    #         queryset = Product.objects.filter(activated=True)
    #         serializer = BranchItemStockHQSerializer(queryset, many=True)
    #     else:
    #         queryset = BranchStock.objects.filter(branch__inv_code=branch_code.upper(),
    #                                               product__activated=True) \
    #             .select_related('product', 'branch')
    #         serializer = BranchItemStockSerializer(queryset, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
