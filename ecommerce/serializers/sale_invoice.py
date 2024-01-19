from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from member.models import Member
from ..models import SaleInvoice, SaleItem


class SaleInvoiceSerializer(serializers.ModelSerializer):
    member_id_card = serializers.SerializerMethodField()

    class Meta:
        model = SaleInvoice
        fields = (
            'sano', 'sadate', 'sctime', 'inv_code', 'mcode', 'name_t', 'total', 'tot_pv',
            'sa_type', 'uid', 'uid_branch', 'lid', 'cancel', 'bill_state', 'order_number',
            'member_id_card', 'remark'
        )

    def get_member_id_card(self, obj):
        try:
            return obj.member.id_card
        except (Member.DoesNotExist, AttributeError):
            return '-'


class SaleItemListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        # if obj exist on db just update it
        try:
            obj = SaleItem.objects.get(
                client_code=validated_data.get('mcode'),
                branch_name=validated_data.get('inv_code'),
                bill_number=validated_data.get('sano'),
                pcode=validated_data.get('pcode')
            )
            return obj
        except ObjectDoesNotExist:
            return SaleItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        itm_mapping = {itm.id: itm for itm in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for itm_id, data in data_mapping.items():
            itm = itm_mapping.get(itm_id, None)
            if itm is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(itm, data))

        # Perform deletions.
        # for itm_id, itm in itm_mapping.items():
        #     if itm_id not in data_mapping:
        #         itm.delete()

        return ret


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = '__all__'
        list_serializer_class = SaleItemListSerializer
