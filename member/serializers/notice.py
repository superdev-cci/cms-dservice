from rest_framework import serializers
from ..models import NoticeInformation


class NoticeInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeInformation
        fields = '__all__'

