from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from accounting.models import StatementType
from ecommerce.models import Product
from ..models import BranchGoodsImportStatement, \
    BranchGoodsImportItem, \
    BranchGoodsExportStatement, \
    BranchGoodsExportItem


class BranchGoodsImportItemListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        # if obj exist on db just update it
        try:
            obj = BranchGoodsImportItem.objects.get(
                statement=validated_data.get('statement'),
                product=validated_data.get('product'),
            )
            obj.price = validated_data.get('price')
            obj.qty = validated_data.get('qty')
            obj.save()
            return obj
        except ObjectDoesNotExist:
            return BranchGoodsImportItem.objects.create(**validated_data)

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
        for itm_id, itm in itm_mapping.items():
            if itm_id not in data_mapping:
                itm.delete()

        return ret


class BranchGoodsImportItemSerializer(serializers.ModelSerializer):
    # statement = serializers.CharField(source='statement.bill_number')

    class Meta:
        model = BranchGoodsImportItem
        fields = '__all__'
        list_serializer_class = BranchGoodsImportItemListSerializer

    def create(self, validated_data):
        return BranchGoodsImportItem(**validated_data)

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.price = validated_data.get('qty', instance.qty)
        return instance


class BranchGoodsImportStatementSerializer(serializers.ModelSerializer):
    # branch_code = serializers.CharField(source='branch.inv_code')
    items = BranchGoodsImportItemSerializer(many=True, required=False)

    class Meta:
        model = BranchGoodsImportStatement
        fields = '__all__'
        extra_kwargs = {
            'bill_number': {'required': False},
            'statement_type': {'required': False}
        }

    def create(self, validated_data):
        validated_data['bill_number'] = BranchGoodsImportStatement.generate_bill_number(validated_data['branch'])
        validated_data['statement_type'] = StatementType.objects.get(name='BranchImportStatement')
        items = validated_data.pop('items')
        statement_obj = BranchGoodsImportStatement.objects.create(**validated_data)
        for x in items:
            statement_obj.items.create(**x)
        return statement_obj

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if hasattr(self, 'context'):
            if 'view' in self.context:
                if self.context['view'].action == 'list':
                    data['branch'] = instance.branch.code
                    data['statement_state'] = instance.statement_state.name
                    data['statement_type'] = instance.statement_type.name
        return data


class BranchGoodsExportItemListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        # if obj exist on db just update it
        try:
            obj = BranchGoodsExportItem.objects.get(
                statement=validated_data.get('statement'),
                product=validated_data.get('product'),
            )
            obj.price = validated_data.get('price')
            obj.qty = validated_data.get('qty')
            obj.save()
            return obj
        except ObjectDoesNotExist:
            return BranchGoodsExportItem.objects.create(**validated_data)

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
        for itm_id, itm in itm_mapping.items():
            if itm_id not in data_mapping:
                itm.delete()

        return ret


class BranchGoodsExportItemSerializer(serializers.ModelSerializer):
    # statement = serializers.CharField(source='statement.bill_number')

    class Meta:
        model = BranchGoodsExportItem
        fields = '__all__'
        list_serializer_class = BranchGoodsExportItemListSerializer

    def create(self, validated_data):
        return BranchGoodsExportItem(**validated_data)

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.price = validated_data.get('qty', instance.qty)
        return instance


class BranchGoodsExportStatementSerializer(serializers.ModelSerializer):
    items = BranchGoodsExportItemSerializer(many=True, required=False)

    class Meta:
        model = BranchGoodsExportStatement
        fields = '__all__'
        extra_kwargs = {
            'bill_number': {'required': False},
            'statement_type': {'required': False}
        }

    def create(self, validated_data):
        validated_data['bill_number'] = BranchGoodsExportStatement.generate_bill_number(validated_data['branch'])
        validated_data['statement_type'] = StatementType.objects.get(name='BranchExportStatement')
        items = validated_data.pop('items')
        statement_obj = BranchGoodsExportStatement.objects.create(**validated_data)
        for x in items:
            statement_obj.items.create(**x)
        return statement_obj

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if hasattr(self, 'context'):
            if 'view' in self.context:
                if self.context['view'].action == 'list':
                    data['branch'] = instance.branch.code
                    data['statement_state'] = instance.statement_state.name
                    data['statement_type'] = instance.statement_type.name
                    data['to_branch'] = instance.to_branch.name

        return data
