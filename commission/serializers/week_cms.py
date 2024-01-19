from rest_framework import serializers
from ..models import WeekCommission


class WeekCommissionSerializer(serializers.ModelSerializer):
    round = serializers.CharField(source='rcode')
    date_issue = serializers.DateField(source='fdate')

    class Meta:
        model = WeekCommission
        fields = ('round', 'date_issue', 'mcode', 'member', 'fast_bonus', 'ws_bonus', 'resale')
