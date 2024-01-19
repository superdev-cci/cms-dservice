from django.db import models


class PositionChangeLog(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=20)
    pos_before = models.CharField(max_length=11, blank=True, null=True)
    pos_after = models.CharField(max_length=11, blank=True, null=True)
    date_change = models.DateField(blank=True, null=True)
    date_update = models.DateField()
    type = models.CharField(max_length=255)
    up_down = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'ali_calc_poschange'
