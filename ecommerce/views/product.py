from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication.legacy import BasicAuthDefault
from core.filters import ProductFilter
from ..serializers import ProductSerializer, CategorySerializer
from ..models import Product, ProductCategory


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (ProductFilter, )
    product_field = 'pcode'

    def list(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def get_active_product(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(Q(pcode__startswith='CCI'))
        queryset = self.filter_queryset(queryset)
        serializers = ProductSerializer(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CategoryView(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    # def list(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

