from rest_framework import serializers
from branch.models import StockAdjustStatement, StockAdjustItem


class StockAdjustItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.pdesc')

    class Meta:
        model = StockAdjustItem
        fields = '__all__'


class StockAdjustStatementSerializer(serializers.ModelSerializer):
    items = StockAdjustItemSerializer(many=True, source='stockadjustitem_set')

    class Meta:
        model = StockAdjustStatement
        fields = '__all__'
