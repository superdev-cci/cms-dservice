from rest_framework import serializers
from ..models import HoldPvStack
from member.serializers import MemberSerializer
from datetime import date, timedelta


class HoldPvStackSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    expire_date = serializers.SerializerMethodField('get_exp_date')

    class Meta:
        model = HoldPvStack
        fields = ('stamp_date', 'member', 'pv', 'remaining', 'expire_date')

    def get_exp_date(self, obj):
        durationDict = {'MB': 30, 'FR': 60, 'AG': 90}
        exp = obj.stamp_date + timedelta(durationDict[obj.member.member_type])
        return exp.strftime("%Y-%m-%d")
