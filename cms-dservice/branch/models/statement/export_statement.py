from datetime import datetime
from django.db import models

from accounting.models.statement import AbstractGoodsStatement
from core.exceptions import AssertBranchError


class BranchGoodsExportItem(models.Model):
    statement = models.ForeignKey('BranchGoodsExportStatement', related_name='items', null=True, blank=True,
                                  on_delete=models.CASCADE)
    product = models.ForeignKey('ecommerce.Product', null=True, blank=True, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True, default=0)
    qty = models.IntegerField(default=0)

    @property
    def amount(self):
        return self.price * self.qty


class BranchGoodsExportStatement(AbstractGoodsStatement):

    @staticmethod
    def generate_bill_number(branch):
        dt = datetime.today()
        queryset = BranchGoodsExportStatement.objects.filter(branch__inv_code=branch).order_by('-id')
        if len(queryset) == 0:
            running_number = 1
        else:
            running_number = queryset.first().bill_number[-4:]
            if running_number is None:
                running_number = 1
            else:
                running_number = int(running_number)
                running_number += 1

        return 'BES{}{}{:04}'.format(branch.code, dt.strftime('%y%m%d'), running_number)

    seller_name = models.CharField(max_length=128)
    to_branch = models.ForeignKey('branch.Branch', null=True, on_delete=models.SET_NULL,
                                  related_name='export_statements')
    total = models.FloatField(default=0)

    class Meta:
        ordering = ('-create_date', '-id',)
