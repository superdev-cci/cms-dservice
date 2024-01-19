from rest_framework import serializers
from ..models import PvTransfer


class PvTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PvTransfer
        fields = '__all__'
