from ecommerce.models import SaleInvoice, Product, Promotion, ShippingBox
from ecommerce.functions import calculate_shiping_box
import pandas as pd

def insert_to_dict(pool, box_code):
    box = 'Oversize'
    if box_code is not None:
        box = box_code.name

    if box not in pool:
        pool[box] = 0

    pool[box] += 1

    return pool


def cal_sales_sku(start, end):
    pool = {}

    select_box = [x for x in ShippingBox.objects.filter(active=True)]
    products = {x.pcode: x for x in Product.objects.all()}
    promotions = {x.pcode: x for x in Promotion.objects.prefetch_related('items').all()}
    queryset = SaleInvoice.objects.prefetch_related('items').filter(sadate__range=(start, end), cancel=0, total__gt=10,
                                                                    sa_type__in=('A', 'H',))
    products_list = {}
    for x in queryset:
        weight = 0
        items = []
        for item in x.items.all():
            if item.pcode.startswith('PCCI') or item.pcode.startswith('CCI'):
                items.append({
                    'code': item.pcode,
                    'qty': int(item.qty)
                })

        select_item, required_volume, required_weight = calculate_shiping_box.calculate_box(items, select_box, products, promotions)
        pool = insert_to_dict(pool, select_item)

    print(pool)
    return pool


def export_excel(start, end):
    x = cal_sales_sku(start, end)
    df = pd.DataFrame.from_dict(x)
    xf = df.T
    xf = xf.sort_index()
    xf.to_excel('./shipping_box.xlsx', na_rep=0, encoding="utf-8")
    return x
