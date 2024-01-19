from rest_framework import serializers
from ..models import WeekRound, MonthRound


class WeekRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekRound
        fields = ('fdate', 'tdate')


class MonthRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthRound
        fields = ('fdate', 'tdate')
