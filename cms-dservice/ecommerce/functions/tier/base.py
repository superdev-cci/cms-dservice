from functools import reduce
from ecommerce.models import Product, ProductClass
import operator
import ast


class Tier(object):

    def __init__(self, pclass, product, data, combine=False):
        self.pclass = pclass
        self.product = product
        self.data = data
        self.qty = reduce(operator.add, [x['qty'] for x in data])
        self.base_prices = 0
        self.product_pool = {x.pcode: x for x in product}
        self.add_flag = False
        self.combine = combine

    def find_rule(self):
        rule = self.pclass.dropshippromotion_set.all()
        rule_match = {}
        for x in rule:
            if len(x.types.filter(meta='force_combile')):
                continue
            if x.formula != '-':
                token = x.formula.split('__')
                if token[0].startswith('T'):
                    token = token[:1]
                method = getattr(operator, token[0])
                if method(self.qty, int(token[1])):
                    if self.combine is False:
                        if '&' not in x.name:
                            rule_match[x.name] = x
                    else:
                        rule_match[x.name] = x

        return rule_match

    def re_produce(self):
        result = {
            'items': [],
            'ship': 0,
            'cod': 0,
            'total': 0
        }
        for x in self.data:
            product_price = self.product_pool[x['code']].personel_price
            result['items'].append({
                'code': x['code'],
                'qty': x['qty'],
                'prices': x['qty'] * product_price,
                'product_prices': product_price
            })
            self.base_prices = product_price
        result['items'] = sorted(result['items'], key=lambda item: item['qty'], reverse=True)
        return result

    def add(self, rule, ptype, result):
        condition = int(rule.formula.split('__')[1])
        add_qty = int(ptype.meta.split('__')[1])
        factor = (self.qty // condition) * add_qty
        # if len(result['items']) > 1:
        #     discount = self.base_prices * factor
        #     result['items'][0]['prices'] -= discount

        if factor > 0:
            result['add'] = {
                'code': result['items'][0]['code'],
                'qty': factor
            }
        self.add_flag = True
        return result

    def sub_price(self, rule, ptype, result):
        condition = int(rule.formula.split('__')[1])
        sub_value = int(ptype.meta.split('__')[1])
        factor = (self.qty // condition)
        result['items'][0]['prices'] -= (sub_value * factor)

        return result

    def set_price(self, rule, ptype, result):
        condition = int(rule.formula.split('__')[1])
        set_value = int(ptype.meta.split('__')[1])
        op = rule.formula.split('__')[0]
        total_qty = self.qty
        for x in result['items']:
            if op == 'eq':
                x['prices'] = set_value * x['qty']
                continue
            if total_qty > x['qty']:
                current_qty = x['qty']
            else:
                current_qty = total_qty
            round_value = current_qty // condition
            diff = current_qty % condition

            if round_value:
                base_prices = self.base_prices * (condition * round_value)
                addon_prices = set_value * diff
            else:
                base_prices = 0
                addon_prices = set_value * diff
            x['prices'] = base_prices + addon_prices
            x['product_prices'] = base_prices
            total_qty -= current_qty
        return result

    def calculate(self):
        rule = self.find_rule()
        result = self.re_produce()
        self.add_flag = False

        for x in sorted(rule.values(), key=lambda r: r.priority):
            if x.ship_prices != '':
                ship = ast.literal_eval(x.ship_prices)
                result['ship'] = ship[0]
                result['cod'] = ship[1]

            all_type = x.types.all()
            for t in all_type:
                if operator.contains(t.meta, 'add'):
                    result = self.add(x, t, result)
                elif operator.contains(t.meta, 'set'):
                    result = self.set_price(x, t, result)
                elif operator.contains(t.meta, 'sub'):
                    result = self.sub_price(x, t, result)
        result['total'] = reduce(operator.add, [x['prices'] for x in result['items']])
        return result
