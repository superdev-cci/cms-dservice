from ..models import Product, ProductClass
from .tier.base import Tier
from .tier import Tier4, CombineShipping
import operator

tier_pool = {
    'Tier1': Tier,
    'Tier2': Tier,
    'Tier3': Tier,
    'Tier4': Tier4,
    'Tier5': Tier,
    'Tier6': Tier,
    'Tier7': Tier
}


def recal_prices(data):
    global tier_pool
    all_code = [x['code'] for x in data]
    all_product = Product.objects.filter(pcode__in=all_code).select_related('product_class')
    product_class = {x.product_class.name: x.product_class for x in all_product}
    if len(product_class.keys()) is 1:
        pclass = list(product_class.values())[0]
        products = pclass.product_set.filter(pcode__in=all_code)
        instance = tier_pool[pclass.name](pclass, products, data)
        result = instance.calculate()
        # result['add'] = [result['add'],]
        if result.get('add') is not None:
            result['add'] = [result['add'],]
        return result
    else:
        instance = CombineShipping(product_class, data, all_product)
        return instance.calculate()
