from rest_framework import serializers
from ..models import WeakStrongCurrentRoundStack
from member.serializers import MemberSerializer


class WeakStrongCurrentRoundStackSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    side = serializers.SerializerMethodField('get_side_of_upa')

    class Meta:
        model = WeakStrongCurrentRoundStack
        fields = ('sano', 'mcode', 'member', 'upa_code', 'side', 'level', 'pv', )

    def get_side_of_upa(self, obj):
        if obj.lr == 1:
            return "Left"
        else:
            return "Right"
