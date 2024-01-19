from rest_framework import serializers

from member.models import Member
from ..models import Attendee


class MemberAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('mcode', 'name_t', 'honor', 'level')


class AttendeeSerializer(serializers.ModelSerializer):
    members = MemberAttendeeSerializer(read_only=True, many=True)

    class Meta:
        model = Attendee
        fields = '__all__'
