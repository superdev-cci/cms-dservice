from rest_framework import serializers
from ..models import MonthCommission


class MonthCommissionSerializer(serializers.ModelSerializer):
    date_issue = serializers.DateField(source='fdate')

    class Meta:
        model = MonthCommission
        fields = ('date_issue', 'mcode', 'member', 'embonus', 'dmbonus', 'total')
