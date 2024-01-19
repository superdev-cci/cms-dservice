from ecommerce.models import SaleInvoice, Product, Promotion


def cal_bill_weight(start, end):
    pool = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '10': 0,
        '20': 0,
        '30': 0,
        '40': 0,
        '50': 0,
        '70': 0,
        '100': 0,
        '101': 0
    }
    prices_pool = {
        '20': {
            'pv': 0,
            'prices': 0
        },
        '30': {
            'pv': 0,
            'prices': 0
        },
        '40': {
            'pv': 0,
            'prices': 0
        },
        '50': {
            'pv': 0,
            'prices': 0
        },
        '70': {
            'pv': 0,
            'prices': 0
        },
        '100': {
            'pv': 0,
            'prices': 0
        },
        '101': {
            'pv': 0,
            'prices': 0
        }
    }

    products = {x.pcode: x for x in Product.objects.all()}
    promotions = {x.pcode: x for x in Promotion.objects.all()}

    queryset = SaleInvoice.objects.prefetch_related('items').filter(sadate__range=(start, end), cancel=0, total__gt=10,
                                                                    sa_type__in=('A', 'H',))
    products_list = {}
    for x in queryset:
        weight = 0
        for item in x.items.all():
            if item.pcode in products:
                weight += (products[item.pcode].weight * item.qty)
            else:
                weight += (promotions[item.pcode].weight * item.qty)

            if (weight / 1000) <= 2:
                if item.pcode not in products_list:
                    products_list[item.pcode] = 1
                else:
                    products_list[item.pcode] += 1

        weight = weight / 1000
        if weight <= 5:
            if weight <= 1:
                pool['1'] += 1
            elif 1 < weight <= 2:
                pool['2'] += 1
            elif 2 < weight <= 3:
                pool['2'] += 1
            elif 4 < weight <= 5:
                pool['2'] += 1
            else:
                pool['5'] += 1
        elif weight <= 10:
            pool['10'] += 1
        elif weight <= 20:
            pool['20'] += 1
            prices_pool['20']['prices'] += x.total
            prices_pool['20']['pv'] += x.tot_pv
        elif weight <= 30:
            pool['30'] += 1
            prices_pool['30']['prices'] += x.total
            prices_pool['30']['pv'] += x.tot_pv
        elif weight <= 40:
            pool['40'] += 1
            prices_pool['40']['prices'] += x.total
            prices_pool['40']['pv'] += x.tot_pv
        elif weight <= 50:
            pool['50'] += 1
            prices_pool['50']['prices'] += x.total
            prices_pool['50']['pv'] += x.tot_pv
        elif weight <= 70:
            pool['70'] += 1
            prices_pool['70']['prices'] += x.total
            prices_pool['70']['pv'] += x.tot_pv
        elif weight <= 100:
            pool['100'] += 1
            prices_pool['100']['prices'] += x.total
            prices_pool['100']['pv'] += x.tot_pv
        else:
            pool['101'] += 1

    print(pool)
    print(prices_pool)
    return pool, prices_pool, products_list
