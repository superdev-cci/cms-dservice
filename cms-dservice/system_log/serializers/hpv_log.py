from rest_framework import serializers
from ..models import LogHpv


class LogHpvSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogHpv
        fields = '__all__'
