from rest_framework import serializers
from ..models import MonthQualified


class SaleMaintainSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthQualified
        fields = '__all__'
