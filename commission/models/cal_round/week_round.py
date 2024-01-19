from django.db import models


class WeekRound(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)
    fsano = models.CharField(max_length=7, blank=True, null=True)
    tsano = models.CharField(max_length=7, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    calc_date = models.DateTimeField()
    remark = models.CharField(max_length=50, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()
    fpdate = models.DateField()
    tpdate = models.DateField()
    total_a = models.DecimalField(max_digits=15, decimal_places=2)
    total_h = models.DecimalField(max_digits=15, decimal_places=2)
    fast = models.DecimalField(max_digits=15, decimal_places=2)
    invent = models.DecimalField(max_digits=15, decimal_places=2)
    binaryt = models.DecimalField(max_digits=15, decimal_places=2)
    matching = models.DecimalField(max_digits=15, decimal_places=2)
    pool = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_binary = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_matching = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_pool = models.DecimalField(max_digits=15, decimal_places=2)
    timequery = models.IntegerField()
    countquery = models.IntegerField()
    uid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_around'

    @property
    def period(self):
        return {
            'start': self.fdate,
            'end': self.tdate
        }

    # @property
    # def get_sales(self):
    #     report = SaleSummaryReport(start=self.fdate, end=self.tdate, get_type='monthly')
    #     return report.total

    # @property
    # def total_sale_pv(self):
    #     return PvFromSaleInvoice(start=self.fdate, end=self.tdate).total
    #
    # @property
    # def total_transfer_pv(self):
    #     return PvFromPvTransfer(start=self.fdate, end=self.tdate).total
