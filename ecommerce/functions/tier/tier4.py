from functools import reduce
from ecommerce.models import Product, ProductClass
import operator
import ast
from .base import Tier


class Tier4(Tier):

    def set_price(self, rule, ptype, result):
        condition = int(rule.formula.split('__')[1])
        set_value = int(ptype.meta.split('__')[1])
        # add_qty = int(ptype.meta.split('__')[1])
        for x in result['items']:
            if x['qty'] >= 12:
                prices = 5800 + ((x['qty'] % 12) * set_value)
            else:
                prices = set_value * x['qty']

            x['prices'] = prices
            x['product_prices'] = set_value
        return result
