from django.db import models


class LogWallet(models.Model):
    rcode = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()
    mcode = models.CharField(max_length=255)
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    evoucher = models.DecimalField(max_digits=15, decimal_places=2)
    eautoship = models.DecimalField(max_digits=15, decimal_places=2)
    ecom = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'ali_log_wallet'
        verbose_name_plural = 'Wallet log'

