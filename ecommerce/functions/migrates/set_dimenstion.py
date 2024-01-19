from ...models import Product
from ...models import ShippingBox

box_size = [
    {
        "name": '0+4 (small)',
        "description": '0+4 (small)',
        "height": 9.5,
        "length": 10.5,
        "width": 16.5,
        "max_weight": 1,
        "inbound_cost": 45,
        "outbound_cost": 65
    },
    {
        "name": '0+4 (large)',
        "description": '0+4 (large)',
        "height": 11.5,
        "length": 10.5,
        "width": 16.5,
        "max_weight": 1,
        "inbound_cost": 45,
        "outbound_cost": 65
    },
    {
        "name": '2A',
        "description": '2A',
        "height": 11.5,
        "length": 13.5,
        "width": 19.5,
        "max_weight": 5,
        "inbound_cost": 75,
        "outbound_cost": 90
    },
    {
        "name": 'B',
        "description": 'B',
        "height": 25.5,
        "length": 16.5,
        "width": 8.5,
        "max_weight": 5,
        "inbound_cost": 75,
        "outbound_cost": 90
    },
    {
        "name": '2B',
        "description": '2B',
        "height": 25,
        "length": 16.5,
        "width": 18,
        "max_weight": 5,
        "inbound_cost": 75,
        "outbound_cost": 90
    },
    {
        "name": 'E',
        "description": 'E',
        "height": 39.5,
        "length": 23.5,
        "width": 18,
        "max_weight": 10,
        "inbound_cost": 100,
        "outbound_cost": 110
    },
    {
        "name": 'L',
        "description": 'L',
        "height": 999,
        "length": 999,
        "width": 999,
        "max_weight": 999,
        "inbound_cost": 150,
        "outbound_cost": 150
    }
]

product_size = {
    'Tier1': {
        'height': 3,
        'length': 10,
        'width': 13,
    },
    'CCI002': {
        'height': 3.5,
        'length': 5,
        'width': 14.5,
    },
    'Tier2': {
        'length': 11.5,
        'width': 4,
        'height': 15.5,
    },
    'Tier4': {
        'width': 8,
        'length': 12,
        'height': 10.5,
    },
    'CCI001': {
        'width': 7.5,
        'length': 7.3,
        'height': 24,
    }
}


def process_migrate():
    for x in box_size:
        box = ShippingBox.objects.filter(name=x['name'])
        if len(box) == 0:
            ShippingBox.objects.create(**x)

    product = Product.objects.filter(product_class__name="Tier1")
    product.update(height=product_size['Tier1']['height'],
                   length=product_size['Tier1']['length'],
                   width=product_size['Tier1']['width'])

    product = Product.objects.filter(pcode="CCI002")
    product.update(height=product_size['CCI002']['height'],
                   length=product_size['CCI002']['length'],
                   width=product_size['CCI002']['width'])

    product = Product.objects.filter(product_class__name="Tier2")
    product.update(height=product_size['Tier2']['height'],
                   length=product_size['Tier2']['length'],
                   width=product_size['Tier2']['width'])

    product = Product.objects.filter(product_class__name="Tier4")
    product.update(height=product_size['Tier4']['height'],
                   length=product_size['Tier4']['length'],
                   width=product_size['Tier4']['width'])

    product = Product.objects.filter(pcode="CCI001")
    product.update(height=product_size['CCI001']['height'],
                   length=product_size['CCI001']['length'],
                   width=product_size['CCI001']['width'])

    product = Product.objects.filter(pcode__in=['CCI025', 'CCI036'])
    product.update(height=product_size['Tier4']['height'],
                   length=product_size['Tier4']['length'],
                   width=product_size['Tier4']['width'])
