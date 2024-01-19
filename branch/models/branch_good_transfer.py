from django.db import models


class BranchGoodTransferItem(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    # invoice = models.ForeignKey('BranchGoodTransfer', on_delete=models.CASCADE, null=True, blank=True,
    #                             related_name='items')
    # bill instance
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=7, blank=True, null=True)
    # branch = models.ForeignKey('Branch', on_delete=models.CASCADE, null=True, blank=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    # product = models.ForeignKey('ecommerce.Product', on_delete=models.CASCADE, null=True, blank=True,
    #                             related_name='stocks')
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    mcode = models.CharField(max_length=7, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    uidbase = models.CharField(max_length=255, blank=True, null=True)
    locationbase = models.IntegerField(default=1)
    outstanding = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ali_isaled'


class BranchGoodTransfer(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, db_column='name_t')
    sadate = models.DateField(blank=True, null=True)
    sctime = models.DateTimeField()
    to_branch = models.CharField(max_length=255, blank=True, null=True, db_column='inv_code')
    lid = models.CharField(max_length=255, blank=True, null=True)
    from_branch = models.CharField(max_length=255, db_column='inv_from', blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.CharField(max_length=1, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    create_by = models.CharField(max_length=255, db_column='uid')
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField(blank=True, null=True)
    txtoption = models.TextField(blank=True, null=True)
    chkcash = models.CharField(db_column='chkCash', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtcash = models.CharField(db_column='txtCash', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtfuture = models.CharField(db_column='txtFuture', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txttransfer = models.CharField(db_column='txtTransfer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    txtcredit1 = models.CharField(db_column='txtCredit1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtcredit2 = models.CharField(db_column='txtCredit2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtcredit3 = models.CharField(db_column='txtCredit3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtinternet = models.CharField(db_column='txtInternet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtdiscount = models.CharField(db_column='txtDiscount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txtother = models.CharField(db_column='txtOther', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(blank=True, null=True)
    send_status = models.IntegerField(db_column='sender', blank=True, null=True)
    send_date = models.DateField(db_column='sender_date', blank=True, null=True)
    receive_status = models.IntegerField(db_column='receive', blank=True, null=True)
    receive_date = models.DateField(blank=True, null=True)
    print = models.IntegerField(blank=True, null=True)
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ewallett_before = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ewallett_after = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cancel_date = models.DateField(blank=True, null=True)
    uid_cancel = models.CharField(max_length=255, blank=True, null=True)
    mbase = models.CharField(max_length=255, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    locationbase = models.IntegerField(blank=True, null=True)
    crate = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    checkportal = models.IntegerField(blank=True, null=True)
    receive_by = models.CharField(max_length=255, db_column='uid_receive', blank=True, null=True)
    sender_by = models.CharField(max_length=255, db_column='uid_sender', blank=True, null=True)
    caddress = models.TextField(blank=True, null=True)
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255)  # Field name made lowercase.
    czip = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ali_isaleh',
        ordering = ('id', 'sctime')
        managed = False
