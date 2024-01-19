from django.db import models
import datetime


class PvTransfer(models.Model):
    hono = models.IntegerField(blank=True, null=True)
    sano = models.IntegerField(blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    sctime = models.DateTimeField(default=datetime.datetime.now, blank=True)
    sa_type = models.CharField(max_length=2, blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_code_to = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tot_sppv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    cancel = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True, related_name='transfer_outs')
    dl = models.CharField(max_length=1, blank=True, null=True)
    print = models.IntegerField(default=0, blank=True, null=True)
    rcode = models.IntegerField(default=9, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    bmcauto = models.IntegerField(blank=True, null=True)
    cancel_date = models.DateField(blank=True, null=True)
    uid_cancel = models.CharField(max_length=255, blank=True, null=True)
    mbase = models.CharField(max_length=255, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    locationbase = models.IntegerField(blank=True, null=True)
    name_f = models.CharField(max_length=255, blank=True, null=True)
    name_t = models.CharField(max_length=255, blank=True, null=True)
    crate = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    sp_code = models.CharField(max_length=255, blank=True, null=True)
    sp_pos = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=100, blank=True, null=True)
    status_package = models.IntegerField(blank=True, null=True)

    remote_ip = models.CharField(max_length=64, default='localhost', blank=True)

    class Meta:
        db_table = 'ali_holdhead'

    def __str__(self):
        return '{} {}: {}'.format(self.mcode, self.sa_type, self.tot_pv)

