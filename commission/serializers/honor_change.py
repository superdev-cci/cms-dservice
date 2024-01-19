from rest_framework import serializers
from ..models import HonorChangeLog


class HonorChangeLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = HonorChangeLog
        fields = '__all__'
