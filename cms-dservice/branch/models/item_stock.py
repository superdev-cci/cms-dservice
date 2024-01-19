from django.db import models


class BranchStock(models.Model):
    pcode = models.CharField(max_length=255)
    qty = models.IntegerField(blank=True, null=True)
    qtys = models.IntegerField(default=0)
    qtyr = models.IntegerField(default=0)
    qtyd = models.IntegerField(default=0)
    ud = models.CharField(max_length=255, blank=True, null=True)
    inv_code = models.CharField(max_length=255)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('ecommerce.Product', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'ali_product_invent'
        verbose_name_plural = 'Item Stock'
