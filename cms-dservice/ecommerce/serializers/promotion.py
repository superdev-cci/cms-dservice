from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from ecommerce.models import Product
from ..models import Promotion, PromotionItem


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('pcode', 'pdesc', 'price', 'customer_price', 'pv', 'special_pv', 'activated')


class PromotionItemListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        try:
            obj = PromotionItem.objects.get(
                promotion=Promotion.objects.get(pcode=validated_data.get('promotion_code')),
                product=Product.objects.get(pcode=validated_data.get('pcode'))
            )
            return obj
        except ObjectDoesNotExist:
            return PromotionItem.objects.create(**validated_data)

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

        return ret


class PromotionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionItem
        fields = '__all__'
        list_serializer_class = PromotionItemListSerializer

