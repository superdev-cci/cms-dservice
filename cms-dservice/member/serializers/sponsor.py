from django.db.models import Sum
from rest_framework import serializers

from commission.models import PvTransfer
from ecommerce.models import SaleInvoice
from ..models import Member


class MemberSponsorSerializer(serializers.ModelSerializer):
    pv_collection = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ('mcode', 'name_t', 'mdate', 'line_pos', 'level', 'honor', 'pv_collection', 'sp_code', 'sp_name',
                  'status', 'upa_code', 'upa_name')

    def get_pv_collection(self, obj):
        temp1 = SaleInvoice.objects.filter(mcode=obj.mcode, cancel=0).aggregate(sum_pv=Sum('tot_pv'))
        temp2 = PvTransfer.objects.filter(mcode=obj.mcode, cancel=0).aggregate(sum_pv=Sum('tot_pv'))
        if temp1['sum_pv'] and temp2['sum_pv']:
            return temp1['sum_pv'] + temp2['sum_pv']
        elif temp1['sum_pv']:
            return temp1['sum_pv']
        else:
            return temp2['sum_pv']

