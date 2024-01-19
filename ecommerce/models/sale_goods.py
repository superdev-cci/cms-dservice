from django.db import models


class SaleItem(models.Model):
    """
    a class represent a products in Sale Invoice
    """
    sano = models.CharField(max_length=7, blank=True, null=True)
    sano_link = models.ForeignKey('SaleInvoice', on_delete=models.CASCADE, null=True, blank=True, related_name='items')
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=16,blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    customer_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sppv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    uidbase = models.CharField(max_length=255, blank=True, null=True)
    locationbase = models.IntegerField(default=1)
    outstanding = models.CharField(max_length=255, blank=True, null=True)
    vat = models.IntegerField(default=7)

    class Meta:
        db_table = 'ali_asaled'
        verbose_name_plural = 'Sale Item'
