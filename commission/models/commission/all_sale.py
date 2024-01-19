from django.db import models


class AllSaleBonusDetail(models.Model):
    round = models.IntegerField(db_column='rcode')
    mcode = models.CharField(max_length=255)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    current_position = models.CharField(max_length=255, db_column='mpos')
    name_t = models.CharField(max_length=255)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    share = models.IntegerField()
    percer = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    pe_bonus = models.DecimalField(max_digits=15, decimal_places=2, db_column='total1')
    se_bonus = models.DecimalField(max_digits=15, decimal_places=2, db_column='total2')
    ee_bonus = models.DecimalField(max_digits=15, decimal_places=2, db_column='total3')
    de_bonus = models.DecimalField(max_digits=15, decimal_places=2, db_column='total4')
    ce_bonus = models.DecimalField(max_digits=15, decimal_places=2, db_column='total5')
    total6 = models.DecimalField(max_digits=15, decimal_places=2)
    pershare = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, db_column='pv_world')
    pools = models.IntegerField()
    qualified_position = models.CharField(max_length=255, db_column='pos_cur')
    pos_cur1 = models.CharField(max_length=255)
    weak = models.DecimalField(max_digits=15, decimal_places=2)
    oon = models.IntegerField()
    exp = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'ali_em'
        verbose_name = 'Allsale detail'


class AllSaleBonus(models.Model):
    level_ref = {
        'PE': 1,
        'SE': 2,
        'EE': 3,
        'DE': 4,
        'CE': 5
    }

    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    current_position = models.CharField(max_length=255, db_column='mpos')
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    total2 = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    oon = models.IntegerField()
    bonus = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    qualified_position = models.CharField(max_length=10, db_column='pos_cur')

    adjust = models.DecimalField(max_digits=15, decimal_places=2)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()
    pos_cur1 = models.CharField(max_length=255)
    weak = models.DecimalField(max_digits=15, decimal_places=2)
    pv_world = models.DecimalField(max_digits=15, decimal_places=2)
    allsumpv_cd = models.DecimalField(max_digits=15, decimal_places=2)
    allsumpv_sd = models.DecimalField(max_digits=15, decimal_places=2)
    sumpv_cd = models.DecimalField(max_digits=15, decimal_places=2)
    sumpv_sd = models.DecimalField(max_digits=15, decimal_places=2)
    exp = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'ali_embonus'
        verbose_name = 'All Sale bonus'

    def __str__(self):
        return '{} {}:{} -> Current: {}, Qualified: {} '.format(self.fdate.strftime('%b'),
                                                                self.mcode, self.name_t, self.current_position,
                                                                self.qualified_position)

    @property
    def is_moving_up(self):
        current = self.level_ref.get(self.current_position)
        next_position = self.level_ref.get(self.qualified_position)
        if current:
            if next_position > current:
                return True
        return False

    @property
    def is_qualified(self):
        current = self.level_ref.get(self.current_position)
        next_position = self.level_ref.get(self.qualified_position)
        if next_position >= current:
            return True
        else:
            return False

    @property
    def member_name(self):
        return self.name_t

