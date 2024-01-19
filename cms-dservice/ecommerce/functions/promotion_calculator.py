import operator
from functools import reduce

from ecommerce.models import Promotion


def main():
    queryset = Promotion.objects.prefetch_related('items').all()
    for x in queryset:
        print(x.pcode, x.pdesc)
        if x.items.count() == 0:
            continue
        items = [float(c.product.cost) * float(c.qty) for c in x.items.all()]
        print(items)
        cost = reduce(operator.add, items)
        print(cost)
        x.cost = cost
        x.save()


def cal_promotion_weight():
    queryset = Promotion.objects.prefetch_related('items', 'items__product').all()
    for x in queryset:
        print(x.pcode, x.pdesc)
        if x.items.count() == 0:
            continue

        items = [float(c.product.weight) * float(c.qty) for c in x.items.all()]
        print(items)
        weight = reduce(operator.add, items)
        x.weight = weight
        x.save()
