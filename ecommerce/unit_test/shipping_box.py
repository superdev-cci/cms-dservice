from ecommerce.functions import calculate_shiping_box
from ecommerce.models import SaleInvoice, Product, Promotion, ShippingBox

test_unit = {
    "CASE2 0+4 (large))": {
        'expect': '0+4 (large)',
        'goods': [
            {
                'CCI002': 3  # RELAX
            },
            {
                'CCI002': 5,  # RELAX
            },
            {
                'CCI002': 6,  # RELAX
            },
            {
                'CCI029': 1,  # Di 8 PRO
            },
            {
                'CCI004': 1,  # CURMA MAX
                'CCI006': 1,  # GREEN CURMIN
            },
            {
                'CCI006': 3  # GREEN CURMIN
            },
            {
                'CCI004': 1,  # CURMA MAX
                'CCI006': 1,  # GREEN CURMIN
            },
            {
                'CCI002': 3,  # RELAX
                'CCI006': 2,  # GREEN CURMIN
            },
            {
                'CCI025': 1  # ICHI COFFEE
            },
            {
                'CCI036': 1  # ICHI BLACK COFFEE
            },
            {
                'CCI024': 2  # ISO CURMA POWDER DRINK
            },
            {
                'CCI002': 2,  # RELAX
                'CCI006': 2,  # GREEN CURMIN
            },
        ]
    },
    "CASE2 2A": {
        'expect': '2A',
        'goods': [
            {
                'CCI002': 7  # RELAX
            },
            {
                'CCI006': 4,  # GREEN CURMIN
            },
            {
                'CCI002': 8,  # RELAX
            },
            {
                'CCI004': 2,  # CURMA MAX
                'CCI006': 1,  # GREEN CURMIN
            },
            {
                'CCI004': 2,  # CURMA MAX
                'CCI006': 1,  # GREEN CURMIN
            },
            {
                'CCI006': 6,  # GREEN CURMIN
            },
            {
                'CCI004': 2,  # CURMA MAX
            },
            {
                'CCI024': 3  # ISO CURMA POWDER DRINK
            },
            {
                'CCI025': 2  # ICHI COFFEE
            },
            {
                'CCI036': 2  # ICHI BLACK COFFEE
            },
        ]
    },
    "CASE2 B": {
        'expect': 'B',
        'goods': [
            {
                'CCI006': 7,  # GREEN CURMIN
            },
            {
                'CCI006': 8,  # GREEN CURMIN
            },
            {
                'CCI002': 2,  # RELAX
                'CCI006': 2,  # GREEN CURMIN
            },
            {
                'CCI004': 2,  # CURMA MAX
            },
            {
                'CCI002': 12,  # RELAX
            },
            {
                'CCI001': 2,  # ARSHITHONG GOLD
            },
            {
                'CCI024': 4  # ISO CURMA POWDER DRINK
            },
            {
                'CCI025': 2  # ICHI COFFEE
            },
            {
                'CCI036': 2  # ICHI BLACK COFFEE
            },
        ]
    },
    "CASE2 2B": {
        'expect': '2B',
        'goods': [
            {
                'CCI006': 13,  # GREEN CURMIN
            },
            {
                'CCI004': 4,  # CURMA MAX
            },
            {
                'CCI024': 8  # ISO CURMA POWDER DRINK
            },
            {
                'CCI002': 21,  # RELAX
            },
            {
                'CCI025': 4  # ICHI COFFEE
            },
            {
                'CCI036': 4  # ICHI BLACK COFFEE
            },

        ]
    },
    "CASE2 E": {
        'expect': 'E',
        'goods': [
            {
                'CCI006': 33,  # GREEN CURMIN
            },
            {
                'CCI004': 12,  # CURMA MAX
            },
            {
                'CCI024': 14  # ISO CURMA POWDER DRINK
            },
            {
                'CCI002': 45,  # RELAX
            },
            {
                'CCI025': 12  # ICHI COFFEE
            },
            {
                'CCI036': 12  # ICHI BLACK COFFEE
            },
            {
                'CCI001': 6,  # ARSHITHONG GOLD
            },
            {
                'CCI006': 2,    # GREEN CURMIN
                'CCI002': 20    # RELAX
            },
            {
                'CCI024': 2,    # ISO CURMA POWDER DRINK
                'CCI002': 20    # RELAX
            },
            {
                'CCI004': 5,  # CURMA MAX
            },
            {
                'CCI004': 6,  # CURMA MAX
            },
            {
                'CCI001': 4,  # ARSHITHONG GOLD
                'CCI006': 6,  # GREEN CURMIN
                'CCI005': 6,  # GREEN CURMIN
                'CCI025': 4,  # ICHI COFFEE
            },
            {
                'PCCI00299': 4
            },
            {
                'CCI004': 10,  # CURMA MAX
                'CCI006': 10,  # GREEN CURMIN
            },
        ]
    },
    # "Other": {
    #
    # }
}


def start_test():
    select_box = [x for x in ShippingBox.objects.filter(active=True)]
    products = {x.pcode: x for x in Product.objects.all()}
    promotions = {x.pcode: x for x in Promotion.objects.prefetch_related('items').all()}

    for k, v in test_unit.items():
        print('Test Case', k, 'expect {}'.format(v['expect']))
        for test_case in v['goods']:
            items = []
            all_item = ''
            for code, qty in test_case.items():
                items.append({
                    'code': code,
                    'qty': qty
                })
                pdesc = products.get(code, None)
                if pdesc is None:
                    pdesc = code
                    # promotions.get(code, '')
                all_item += '{}: {} '.format(pdesc, qty)

            select_item, required_volume, required_weight = calculate_shiping_box.calculate_box(items, select_box,
                                                                                                products, promotions)
            passResult = 'Pass' if v['expect'] == select_item.name else 'FAIL'
            space_use = required_volume / select_item.volume * 100
            print('Result ---> {} !!! {} : Volume {:.2f} cm3, weight {} kg, spcace {:.2f}%'.format(passResult,
                                                                                                   select_item.name,
                                                                                                   required_volume,
                                                                                                   required_weight,
                                                                                                   space_use))
            # print('       ---> Box : Volume {} cm3 , H: {} W: {} L: {}'.format(select_item.volume, select_item.height,
            #                                                                    select_item.width,
            #                                                                    select_item.length))
            print('       ---> Items : {}'.format(all_item))
