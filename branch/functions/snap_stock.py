from accounting.models import StatementType, StatementState
from branch.models import Branch, BranchGoodsSnapRemainingStatement, BranchGoodsSnapRemainingItem, BranchStock
from ecommerce.models import Product
from django.db.models import Q


class BranchSnapStockCard(object):

    def __init__(self, *args, **kwargs):
        return

    def sync_hq_stock(self):
        query_set = Product.objects.filter(
            Q(pcode__startswith='CCI') | Q(pcode__startswith='AS') | Q(pcode__startswith='DI'))
        branch = Branch.objects.get(inv_type=2)
        for x in query_set:
            item = BranchStock.objects.filter(pcode=x.pcode, inv_code=branch.inv_code)
            if item.count() != 0:
                item = item.first()
                item.qty = x.qty
                item.save()
            else:
                BranchStock.objects.create(pcode=x.pcode,
                                           qty=x.qty,
                                           inv_code=branch.inv_code,
                                           branch=branch,
                                           product_id=x.pcode)
        return

    def create(self):
        self.sync_hq_stock()

        for branch in Branch.objects.all():
            statement_type = StatementType.objects.get(code='BSR')
            statement_state = StatementState.objects.get(code='CM')
            create_bill = BranchGoodsSnapRemainingStatement(statement_type=statement_type,
                                                            statement_state=statement_state,
                                                            create_user='System')
            create_bill.bill_number = BranchGoodsSnapRemainingStatement.generate_bill_number(branch)
            create_bill.branch = branch
            # create_bill = create_bill.save()
            create_bill.save()
            # Branch stock snap
            create_list = []
            for item in branch.branchstock_set.filter(product__activated=True):
                create_list.append(BranchGoodsSnapRemainingItem(statement=create_bill,
                                                                product=item.product,
                                                                qty=item.qty))
            BranchGoodsSnapRemainingItem.objects.bulk_create(create_list)
        return
