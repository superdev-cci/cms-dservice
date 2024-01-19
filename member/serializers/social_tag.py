from rest_framework import serializers
from ..models import MemberSocialTagConfig


class MemberSocialTagConfigSerializer(serializers.ModelSerializer):
    pixel_id = serializers.CharField(required=False)
    line_tag_id = serializers.CharField(required=False)
    google_tag_id = serializers.CharField(required=False)
    google_analytics_id = serializers.CharField(required=False)

    class Meta:
        model = MemberSocialTagConfig
        fields = '__all__'

