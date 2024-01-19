from django.db.models import Q
from branch.models import Branch, BranchStock, StockStatement
from ecommerce.models import Product, SaleInvoice, SaleItem
from branch.serializers import StockMovementSerializer, BranchItemStockSerializer
from ecommerce.serializers import SaleInvoiceSerializer, SaleItemSerializer
from datetime import date
import pprint
import operator


def get_or_create(branch, item, default_qty):
    instance, create = BranchStock.objects.get_or_create(
        branch=branch,
        product=item,
        defaults={
            'pcode': item.pcode,
            'qty': 0 + default_qty,
            'qtys': 0,
            'qtyr': 0,
            'qtyd': 0,
            'ud': '',
            'inv_code': branch.inv_code,
            'branch': branch,
            'product': item
        }
    )
    return instance, create


def create_movement(statement, to_branch, ref_branch, stock_item, item, qty, action):
    meta = {
        "client_code": statement.create_user,
        "client_name": statement.create_user,
        "branch_name": statement.branch.inv_code,
        "from_branch": ref_branch,
        "to_branch": to_branch,
        "bill_number": statement.bill_number,
        "sano_ref": '',
        "pcode": item.product.pcode,
        "pdesc": item.product.pdesc,
        "date_issue": statement.date_issue,
        "rdate": date.today().strftime('%Y-%m-%d'),
        "rccode": None,
        "uid": statement.create_user,
        "action": statement.statement_type,
        "bring_forward": 0,
        "balance": 0,
        "price": item.price,
        "amount": 0
    }
    if action == 'import':
        meta['in_qty'] = operator.abs(qty)
        meta['in_price'] = item.price
        meta['in_amount'] = item.amount
    else:
        meta['out_qty'] = operator.abs(qty)
        meta['out_price'] = item.price
        meta['out_amount'] = item.amount

    meta['bring_forward'] = stock_item.qty
    meta['balance'] = stock_item.qty + qty
    meta['amount'] = operator.abs(qty) * item.price

    return StockStatement.objects.create(**meta)


def update_stock(statement_obj, action, bill_type):  # stamp StockStatement for BranchGoodsTransferStatement
    obj_list = []
    for si in statement_obj.items.all():
        branch_obj = statement_obj.branch
        product_obj = si.product
        qty = int(si.qty)
        if bill_type == 'import_statement':
            another_branch = statement_obj.from_branch
        else:
            another_branch = statement_obj.to_branch
        if action in ('send', 'sale'):
            item_stock, created = get_or_create(branch_obj, product_obj, -qty)
            create_movement(statement_obj, branch_obj, another_branch, item_stock, si, -qty, 'export')
            item_stock.qty -= qty
            item_stock.save()
        elif action in ('receive', 'cancel'):
            item_stock, created = get_or_create(branch_obj, product_obj, qty)
            create_movement(statement_obj, branch_obj, another_branch, item_stock, si, qty, 'import')
            item_stock.qty += qty
            item_stock.save()
        elif action == 'reject':
            pass

        # obj_list.append({'BranchStock_obj': obj2, 'StockStatement_obj': obj})
    return obj_list


def create_hq_stock():
    query_set = Product.objects.filter(
        Q(pcode__startswith='CCI') | Q(pcode__startswith='AS') | Q(pcode__startswith='DI'))
    branch = Branch.objects.get(inv_type=2)
    create_list = []
    for x in query_set:
        if BranchStock.objects.filter(pcode=x.pcode, inv_code=branch.inv_code).count() == 0:
            create_list.append(BranchStock(pcode=x.pcode,
                                           qty=x.qty,
                                           inv_code=branch.inv_code,
                                           branch=branch,
                                           product_id=x.pcode))
    BranchStock.objects.bulk_create(create_list)


def link_record():
    all_product = {x.pcode: x for x in Product.objects.all()}
    all_branch = {x.inv_code: x for x in Branch.objects.all()}
    for x in BranchStock.objects.filter(branch__isnull=True):
        x.branch = all_branch.get(x.inv_code, None)
        x.save()

    for x in BranchStock.objects.filter(product__isnull=True):
        x.product = all_product.get(x.pcode, None)
        x.save()
