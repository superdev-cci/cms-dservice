from rest_framework import serializers
from trip.models import TripApplication


class TripApplicationSerializer(serializers.ModelSerializer):

    trip = serializers.StringRelatedField()
    trip_name = serializers.CharField(source='trip.name')
    member = serializers.StringRelatedField()
    member_name = serializers.CharField(source='member.full_name')

    class Meta:
        model = TripApplication
        fields = '__all__'
