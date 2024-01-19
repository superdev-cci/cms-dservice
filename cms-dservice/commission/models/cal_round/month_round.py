from django.db import models


class MonthRound(models.Model):
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
    timequery = models.IntegerField()
    uid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_bround'