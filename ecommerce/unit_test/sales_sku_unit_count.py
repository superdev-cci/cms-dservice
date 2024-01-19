from ecommerce.models import SaleInvoice, Product, Promotion
import pandas as pd

def insert_to_dict(pool, code, qty):
    if code not in pool:
        pool[code] = {
            101: 0,
            100: 0,
            50: 0,
            40: 0,
            30: 0,
            20: 0,
            10: 0,
            5: 0,
            1: 0
        }

    for k, v in pool[code].items():
        if qty >= k:
            pool[code][k] += 1
            break

    return pool


def cal_sales_sku(start, end):
    pool = {}

    products = {x.pcode: x for x in Product.objects.all()}
    promotions = {x.pcode: x for x in Promotion.objects.prefetch_related('items').all()}

    queryset = SaleInvoice.objects.prefetch_related('items').filter(sadate__range=(start, end), cancel=0, total__gt=10,
                                                                    sa_type__in=('A', 'H',))
    products_list = {}
    for x in queryset:
        weight = 0
        for item in x.items.all():
            if item.pcode in products:
                pool = insert_to_dict(pool, (item.pcode, item.pdesc), int(item.qty))
            else:
                for pitem in promotions[item.pcode].items.all():
                    pool = insert_to_dict(pool, (pitem.pcode, pitem.pdesc), int(pitem.qty) * int(item.qty))

    print(pool)
    return pool


def export_excel(start, end):
    x = cal_sales_sku(start, end)
    df = pd.DataFrame.from_dict(x)
    xf = df.T
    xf = xf.sort_index()
    xf.to_excel('./sales_sku.xlsx', na_rep=0, encoding="utf-8")
    return x
