from django.db import models


class MatchingBonusDetail(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    name_t = models.CharField(max_length=255)
    mposi = models.CharField(max_length=10, blank=True, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    upa_name = models.CharField(max_length=255)
    bposi = models.CharField(max_length=10, blank=True, null=True)
    level = models.DecimalField(max_digits=15, decimal_places=0)
    gen = models.DecimalField(max_digits=15, decimal_places=0)
    btype = models.CharField(max_length=10, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    percer = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()

    class Meta:
        db_table = 'ali_dc'
        verbose_name = 'Matching bonus detail'


# class MatchingBonusDetail(models.Model):
#     rcode = models.IntegerField()
#     mcode = models.CharField(max_length=255)
#     upa_code = models.CharField(max_length=255, blank=True, null=True)
#     lr = models.IntegerField(blank=True, null=True)
#     pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
#     gpv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
#     mpos = models.CharField(max_length=10)
#     npos = models.CharField(max_length=10)
#
#     class Meta:
#         managed = False
#         db_table = 'ali_dm'
#         verbose_name = 'Matching bonus detail'


class MatchingBonus(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    bonus = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    pos_cur = models.CharField(max_length=255)
    adjust = models.DecimalField(max_digits=15, decimal_places=2)
    pstatus = models.IntegerField()
    prcode = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=2)
    locationbase = models.IntegerField()

    class Meta:
        db_table = 'ali_dmbonus'
        verbose_name = 'Matching bonus'
