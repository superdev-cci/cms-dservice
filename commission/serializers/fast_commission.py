from rest_framework import serializers
from ..models import FastCommission
from member.serializers import MemberSerializer


class FastCommissionSerializer(serializers.ModelSerializer):
    round = serializers.CharField(source='rcode')
    date_issue = serializers.DateField(source='fdate')
    member = MemberSerializer()

    class Meta:
        model = FastCommission
        fields = ('round', 'date_issue', 'mcode', 'member', 'bonus', 'name_t', 'total', 'tot_pv')
