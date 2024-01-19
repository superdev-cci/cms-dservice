from django.db import models


class Branch(models.Model):
    inv_code = models.CharField(max_length=7, blank=True, null=True)
    inv_desc = models.CharField(max_length=50, blank=True, null=True)
    inv_type = models.IntegerField(default=1)
    code_ref = models.CharField(max_length=20)
    address = models.TextField()
    districtid = models.IntegerField(db_column='districtId')  # Field name made lowercase.
    amphurid = models.IntegerField(db_column='amphurId')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='provinceId')  # Field name made lowercase.
    zip = models.CharField(max_length=5)
    sub_district = models.CharField(max_length=32, blank=True)
    district = models.CharField(max_length=32, blank=True)
    province = models.CharField(max_length=32, blank=True)
    post_code = models.CharField(max_length=8, blank=True)
    home_t = models.CharField(max_length=255)
    uid = models.IntegerField()
    sync = models.CharField(max_length=1, blank=True, null=True)
    web = models.CharField(max_length=1, blank=True, null=True)
    ewallet = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    voucher = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bewallet = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bvoucher = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    locationbase = models.IntegerField(default=1)
    bill_ref = models.CharField(max_length=50)
    fax = models.CharField(max_length=10, null=True, blank=True)
    no_tax = models.CharField(max_length=10, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    branch_number = models.CharField(null=True, blank=True, max_length=16)

    class Meta:
        db_table = 'ali_invent'

    def __str__(self):
        return self.code

    @property
    def code(self):
        return self.inv_code

    @property
    def name(self):
        return self.inv_desc
