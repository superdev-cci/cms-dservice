from rest_framework import serializers
from branch.models import BranchTransferHq, BranchTransferHqItem


class BranchTransferHqItemSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField(source='product.pdesc')

    class Meta:
        model = BranchTransferHqItem
        fields = '__all__'


class BranchTransferHqSerializer(serializers.ModelSerializer):
    # items = StockAdjustItemSerializer(many=True, source='stockadjustitem_set')

    class Meta:
        model = BranchTransferHq
        fields = '__all__'
