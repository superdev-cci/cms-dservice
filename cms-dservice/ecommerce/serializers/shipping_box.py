from rest_framework import serializers
from ..models import ShippingBox


class ShippingBoxSerializer(serializers.ModelSerializer):
    volume = serializers.FloatField()

    class Meta:
        model = ShippingBox
        fields = '__all__'

