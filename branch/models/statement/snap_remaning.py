from django.db import models
from datetime import datetime
from accounting.models.statement import AbstractGoodsStatement


class BranchGoodsSnapRemainingItem(models.Model):
    statement = models.ForeignKey('BranchGoodsSnapRemainingStatement', related_name='items', null=True, blank=True,
                                  on_delete=models.CASCADE)
    product = models.ForeignKey('ecommerce.Product', null=True, blank=True, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)


class BranchGoodsSnapRemainingStatement(AbstractGoodsStatement):

    @staticmethod
    def generate_bill_number(branch):
        dt = datetime.today()
        queryset = BranchGoodsSnapRemainingStatement.objects.filter(branch__inv_code=branch).order_by('-id')
        if len(queryset) == 0:
            running_number = 1
        else:
            running_number = queryset.first().bill_number[-4:]
            if running_number is None:
                running_number = 1
            else:
                running_number = int(running_number)
                running_number += 1

        return 'BSR{}{}{:04}'.format(branch.code, dt.strftime('%y%m%d'), running_number)

    class Meta:
        ordering = ('-create_date', '-id',)
