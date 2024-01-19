from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from branch.models import Branch, BranchStock
from ecommerce.models import Product

class BranchItemStockListSerializer(serializers.ListSerializer):
        
    def create(self, validated_data):
        #if obj exist on db just update it
        try:
            obj = BranchStock.objects.get(
                branch=Branch.objects.get(inv_code=validated_data.get('inv_code')),
                product=Product.objects.get(pcode=validated_data.get('pcode'))
            )
            obj.qty = validated_data.get('qty')
            obj.save()
            return obj
        except ObjectDoesNotExist:
            return BranchStock.objects.create(**validated_data)

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


class BranchItemStockSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='product.pdesc')
    branch_code = serializers.CharField(source='branch.inv_code')
    id = serializers.IntegerField()

    class Meta:
        model = BranchStock
        fields = ('id', 'pcode', 'description', 'qty', 'branch_code',)
        list_serializer_class = BranchItemStockListSerializer


class BranchItemStockHQSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='pdesc')
    branch_code = serializers.SerializerMethodField('get_branch')

    class Meta:
        model = Product
        fields = ('pcode', 'description', 'qty', 'branch_code',)

    def get_branch(self, obj):
        return 'HQ'
