from rest_framework import serializers
from ..models import MemberDiscount


class MemberDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberDiscount
        fields = '__all__'
