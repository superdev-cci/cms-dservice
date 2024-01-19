from rest_framework import serializers

from trip.functions.travel_point_stack import TravelPointStackOperator
from trip.models import TravelPointUseStatement, TravelPointStack


class TravelPointUseStatementSerializer(serializers.ModelSerializer):
    member_name = serializers.SerializerMethodField()
    member_code = serializers.SerializerMethodField()
    trip = serializers.CharField(source='trip.name')

    class Meta:
        model = TravelPointUseStatement
        fields = '__all__'
        extra_kwargs = {
            'bill_number': {'required': False},
        }

    def validate(self, attrs):
        gold_coin = TravelPointStack.get_gold_coin(attrs['member'])
        silver_coin = TravelPointStack.get_silver_coin(attrs['member'])

        if attrs['gold_coin'] > gold_coin:
            raise serializers.ValidationError("Gold coin insufficient")

        if attrs['silver_coin'] > silver_coin:
            raise serializers.ValidationError("Silver coin insufficient")
        return attrs

    def create(self, validated_data):
        stack = TravelPointStackOperator(member=validated_data['member'])
        if validated_data['gold_coin'] > 0:
            stack.pop_gold_stack(validated_data['gold_coin'])
        if validated_data['silver_coin'] > 0:
            stack.pop_silver_stack(validated_data['silver_coin'])
        validated_data['bill_number'] = TravelPointUseStatement.generate_bill_number()
        instance = super().create(validated_data)
        return instance

    def get_member_name(self, obj):
        if obj is not None:
            return obj.member.full_name
        return '-'

    def get_member_code(self, obj):
        if obj is not None:
            return obj.member.code
        return '-'


class TravelPointUseStatementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPointUseStatement
        fields = '__all__'
        extra_kwargs = {
            'bill_number': {'required': False},
        }

    def validate(self, attrs):
        gold_coin = TravelPointStack.get_gold_coin(attrs['member'])
        silver_coin = TravelPointStack.get_silver_coin(attrs['member'])

        if attrs['gold_coin'] > gold_coin:
            raise serializers.ValidationError("Gold coin insufficient")

        if attrs['silver_coin'] > silver_coin:
            raise serializers.ValidationError("Silver coin insufficient")
        return attrs

    def create(self, validated_data):
        stack = TravelPointStackOperator(member=validated_data['member'])
        if validated_data['gold_coin'] > 0:
            stack.pop_gold_stack(validated_data['gold_coin'])
        if validated_data['silver_coin'] > 0:
            stack.pop_silver_stack(validated_data['silver_coin'])
        validated_data['bill_number'] = TravelPointUseStatement.generate_bill_number()
        instance = super().create(validated_data)
        return instance

    def get_member_name(self, obj):
        if obj is not None:
            return obj.member.full_name
        return '-'

    def get_member_code(self, obj):
        if obj is not None:
            return obj.member.code
        return '-'
