from django.db import models


class T2PPResult(models.Model):
    app_code = models.CharField(max_length=32, blank=True)
    invoice_no = models.CharField(max_length=32, blank=True)
    amount = models.CharField(max_length=32, blank=True)
    tx_id = models.CharField(max_length=32, blank=True)
    return_code = models.CharField(max_length=8, blank=True)
    channel = models.CharField(max_length=32, blank=True)

    order = models.ForeignKey('SaleInvoice', on_delete=models.CASCADE, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
