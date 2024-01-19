from rest_framework import serializers
from ..models import WeakStrongSummary


class WeakStrongSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeakStrongSummary
        fields = '__all__'
