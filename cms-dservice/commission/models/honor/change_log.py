from django.db import models


class HonorChangeLog(models.Model):
    level_ref = {
        'PE': 1,
        'SE': 2,
        'EE': 3,
        'DE': 4,
        'CE': 5
    }

    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    pos_before = models.CharField(max_length=11, blank=True, null=True)
    pos_after = models.CharField(max_length=11, blank=True, null=True)
    date_change = models.DateField(blank=True, null=True)
    date_update = models.DateField()
    type = models.CharField(max_length=255)
    pvleft = models.DecimalField(max_digits=15, decimal_places=2)
    pvright = models.DecimalField(max_digits=15, decimal_places=2)
    dpvleft = models.IntegerField()
    dpvright = models.IntegerField()
    uid = models.CharField(max_length=255)
    status = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'ali_calc_poschange2'

    @property
    def is_moving_up(self):
        before = self.level_ref.get(self.pos_before)
        after = self.level_ref.get(self.pos_after)
        if before:
            if after > before:
                return True
            else:
                return True
        else:
            return True

    @property
    def first_honor(self):
        before = self.level_ref.get(self.pos_before)
        if before:
            return False
        else:
            return True
