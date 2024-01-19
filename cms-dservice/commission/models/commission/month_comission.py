from django.db import models


class MonthCommission(models.Model):
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    name_t = models.CharField(max_length=255)
    pos_cur3 = models.CharField(max_length=255)
    dmbonus = models.DecimalField(max_digits=15, decimal_places=2)
    embonus = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    rcode = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        db_table = 'ali_commission_b'
        verbose_name = 'Month commission'


class MonthQualified(models.Model):
    rcode = models.IntegerField()
    sano = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=2)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    pvb = models.IntegerField()
    mdate = models.DateField()
    sdate = models.DateField()
    satype = models.CharField(max_length=5)
    month_pv = models.CharField(max_length=10)
    mpos = models.CharField(max_length=255)
    realpos = models.CharField(max_length=255)
    first_regis = models.IntegerField()

    class Meta:
        db_table = 'ali_status'
