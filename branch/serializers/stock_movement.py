from rest_framework import serializers
from branch.models import StockStatement


class StockMovementSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField()

    class Meta:
        model = StockStatement
        fields = '__all__'
