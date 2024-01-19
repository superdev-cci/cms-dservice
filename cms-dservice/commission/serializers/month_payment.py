from rest_framework import serializers
from ..models import MonthPayment
from member.serializers import MemberSerializer
from member.models import Member


class MonthPaymentSerializer(serializers.ModelSerializer):
    member_info = serializers.SerializerMethodField()

    class Meta:
        model = MonthPayment
        fields = '__all__'

    def get_member_info(self, obj):
        if obj.member:
            return MemberSerializer(obj.member).data
        else:
            return MemberSerializer(Member.objects.get(mcode=obj.mcode)).data
