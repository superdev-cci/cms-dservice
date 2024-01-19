from rest_framework import serializers

from trip.functions.travel_point_stack import TravelPointStackOperator
from trip.models import TravelPointStack


class TravelPointStackSerializer(serializers.ModelSerializer):
    member_name = serializers.SerializerMethodField()
    member_code = serializers.SerializerMethodField()
    expired_date = serializers.SerializerMethodField()

    class Meta:
        model = TravelPointStack
        fields = '__all__'

    def get_member_name(self, obj):
        if obj is not None:
            return obj.member.full_name
        return '-'

    def get_member_code(self, obj):
        if obj is not None:
            return obj.member.code
        return '-'

    def get_expired_date(self, obj):
        try:
            next_date = obj.stamp_date.replace(day=15, month=obj.stamp_date.month + 1)
        except Exception as e:
            next_date = obj.stamp_date.replace(year=obj.stamp_date.year + 1, month=1, day=15)
        return next_date
