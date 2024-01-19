from .base import Tier
from .tier4 import Tier4
from ...models import DropShipPromotion, Product
import ast
import operator
from core.utility.dict_transfrom import list_to_dict


class CombineShipping(object):
    tier_pool = {
        'Tier1': Tier,
        'Tier2': Tier,
        'Tier3': Tier,
        'Tier4': Tier4,
        'Tier5': Tier,
        'Tier6': Tier,
        'Tier7': Tier
    }

    tier_select = {
        'T1': 'Tier1',
        'T2': 'Tier2',
        'T3': 'Tier3',
        'T4': 'Tier4',
        'T5': 'Tier5',
        'T6': 'Tier6',
        'T7': 'Tier7',
    }

    def __init__(self, product_class, data, products):
        self.product_class = product_class
        self.data = data
        self.products = {x.pcode: x for x in products}
        self.products_query = products

    def create_init(self):
        return {
            'items': [],
            'ship': 0,
            'cod': 0,
            'total': 0
        }

    def solve_product_match(self, formula):
        token = formula.split('__')
        pool = list_to_dict(self.data, 'code')
        tier = self.tier_select[token[0]]
        product = None
        match = False
        for k, v in self.products.items():
            if v.product_class.name == tier:
                match = True
                product = k
        method = getattr(operator, token[1])
        if not method(pool[product]['qty'], int(token[2])):
            match = False
        return match

    def calculate_by_tier(self):
        pool = []
        sort_data = {}
        for x in self.product_class:
            sort_data[x] = list(filter(lambda y: self.products[y['code']].product_class.name == x, self.data))
        print(sort_data)
        for k, v in sort_data.items():
            pclass = self.product_class[k]
            instance = self.tier_pool[k](pclass, self.products_query, v, combine=True)
            pool.append(instance.calculate())
        # for x in self.data:
        #     product = self.products[x['code']]
        #     pclass = product.product_class
        #     instance = self.tier_pool[pclass.name](pclass, self.products_query, [x, ], combine=True)
        #     pool.append(instance.calculate())
        return pool

    def calculate(self):
        pool = []
        result = self.create_init()
        static_shipping = False
        if len(self.product_class.keys()) is 2:
            pclass = [x for x in self.product_class.values()]
            if len(pclass) is 2:
                promotions = DropShipPromotion.objects.filter(items=pclass[0]).filter(items=pclass[1])
                if promotions:
                    match_promotion = None
                    # Solve Match promotion by item
                    for x in promotions:
                        if x.formula == '-':
                            continue
                        formula = x.formula.split(' ')
                        if len(formula) > 1:
                            case1 = self.solve_product_match(formula[0])
                            case2 = self.solve_product_match(formula[2])
                            method = getattr(operator, formula[1].lower())
                            if method(case1, case2):
                                match_promotion = x

                    if match_promotion:
                        ship = ast.literal_eval(match_promotion.ship_prices)
                        for t in match_promotion.types.all():
                            if operator.contains(t.meta, 'static'):
                                static_shipping = True
                        result['ship'] = ship[0]
                        result['cod'] = ship[1]

                    pool = self.calculate_by_tier()
                else:
                    pool = self.calculate_by_tier()
            else:
                pool = self.calculate_by_tier()
        else:
            pool = self.calculate_by_tier()

        start_prices = 0
        for x in pool:
            prices = x['items'][0]['product_prices']
            result['items'] = result['items'] + x['items']
            result['total'] += x['total']

            if prices > start_prices:
                start_prices = prices
                if static_shipping is False:
                    result['ship'] = x['ship']
                    result['cod'] = x['cod']
                    # if result['ship'] < x['ship']:
                    #     result['ship'] = x['ship']
                    #
                    # if result['cod'] < x['cod']:
                    #     result['cod'] = x['cod']

            if x.get('add') is not None:
                if result.get('add') is None:
                    result['add'] = []
                result['add'].append(x['add'])
        return result
