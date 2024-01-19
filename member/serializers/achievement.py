from rest_framework import serializers
from ..models import Achievement, Member
import datetime
from dateutil import relativedelta


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('code', 'full_name', 'level', 'honor', 'mobile', 'line_id')


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"


class OnlineCertAchievementSerializer(serializers.ModelSerializer):
    remaining_days = serializers.SerializerMethodField()
    expired_day = serializers.SerializerMethodField()
    member = MemberSerializer()

    class Meta:
        model = Achievement
        fields = "__all__"

    def get_remaining_days(self, obj):
        expired_day = obj.stamp_date.replace(year=obj.stamp_date.year + 2)
        current_day = datetime.date.today()
        diff = expired_day - current_day
        if diff.days >= 0:
            return diff.days
        else:
            return 0

    def get_expired_day(self, obj):
        expired_day = obj.stamp_date.replace(year=obj.stamp_date.year + 2)
        return expired_day.strftime("%m/%d/%Y")
