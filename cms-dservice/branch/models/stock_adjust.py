from django.db import models
from ecommerce.models import Product
import datetime


class StockAdjustItem(models.Model):
    bill_number = models.ForeignKey('StockAdjustStatement', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)


class StockAdjustStatement(models.Model):
    bill_number = models.CharField(max_length=32, blank=True, null=True)
    sadate = models.DateField(default=datetime.date.today)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    usercode = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    cancel = models.IntegerField(blank=True, null=True)
    cancel_date = models.DateField(blank=True, null=True)
    uid_cancel = models.CharField(max_length=255)

    class Meta:
        ordering = ('-sadate', 'bill_number')

    @property
    def date_issue(self):
        return self.sadate