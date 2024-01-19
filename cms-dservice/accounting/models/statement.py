from django.db import models
from django.utils import timezone
from datetime import date

from simple_history.models import HistoricalRecords

from core.exceptions import AssertBranchError


class AbstractBaseStatement(models.Model):
    bill_number = models.CharField(max_length=32)
    create_date = models.DateTimeField(default=timezone.now)
    date_issue = models.DateField(default=date.today)
    statement_type = models.ForeignKey('accounting.StatementType', null=True, blank=True, on_delete=models.CASCADE)
    statement_state = models.ForeignKey('accounting.StatementState', null=True, blank=True, on_delete=models.CASCADE)
    remark = models.CharField(max_length=128, null=True, blank=True)
    discount = models.FloatField(default=0)
    history = HistoricalRecords(inherit=True)
    create_user = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        abstract = True


class AbstractGoodsStatement(AbstractBaseStatement):
    branch = models.ForeignKey('branch.Branch', null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    # def remove_goods_form_branch(self):
    #     assert self.branch is not None, AssertBranchError(self, 'Branch is not exist on {}'.format(self.bill_number))
    #     branch = self.branch
    #     product_ids = [x['item'] for x in self.goods]
    #     stock_ins = {x.id: x for x in branch.goods.filter(id__in=product_ids)}
    #     for x in self.goods:
    #         stock = stock_ins[x['item']]
    #         stock.qty = stock.qty - int(x['qty'])
    #         stock.save()
    #     return
