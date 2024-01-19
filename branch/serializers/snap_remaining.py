from rest_framework import serializers
from branch.models import BranchGoodsSnapRemainingStatement, BranchGoodsSnapRemainingItem


class BranchGoodsSnapRemainingItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.pdesc')

    class Meta:
        model = BranchGoodsSnapRemainingItem
        fields = '__all__'


class BranchGoodsSnapRemainingStatementSerializer(serializers.ModelSerializer):
    items = BranchGoodsSnapRemainingItemSerializer(many=True)

    class Meta:
        model = BranchGoodsSnapRemainingStatement
        fields = '__all__'
