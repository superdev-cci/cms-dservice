from django.db import models


class WeakStrongStack(models.Model):
    rcode = models.IntegerField()
    sano = models.CharField(max_length=50)
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    lr = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2)
    gpv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=10)
    sa_type = models.CharField(max_length=10)
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        db_table = 'ali_bm'


class WeakStrongCurrentRoundStack(models.Model):
    rcode = models.IntegerField()
    sano = models.CharField(max_length=50)
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    lr = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2)
    gpv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=10)
    sa_type = models.CharField(max_length=10)
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        db_table = 'ali_bm1'
    
    def __str__(self):
        return '{} {} {}: PV {}'.format(self.mcode, self.upa_code, self.level, self.pv)


class WeakStrongSummary(models.Model):
    cid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=9)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    member_name = models.CharField(max_length=255, db_column='name_t')
    current_left = models.DecimalField(max_digits=15, decimal_places=2, db_column='ro_l')
    current_right = models.DecimalField(max_digits=15, decimal_places=2, db_column='ro_c')
    ro_r = models.DecimalField(max_digits=15, decimal_places=2)
    previous_left = models.DecimalField(max_digits=15, decimal_places=2, db_column='pcrry_l')
    previous_right = models.DecimalField(max_digits=15, decimal_places=2, db_column='pcrry_c')
    pquota = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_ll = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_rr = models.DecimalField(max_digits=15, decimal_places=2)
    total_left = models.DecimalField(max_digits=15, decimal_places=2, db_column='total_pv_l')
    total_right = models.DecimalField(max_digits=15, decimal_places=2, db_column='total_pv_r')
    remaining_left = models.DecimalField(max_digits=15, decimal_places=2, db_column='carry_l')
    remaining_right = models.IntegerField(db_column='carry_c')
    carry_r = models.IntegerField()
    quota = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    percer = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    totalamt = models.DecimalField(max_digits=15, decimal_places=2)
    paydate = models.DateField()
    current_pos = models.CharField(max_length=10, blank=True, null=True, db_column='mpos')
    end_date = models.DateField(db_column='tdate')
    date_issue = models.DateField(db_column='fdate')
    pair_stop = models.DecimalField(max_digits=15, decimal_places=2)
    point = models.IntegerField()
    status = models.CharField(max_length=255)
    adjust = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    cycle_b = models.IntegerField()
    locationbase = models.IntegerField()
    crate = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        db_table = 'ali_bmbonus'

    @property
    def ws_factor(self):
        return self.percer

    @property
    def weak_team(self):
        data = {
            'value': 0,
            'dir': 'L'
        }
        if self.total_left > self.total_right:
            data['value'] = self.total_left
            return data
        elif self.total_left < self.total_right:
            data['value'] = self.total_right
            data['dir'] = 'R'
            return data

        last_record = WeakStrongCurrentRoundStack.objects.filter(rcode__lt=self.rcode, mcode=self.mcode)\
            .order_by('-rcode').first()

        if last_record:
            return last_record.weak_team

        return data