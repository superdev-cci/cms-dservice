from django.db import models

from core.models import AbstractBaseCode


class PaymentType(AbstractBaseCode):
    enable = models.BooleanField(default=True)


class Payment(AbstractBaseCode):
    BILL_STATE_TYPE_CHOICE = (
        ('CA', 'CASH'),
        ('TR', 'TRANSFER'),
        ('CE', 'Credit'),
        ('TP', 'P2P'),
        ('VC', 'VOUCHER')
    )

    invoice = models.ForeignKey('ecommerce.SaleInvoice', on_delete=models.CASCADE, null=True, blank=True)
    payment_type = models.CharField(max_length=4, choices=BILL_STATE_TYPE_CHOICE, blank=True, null=True)
    amount = models.FloatField(default=0)
    remark = models.CharField(max_length=64, null=True, blank=True)
