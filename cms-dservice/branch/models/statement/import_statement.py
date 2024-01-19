from datetime import datetime
from django.db import models

from accounting.models.statement import AbstractGoodsStatement
from core.exceptions import AssertBranchError


class BranchGoodsImportItem(models.Model):
    statement = models.ForeignKey('BranchGoodsImportStatement', related_name='items', null=True, blank=True,
                                  on_delete=models.CASCADE)
    product = models.ForeignKey('ecommerce.Product', null=True, blank=True, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True, default=0)
    qty = models.IntegerField(default=0)

    @property
    def amount(self):
        return self.price * self.qty


class BranchGoodsImportStatement(AbstractGoodsStatement):

    @staticmethod
    def generate_bill_number(branch):
        dt = datetime.today()
        queryset = BranchGoodsImportStatement.objects.filter(branch__inv_code=branch).order_by('-id')
        if len(queryset) == 0:
            running_number = 1
        else:
            running_number = queryset.first().bill_number[-4:]
            if running_number is None:
                running_number = 1
            else:
                running_number = int(running_number)
                running_number += 1

        return 'BIS{}{}{:04}'.format(branch.code, dt.strftime('%y%m%d'), running_number)

    seller_name = models.CharField(max_length=128)
    from_branch = models.ForeignKey('branch.Branch', null=True, on_delete=models.SET_NULL,
                                    related_name='import_statements')
    import_statement = models.OneToOneField('branch.BranchGoodsImportStatement', on_delete=models.SET_NULL, null=True,
                                            blank=True)
    total = models.FloatField(default=0)

    class Meta:
        ordering = ('-create_date', '-id',)
