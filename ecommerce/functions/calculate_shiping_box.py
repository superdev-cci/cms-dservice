import operator
from ecommerce.models.shipping_box import ShippingBox
from ecommerce.models.product import Product
from ecommerce.models.promotion import Promotion

exception_size = {
    '2B': {
        'CCI003': 'gt__4',
        'CCI004': 'gt__4',
        'CCI0010': 'gt__4',
        'CCI0022': 'gt__4',
    }
}


def check_exception_size(size, data):
    select_size = exception_size.get(size, None)
    if select_size is None:
        return False

    for k, v in data.items():
        if k in select_size.keys():
            token = select_size[k].split('__')
            method = getattr(operator, token[0])
            if method(v, int(token[1])):
                return True

    return False


def calculate_dimension(items, product_pool=None, promotion_pool=None):
    total_volume = 0
    total_weight = 0
    max_height = 0
    max_width = 0

    items_code = [x['code'] for x in items]
    if product_pool is None:
        products = {x.pcode: x for x in Product.objects.filter(pcode__in=items_code)}
    else:
        products = product_pool

    if promotion_pool is None:
        promotions = {x.pcode: x for x in Promotion.objects.prefetch_related('items').filter(pcode__in=items_code)}
    else:
        promotions = promotion_pool

    all_items = {}

    for x in items:
        if x['code'].startswith('PCCI'):
            promotion = promotions[x['code']]
            for promotion_item in promotion.items.all():
                total_volume += promotion_item.product.volume * promotion_item.qty * x['qty']
                total_weight += promotion_item.product.weight * promotion_item.qty * x['qty']
                max_height = sorted([max_height, promotion_item.product.height], reverse=True)[0]
                max_width = sorted([max_width, promotion_item.product.weight], reverse=True)[0]

                if x['code'] in all_items:
                    all_items[promotion_item.product.pcode] += promotion_item.qty * x['qty']
                else:
                    all_items[promotion_item.product.pcode] = promotion_item.qty * x['qty']
        else:
            product = products[x['code']]
            total_volume += product.volume * x['qty']
            total_weight += (product.weight * x['qty'])
            max_height = sorted([max_height, product.height], reverse=True)[0]
            max_width = sorted([max_width, product.weight], reverse=True)[0]

            if x['code'] in all_items:
                all_items[x['code']] += x['qty']
            else:
                all_items[x['code']] = x['qty']

    return all_items, float(total_volume) * 1.1, float(total_weight) / 1000, float(max_height) * 1.05, float(
        max_width) * 1.05


def calculate_box(items, shipping_box_pool=None, product_pool=None, promotion_pool=None):
    all_items, required_volume, required_weight, required_height, required_width = calculate_dimension(items,
                                                                                                       product_pool,
                                                                                                       promotion_pool)
    if shipping_box_pool is None:
        select_box = [x for x in ShippingBox.objects.filter(active=True)]
    else:
        select_box = shipping_box_pool

    select_box = sorted(select_box, key=lambda x: x.volume)

    match_volume = sorted(filter(lambda x: x.volume > (required_volume * 1), select_box), key=lambda x: x.volume)
    match_volume = list(filter(lambda x: x.max_weight > required_weight, match_volume))

    select_item = None
    for x in match_volume:
        if check_exception_size(x.name, all_items) is True:
            continue
        if x.height < required_height:
            if required_height > x.width:
                continue
            else:
                if required_height < x.width:
                    select_item = x
                    break
        select_item = x
        break

    return select_item, required_volume, required_weight
