# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AliAdjust(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.CharField(max_length=1, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtmoney = models.CharField(db_column='txtMoney', max_length=255)  # Field name made lowercase.
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    txtoption = models.TextField()
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    chkcommission = models.DecimalField(db_column='chkCommission', max_digits=15, decimal_places=2)  # Field name made lowercase.
    mbase = models.CharField(max_length=244)
    crate = models.DecimalField(max_digits=11, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'ali_adjust'


class AliAging(models.Model):
    pcode = models.CharField(max_length=255)
    intime = models.DateTimeField()
    outtime = models.DateTimeField()
    serial = models.CharField(max_length=255)
    fdate = models.DateField()
    tdate = models.DateField()
    barcode = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)
    sano = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255)
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_aging'


class AliApv(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_apv'


class AliAround(models.Model):
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
    total_a = models.DecimalField(max_digits=15, decimal_places=2)
    total_h = models.DecimalField(max_digits=15, decimal_places=2)
    fast = models.DecimalField(max_digits=15, decimal_places=2)
    invent = models.DecimalField(max_digits=15, decimal_places=2)
    binaryt = models.DecimalField(max_digits=15, decimal_places=2)
    matching = models.DecimalField(max_digits=15, decimal_places=2)
    pool = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_binary = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_matching = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_pool = models.DecimalField(max_digits=15, decimal_places=2)
    timequery = models.IntegerField()
    countquery = models.IntegerField()
    uid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_around'


class AliAsaled(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    customer_price = models.DecimalField(max_digits=15, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sppv = models.DecimalField(max_digits=15, decimal_places=2)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    weight = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    uidbase = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    outstanding = models.CharField(max_length=255)
    vat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_asaled'


class AliAsaleh(models.Model):
    sano = models.CharField(max_length=255)
    pano = models.CharField(max_length=255)
    sadate = models.CharField(max_length=255)
    sctime = models.DateTimeField()
    inv_code = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    sp_pos = models.CharField(max_length=10)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    total_vat = models.DecimalField(max_digits=15, decimal_places=2)
    total_net = models.DecimalField(max_digits=15, decimal_places=2)
    total_invat = models.DecimalField(max_digits=15, decimal_places=2)
    total_exvat = models.DecimalField(max_digits=15, decimal_places=2)
    customer_total = models.DecimalField(max_digits=15, decimal_places=2)
    tot_pv = models.CharField(max_length=255)
    tot_bv = models.CharField(max_length=255)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    tot_sppv = models.DecimalField(max_digits=15, decimal_places=2)
    tot_weight = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    uid_branch = models.CharField(max_length=20)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtoption = models.TextField()
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkcredit4 = models.CharField(db_column='chkCredit4', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit4 = models.DecimalField(db_column='txtCredit4', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtinternet = models.DecimalField(db_column='txtInternet', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtdiscount = models.DecimalField(db_column='txtDiscount', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtother = models.DecimalField(db_column='txtOther', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtsending = models.DecimalField(db_column='txtSending', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioncredit4 = models.CharField(db_column='optionCredit4', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255)  # Field name made lowercase.
    discount = models.CharField(max_length=255)
    print = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    hcancel = models.IntegerField()
    caddress = models.TextField()
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255)  # Field name made lowercase.
    czip = models.CharField(max_length=255)
    sender = models.IntegerField()
    sender_date = models.DateField()
    receive = models.IntegerField()
    receive_date = models.DateField()
    asend = models.IntegerField()
    ato_type = models.IntegerField()
    ato_id = models.IntegerField()
    online = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    htotal = models.DecimalField(max_digits=15, decimal_places=2)
    hdate = models.DateField()
    scheck = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    rcode = models.IntegerField()
    bmcauto = models.IntegerField()
    cancel_date = models.DateTimeField()
    uid_cancel = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    cmobile = models.CharField(max_length=255)
    uid_sender = models.CharField(max_length=255)
    uid_receive = models.CharField(max_length=255)
    mbase = models.CharField(max_length=255)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    locationbase = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    status = models.IntegerField()
    ref = models.CharField(max_length=100)
    selectcash = models.CharField(db_column='selectCash', max_length=255)  # Field name made lowercase.
    selecttransfer = models.CharField(db_column='selectTransfer', max_length=255)  # Field name made lowercase.
    selectcredit1 = models.CharField(db_column='selectCredit1', max_length=255)  # Field name made lowercase.
    selectcredit2 = models.CharField(db_column='selectCredit2', max_length=255)  # Field name made lowercase.
    selectcredit3 = models.CharField(db_column='selectCredit3', max_length=255)  # Field name made lowercase.
    selectdiscount = models.CharField(db_column='selectDiscount', max_length=255)  # Field name made lowercase.
    selectinternet = models.CharField(db_column='selectInternet', max_length=255)  # Field name made lowercase.
    txtvoucher = models.DecimalField(db_column='txtVoucher', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optionvoucher = models.CharField(db_column='optionVoucher', max_length=255)  # Field name made lowercase.
    selectvoucher = models.CharField(db_column='selectVoucher', max_length=255)  # Field name made lowercase.
    txttransfer1 = models.CharField(db_column='txtTransfer1', max_length=255)  # Field name made lowercase.
    optiontransfer1 = models.CharField(db_column='optionTransfer1', max_length=255)  # Field name made lowercase.
    selecttransfer1 = models.CharField(db_column='selectTransfer1', max_length=255)  # Field name made lowercase.
    txttransfer2 = models.CharField(db_column='txtTransfer2', max_length=255)  # Field name made lowercase.
    optiontransfer2 = models.CharField(db_column='optionTransfer2', max_length=255)  # Field name made lowercase.
    selecttransfer2 = models.CharField(db_column='selectTransfer2', max_length=255)  # Field name made lowercase.
    txttransfer3 = models.CharField(db_column='txtTransfer3', max_length=255)  # Field name made lowercase.
    optiontransfer3 = models.CharField(db_column='optionTransfer3', max_length=255)  # Field name made lowercase.
    selecttransfer3 = models.CharField(db_column='selectTransfer3', max_length=255)  # Field name made lowercase.
    status_package = models.IntegerField()
    txtpremium = models.DecimalField(db_column='txtPremium', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chkpremium = models.CharField(db_column='chkPremium', max_length=8, blank=True, null=True)  # Field name made lowercase.
    selectpremium = models.CharField(db_column='selectPremium', max_length=8, blank=True, null=True)  # Field name made lowercase.
    optionpremium = models.CharField(db_column='optionPremium', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ali_asaleh'


class AliAtoasaled(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    customer_price = models.DecimalField(max_digits=15, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sppv = models.DecimalField(max_digits=15, decimal_places=2)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    weight = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    uidbase = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    outstanding = models.CharField(max_length=255)
    vat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_atoasaled'


class AliAtoasaleh(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    pano = models.CharField(max_length=255)
    sadate = models.DateField(blank=True, null=True)
    sctime = models.DateTimeField()
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_ref = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    sp_code = models.CharField(max_length=255)
    sp_pos = models.CharField(max_length=10)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_vat = models.DecimalField(max_digits=15, decimal_places=2)
    total_net = models.DecimalField(max_digits=15, decimal_places=2)
    total_invat = models.DecimalField(max_digits=15, decimal_places=2)
    total_exvat = models.DecimalField(max_digits=15, decimal_places=2)
    customer_total = models.DecimalField(max_digits=15, decimal_places=2)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    tot_sppv = models.DecimalField(max_digits=15, decimal_places=2)
    tot_weight = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    uid_branch = models.CharField(max_length=20)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtoption = models.TextField()
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkcredit4 = models.CharField(db_column='chkCredit4', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit4 = models.DecimalField(db_column='txtCredit4', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtinternet = models.DecimalField(db_column='txtInternet', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtdiscount = models.DecimalField(db_column='txtDiscount', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtother = models.DecimalField(db_column='txtOther', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioncredit4 = models.CharField(db_column='optionCredit4', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255)  # Field name made lowercase.
    discount = models.CharField(max_length=255)
    print = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    hcancel = models.IntegerField()
    caddress = models.TextField()
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255)  # Field name made lowercase.
    czip = models.CharField(max_length=255)
    sender = models.IntegerField()
    sender_date = models.DateField()
    receive = models.IntegerField()
    receive_date = models.DateField()
    asend = models.IntegerField()
    ato_type = models.IntegerField()
    ato_id = models.IntegerField()
    online = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    htotal = models.DecimalField(max_digits=15, decimal_places=2)
    hdate = models.DateField()
    scheck = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    rcode = models.IntegerField()
    bmcauto = models.IntegerField()
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    cmobile = models.CharField(max_length=255)
    uid_sender = models.CharField(max_length=255)
    uid_receive = models.CharField(max_length=255)
    mbase = models.CharField(max_length=255)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    locationbase = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_atoasaleh'


class AliAutocals(models.Model):
    cid = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_autocals'


class AliBank(models.Model):
    bankcode = models.CharField(primary_key=True, max_length=255)
    bankname = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_bank'


class AliBankNew(models.Model):
    bankcode = models.AutoField(primary_key=True)
    bankname = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=255)
    uid = models.CharField(max_length=1, blank=True, null=True)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_bank_new'


class AliBankOld(models.Model):
    bankcode = models.AutoField(primary_key=True)
    bankname = models.CharField(max_length=25, blank=True, null=True)
    code = models.CharField(max_length=255)
    uid = models.CharField(max_length=1, blank=True, null=True)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_bank_old'


class AliBbuy(models.Model):
    bbuy_id = models.AutoField(db_column='bbuy_ID', primary_key=True)  # Field name made lowercase.
    bbuy_date = models.DateField(db_column='bbuy_Date')  # Field name made lowercase.
    pcode = models.CharField(max_length=255)
    bbuy_qua = models.IntegerField(db_column='bbuy_Qua')  # Field name made lowercase.
    bbuy_balance = models.IntegerField(db_column='bbuy_Balance')  # Field name made lowercase.
    txtoption = models.TextField()

    class Meta:
        managed = False
        db_table = 'ali_bbuy'


class AliBc(models.Model):
    bid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=7)
    upa_code = models.CharField(max_length=7, blank=True, null=True)
    rol_l = models.DecimalField(max_digits=15, decimal_places=2)
    rol_r = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_bc'


class AliBinaryNewpoint(models.Model):
    mcode = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    mdate = models.DateField()
    name_t = models.CharField(max_length=255)
    point_left = models.DecimalField(max_digits=15, decimal_places=2)
    point_right = models.DecimalField(max_digits=15, decimal_places=2)
    point_all = models.DecimalField(max_digits=15, decimal_places=2)
    uid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_binary_newpoint'


class AliBinaryReport(models.Model):
    mcode = models.CharField(max_length=255)
    mdate = models.DateField()
    id = models.BigAutoField(primary_key=True)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fast = models.DecimalField(max_digits=15, decimal_places=2)
    weakstrong = models.DecimalField(max_digits=15, decimal_places=2)
    matching = models.DecimalField(max_digits=15, decimal_places=2)
    upa_code = models.CharField(max_length=255)
    upa_name = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    sp_name = models.CharField(max_length=255)
    lv = models.IntegerField()
    lv_sp = models.IntegerField()
    lr = models.IntegerField()
    pos_cur = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=10)
    uid = models.CharField(max_length=255)
    totpv = models.DecimalField(max_digits=15, decimal_places=2)
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    thismonth = models.DecimalField(max_digits=15, decimal_places=2)
    nextmonth = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_binary_report'

class AliBm2(models.Model):
    rcode = models.IntegerField()
    sano = models.CharField(max_length=50)
    mcode = models.CharField(max_length=255)
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
        managed = False
        db_table = 'ali_bm2'


class AliBmbonusNew(models.Model):
    cid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=7)
    ro_l = models.DecimalField(max_digits=15, decimal_places=2)
    ro_c = models.DecimalField(max_digits=15, decimal_places=2)
    ro_r = models.DecimalField(max_digits=15, decimal_places=2)
    pcrry_l = models.DecimalField(max_digits=15, decimal_places=2)
    ccpcrry_l = models.CharField(max_length=255)
    ccpcrry_c = models.CharField(max_length=255)
    pcrry_c = models.DecimalField(max_digits=15, decimal_places=2)
    pcrry_r = models.DecimalField(max_digits=15, decimal_places=2)
    pquota = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_ll = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_rr = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_l = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_r = models.DecimalField(max_digits=15, decimal_places=2)
    count_l = models.DecimalField(max_digits=15, decimal_places=0)
    count_c = models.DecimalField(max_digits=15, decimal_places=0)
    count_r = models.DecimalField(max_digits=15, decimal_places=0)
    carry_l = models.DecimalField(max_digits=15, decimal_places=2)
    carry_c = models.DecimalField(max_digits=15, decimal_places=2)
    carry_r = models.DecimalField(max_digits=15, decimal_places=2)
    quota = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    percer = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    totalamt = models.DecimalField(max_digits=15, decimal_places=2)
    paydate = models.DateField()
    mpos = models.CharField(max_length=10, blank=True, null=True)
    tdate = models.DateField()
    fdate = models.DateField()
    pair_stop = models.DecimalField(max_digits=15, decimal_places=2)
    point = models.IntegerField()
    pos_cur = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    adjust = models.DecimalField(max_digits=15, decimal_places=2)
    total_cmt_weak = models.DecimalField(max_digits=15, decimal_places=2)
    total_cmt_strong = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    cycle_b = models.IntegerField()
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_bmbonus_new'


class AliBmnew(models.Model):
    carry_l = models.IntegerField()
    carry_c = models.IntegerField()
    mcode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_bmnew'


class AliBround(models.Model):
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


class AliCalcPoschange1(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    pos_before = models.CharField(max_length=11, blank=True, null=True)
    pos_after = models.CharField(max_length=11, blank=True, null=True)
    date_change = models.DateField(blank=True, null=True)
    date_update = models.DateField()
    type = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_calc_poschange1'


class AliCalcPoschange2(models.Model):
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

    class Meta:
        managed = False
        db_table = 'ali_calc_poschange2'


class AliCalcPoschange3(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    pos_before = models.CharField(max_length=11, blank=True, null=True)
    pos_after = models.CharField(max_length=11, blank=True, null=True)
    date_change = models.DateField(blank=True, null=True)
    date_update = models.DateField()
    type = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_calc_poschange3'



class AliCc(models.Model):
    bid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=7)
    upa_code = models.CharField(max_length=7, blank=True, null=True)
    rol_l = models.DecimalField(max_digits=15, decimal_places=2)
    rol_r = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_cc'


class AliCheckdownline(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fast = models.DecimalField(max_digits=15, decimal_places=2)
    weakstrong = models.DecimalField(max_digits=15, decimal_places=2)
    matching = models.DecimalField(max_digits=15, decimal_places=2)
    star = models.DecimalField(max_digits=15, decimal_places=2)
    onetime = models.DecimalField(max_digits=15, decimal_places=2)
    alltotal = models.DecimalField(max_digits=15, decimal_places=2)
    upa_code = models.CharField(max_length=255)
    lv = models.IntegerField()
    lr = models.IntegerField()
    mdate = models.DateField(blank=True, null=True)
    id_card = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_checkdownline'


class AliCheckdownlineSp(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fast = models.DecimalField(max_digits=15, decimal_places=2)
    weakstrong = models.DecimalField(max_digits=15, decimal_places=2)
    matching = models.DecimalField(max_digits=15, decimal_places=2)
    star = models.DecimalField(max_digits=15, decimal_places=2)
    onetime = models.DecimalField(max_digits=15, decimal_places=2)
    alltotal = models.DecimalField(max_digits=15, decimal_places=2)
    upa_code = models.CharField(max_length=255)
    lv = models.IntegerField()
    lr = models.IntegerField()
    mdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_checkdownline_sp'


class AliCm(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=20)
    upa_code = models.CharField(max_length=20, blank=True, null=True)
    lr = models.IntegerField(blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    gpv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=10)
    npos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'ali_cm'






class AliCpv(models.Model):
    bid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=5, blank=True, null=True)
    npos = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_cpv'


class AliCron(models.Model):
    cron_detail = models.CharField(max_length=255)
    cron_date = models.DateTimeField()
    rcode = models.IntegerField()
    httppost = models.CharField(max_length=255)
    requesturl = models.CharField(max_length=255)
    phpself = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_cron'


class AliCronjob(models.Model):
    cstatus = models.IntegerField()
    ctype = models.IntegerField()
    cfdate = models.DateField()
    ctdate = models.DateField()
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ali_cronjob'


class AliCround(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    cstatus = models.IntegerField()
    rdate = models.DateField(blank=True, null=True)
    fsano = models.CharField(max_length=7, blank=True, null=True)
    tsano = models.CharField(max_length=7, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()
    fpdate = models.DateField()
    tpdate = models.DateField()
    total_a = models.DecimalField(max_digits=15, decimal_places=2)
    total_h = models.DecimalField(max_digits=15, decimal_places=2)
    fast = models.DecimalField(max_digits=15, decimal_places=2)
    invent = models.DecimalField(max_digits=15, decimal_places=2)
    binaryt = models.DecimalField(max_digits=15, decimal_places=2)
    matching = models.DecimalField(max_digits=15, decimal_places=2)
    pool = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_binary = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_matching = models.DecimalField(max_digits=15, decimal_places=2)
    adjust_pool = models.DecimalField(max_digits=15, decimal_places=2)
    calc_date = models.DateTimeField()
    timequery = models.IntegerField()
    uid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_cround'


class AliCround1(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)
    fsano = models.CharField(max_length=7, blank=True, null=True)
    tsano = models.CharField(max_length=7, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()
    fpdate = models.DateField()
    tpdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_cround1'


class AliDpv(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_dpv'


class AliDround(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)
    fsano = models.CharField(max_length=7, blank=True, null=True)
    tsano = models.CharField(max_length=7, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()
    fpdate = models.DateField()
    tpdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_dround'




class AliEc(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    point = models.DecimalField(max_digits=15, decimal_places=0)
    share = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    pershare = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    pos_cur = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_ec'


class AliEcom(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    rcode = models.IntegerField()
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=255)
    trnf = models.CharField(max_length=1, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtmoney = models.DecimalField(db_column='txtMoney', max_digits=15, decimal_places=2)  # Field name made lowercase.
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=100)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkwithdraw = models.CharField(db_column='chkWithdraw', max_length=255)  # Field name made lowercase.
    chktransfer_in = models.CharField(db_column='chkTransfer_in', max_length=255)  # Field name made lowercase.
    chktransfer_out = models.CharField(db_column='chkTransfer_out', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtinternet = models.DecimalField(db_column='txtInternet', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtwithdraw = models.DecimalField(db_column='txtWithdraw', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer_in = models.DecimalField(db_column='txtTransfer_in', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer_out = models.DecimalField(db_column='txtTransfer_out', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optionwithdraw = models.CharField(db_column='optionWithdraw', max_length=255)  # Field name made lowercase.
    optiontransfer_in = models.CharField(db_column='optionTransfer_in', max_length=255)  # Field name made lowercase.
    optiontransfer_out = models.CharField(db_column='optionTransfer_out', max_length=255)  # Field name made lowercase.
    txtoption = models.TextField()
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    chkcommission = models.CharField(db_column='chkCommission', max_length=255)  # Field name made lowercase.
    txtcommission = models.DecimalField(db_column='txtCommission', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncommission = models.CharField(db_column='optionCommission', max_length=255)  # Field name made lowercase.
    mbase = models.CharField(max_length=244)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    echeck = models.CharField(max_length=255)
    sano_temp = models.CharField(max_length=255)
    selectcash = models.CharField(db_column='selectCash', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selecttransfer = models.CharField(db_column='selectTransfer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selectcredit1 = models.CharField(db_column='selectCredit1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selectcredit2 = models.CharField(db_column='selectCredit2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selectcredit3 = models.CharField(db_column='selectCredit3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selectinternet = models.CharField(db_column='selectInternet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txttransfer1 = models.DecimalField(db_column='txtTransfer1', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    optiontransfer1 = models.CharField(db_column='optionTransfer1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selecttransfer1 = models.CharField(db_column='selectTransfer1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txttransfer2 = models.DecimalField(db_column='txtTransfer2', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    optiontransfer2 = models.CharField(db_column='optionTransfer2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selecttransfer2 = models.CharField(db_column='selectTransfer2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txttransfer3 = models.DecimalField(db_column='txtTransfer3', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    optiontransfer3 = models.CharField(db_column='optionTransfer3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selecttransfer3 = models.CharField(db_column='selectTransfer3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image_transfer = models.TextField()
    txtvoucher = models.DecimalField(db_column='txtVoucher', max_digits=15, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ali_ecom'


class AliEcommision(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    rcode = models.IntegerField()
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.CharField(max_length=1, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtmoney = models.DecimalField(db_column='txtMoney', max_digits=15, decimal_places=2)  # Field name made lowercase.
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkwithdraw = models.CharField(db_column='chkWithdraw', max_length=255)  # Field name made lowercase.
    chktransfer_in = models.CharField(db_column='chkTransfer_in', max_length=255)  # Field name made lowercase.
    chktransfer_out = models.CharField(db_column='chkTransfer_out', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtwithdraw = models.DecimalField(db_column='txtWithdraw', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer_in = models.DecimalField(db_column='txtTransfer_in', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer_out = models.DecimalField(db_column='txtTransfer_out', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optionwithdraw = models.CharField(db_column='optionWithdraw', max_length=255)  # Field name made lowercase.
    optiontransfer_in = models.CharField(db_column='optionTransfer_in', max_length=255)  # Field name made lowercase.
    optiontransfer_out = models.CharField(db_column='optionTransfer_out', max_length=255)  # Field name made lowercase.
    txtoption = models.TextField()
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    chkcommission = models.CharField(db_column='chkCommission', max_length=255)  # Field name made lowercase.
    txtcommission = models.DecimalField(db_column='txtCommission', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncommission = models.CharField(db_column='optionCommission', max_length=255)  # Field name made lowercase.
    status_tranfer = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    echeck = models.CharField(max_length=255)
    cmbonus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_ecommision'


class AliEd(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    pv = models.FloatField()
    fdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_ed'


class AliEpv(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_epv'


class AliEsaled(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    mcode = models.CharField(max_length=7, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_esaled'


class AliEsaleh(models.Model):
    sano = models.BigIntegerField(blank=True, null=True)
    sano1 = models.BigIntegerField()
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_ref = models.CharField(max_length=255)
    mcode = models.CharField(max_length=20, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtoption = models.TextField()
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255)  # Field name made lowercase.
    txtcash = models.CharField(db_column='txtCash', max_length=255)  # Field name made lowercase.
    txtfuture = models.CharField(db_column='txtFuture', max_length=255)  # Field name made lowercase.
    txttransfer = models.CharField(db_column='txtTransfer', max_length=255)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    txtcredit1 = models.CharField(db_column='txtCredit1', max_length=255)  # Field name made lowercase.
    txtcredit2 = models.CharField(db_column='txtCredit2', max_length=255)  # Field name made lowercase.
    txtcredit3 = models.CharField(db_column='txtCredit3', max_length=255)  # Field name made lowercase.
    txtinternet = models.CharField(db_column='txtInternet', max_length=255)  # Field name made lowercase.
    txtdiscount = models.CharField(db_column='txtDiscount', max_length=255)  # Field name made lowercase.
    txtother = models.CharField(db_column='txtOther', max_length=255)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255)  # Field name made lowercase.
    asend = models.IntegerField()
    asend_date = models.DateField()
    discount = models.CharField(max_length=255)
    status = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ewallett_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallett_after = models.DecimalField(max_digits=15, decimal_places=2)
    print = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_esaleh'



class AliEwalletd(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.CharField(max_length=1, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtmoney = models.DecimalField(db_column='txtMoney', max_digits=15, decimal_places=2)  # Field name made lowercase.
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkcommission = models.CharField(db_column='chkCommission', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtinternet = models.DecimalField(db_column='txtInternet', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcommission = models.DecimalField(db_column='txtCommission', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optioncommission = models.CharField(db_column='optionCommission', max_length=255)  # Field name made lowercase.
    txtoption = models.TextField()
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    mbase = models.CharField(max_length=244)
    crate = models.DecimalField(max_digits=11, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'ali_ewalletd'


class AliExpdate(models.Model):
    mid = models.IntegerField()
    exp_date = models.DateField()
    date_change = models.DateField(blank=True, null=True)
    exp_type = models.CharField(max_length=255, blank=True, null=True)
    sano = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_expdate'


class AliFc(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
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
    total_r = models.DecimalField(max_digits=15, decimal_places=2)
    ctax = models.DecimalField(max_digits=15, decimal_places=2)
    cvat = models.DecimalField(max_digits=15, decimal_places=2)
    amt = models.DecimalField(max_digits=15, decimal_places=2)
    oon = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    pos_cur = models.CharField(max_length=255)
    crate = models.IntegerField()
    locationbase = models.IntegerField()
    sano = models.CharField(max_length=255)
    pcode = models.CharField(max_length=255)
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_fc'


class AliFm(models.Model):
    rcode = models.IntegerField()
    inv_code = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    sano = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sa_type = models.CharField(max_length=255)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mdate = models.DateField()
    crate = models.IntegerField()
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_fm'


class AliFmbonus(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    total_r = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    bonus = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    pos_cur = models.CharField(max_length=255)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()
    paydate = models.DateField()
    inv_code = models.CharField(max_length=255)
    paytype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_fmbonus'


class AliFpv(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=255, blank=True, null=True)
    npos = models.CharField(max_length=5, blank=True, null=True)
    crate = models.IntegerField()
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_fpv'


class AliFround(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)
    fsano = models.CharField(max_length=7, blank=True, null=True)
    tsano = models.CharField(max_length=7, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()
    fpdate = models.DateField()
    tpdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_fround'


class AliGlobal(models.Model):
    numofchild = models.IntegerField()
    treeformat = models.CharField(max_length=50)
    numoflevel = models.IntegerField()
    statusformat = models.CharField(max_length=255)
    status_member = models.IntegerField()
    status_member_remark = models.CharField(max_length=255)
    status_regis_mb = models.IntegerField()
    status_regis_mb_remark = models.CharField(max_length=255)
    status_sale_mb = models.IntegerField()
    status_sale_mb_remark = models.CharField(max_length=255)
    status_swap_mb = models.IntegerField()
    status_swap_mb_remark = models.CharField(max_length=255)
    status_hold_mb = models.IntegerField()
    status_hold_mb_remark = models.CharField(max_length=255)
    status_remark = models.CharField(max_length=255)
    statusewallet = models.CharField(max_length=255)
    vip_exp = models.IntegerField()
    status_cron = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_global'


class AliGmbonus(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    fast_bonus = models.DecimalField(max_digits=15, decimal_places=2)
    cycle_bonus = models.DecimalField(max_digits=15, decimal_places=2)
    matching_bonus = models.DecimalField(max_digits=15, decimal_places=2)
    key_bonus = models.DecimalField(max_digits=15, decimal_places=2)
    autoship = models.DecimalField(max_digits=15, decimal_places=2)
    rcode = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()
    beatoship = models.DecimalField(max_digits=15, decimal_places=2)
    bvoucher = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_gmbonus'


class AliHolddesc(models.Model):
    hono = models.IntegerField(blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    sppv = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    uidbase = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    vat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_holddesc'


class AliImportStockD(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=40, blank=True, null=True)
    mcode = models.CharField(max_length=7, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qty_old = models.DecimalField(max_digits=15, decimal_places=2)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_import_stock_d'




class AliInvent(models.Model):
    inv_code = models.CharField(max_length=7, blank=True, null=True)
    inv_desc = models.CharField(max_length=50, blank=True, null=True)
    inv_type = models.IntegerField()
    code_ref = models.CharField(max_length=20)
    address = models.TextField()
    districtid = models.IntegerField(db_column='districtId')  # Field name made lowercase.
    amphurid = models.IntegerField(db_column='amphurId')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='provinceId')  # Field name made lowercase.
    zip = models.CharField(max_length=5)
    home_t = models.CharField(max_length=255)
    uid = models.IntegerField()
    sync = models.CharField(max_length=1, blank=True, null=True)
    web = models.CharField(max_length=1, blank=True, null=True)
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    voucher = models.DecimalField(max_digits=15, decimal_places=2)
    bewallet = models.DecimalField(max_digits=15, decimal_places=2)
    bvoucher = models.DecimalField(max_digits=15, decimal_places=2)
    discount = models.IntegerField()
    locationbase = models.IntegerField()
    bill_ref = models.CharField(max_length=50)
    fax = models.CharField(max_length=10)
    no_tax = models.CharField(max_length=10)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_invent'


class AliInventoryOrder(models.Model):
    mlm_inv_type = models.CharField(db_column='MLM_Inv_Type', max_length=255)  # Field name made lowercase.
    mlm_type_group = models.CharField(db_column='MLM_Type_Group', max_length=255)  # Field name made lowercase.
    oracle_type = models.CharField(db_column='Oracle_Type', max_length=255)  # Field name made lowercase.
    mapping_code = models.CharField(db_column='Mapping_Code', primary_key=True, max_length=255)  # Field name made lowercase.
    mapping_type = models.CharField(db_column='Mapping_type', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ali_inventory_order'
        unique_together = (('mapping_code', 'mapping_type'),)


class BranchGoodTransferItem(models.Model):
    sano = models.IntegerField(blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_coden = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    inv_refn = models.CharField(max_length=255)
    rccode = models.CharField(max_length=255)
    stockist = models.CharField(max_length=255)
    pcode = models.CharField(max_length=255, blank=True, null=True)
    pdesc = models.CharField(max_length=40, blank=True, null=True)
    unit = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ctax = models.IntegerField()
    group_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'ali_istockd'







class AliIstockh(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sano1 = models.CharField(max_length=255)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_coden = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    inv_refn = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    sa_mtype = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    uid_ref = models.CharField(max_length=255)
    cancel = models.IntegerField()
    txtoption = models.TextField()
    sender = models.CharField(max_length=255)
    sender_date = models.DateTimeField()
    receive = models.IntegerField()
    receive_date = models.DateTimeField()
    uid_receive = models.CharField(max_length=255)
    status = models.IntegerField()
    print = models.IntegerField()
    rccode = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    mapping_code = models.CharField(max_length=255)
    rrcode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_istockh'


class AliLocationBase(models.Model):
    cid = models.AutoField(primary_key=True)
    cshort = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    csending = models.CharField(max_length=255)
    ctax = models.DecimalField(max_digits=15, decimal_places=2)
    ctax1 = models.DecimalField(max_digits=15, decimal_places=2)
    com_stockist = models.DecimalField(max_digits=15, decimal_places=2)
    crate = models.DecimalField(max_digits=15, decimal_places=6)
    pcode_register = models.CharField(max_length=255)
    pcode_extend = models.CharField(max_length=255)
    pcode_charge = models.CharField(max_length=255)
    smssending = models.IntegerField()
    currcode = models.CharField(max_length=255)
    lang = models.CharField(max_length=255)
    timediff = models.IntegerField()
    regis_transfer = models.CharField(max_length=255)
    regis_success = models.CharField(max_length=255)
    regis_fail = models.CharField(max_length=255)
    regis_cancel = models.CharField(max_length=255)
    main_inv_code = models.CharField(max_length=255)
    com_transfer_chagre = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_location_base'


class AliLogChange(models.Model):
    rcode = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()
    mcode = models.CharField(max_length=255)
    mpos = models.CharField(max_length=50)
    status = models.CharField(max_length=2)
    pvb = models.DecimalField(max_digits=15, decimal_places=2)
    pvh = models.DecimalField(max_digits=15, decimal_places=3)
    fob = models.DecimalField(max_digits=15, decimal_places=2)
    cycle = models.DecimalField(max_digits=15, decimal_places=2)
    ambonus2 = models.DecimalField(max_digits=15, decimal_places=2)
    fmbonus = models.DecimalField(max_digits=15, decimal_places=2)
    unilevel = models.DecimalField(max_digits=15, decimal_places=2)
    adjust = models.DecimalField(max_digits=15, decimal_places=2)
    autoship = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_withdraw = models.DecimalField(max_digits=15, decimal_places=2)
    tot_tax = models.DecimalField(max_digits=15, decimal_places=2)
    pv = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=2)
    paydate = models.DateField()
    date_change = models.DateTimeField()
    com_transfer_chagre = models.IntegerField()
    uid = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ali_log_change'


class AliLogEcom(models.Model):
    mcode = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)
    sadate = models.DateField()
    satime = models.TimeField()
    sano = models.CharField(max_length=255)
    field_in = models.DecimalField(db_column='_in', max_digits=15, decimal_places=2)  # Field renamed because it started with '_'.
    field_out = models.DecimalField(db_column='_out', max_digits=15, decimal_places=2)  # Field renamed because it started with '_'.
    total = models.DecimalField(max_digits=15, decimal_places=2)
    uid = models.CharField(max_length=255)
    sa_type = models.CharField(max_length=255)
    field_option = models.CharField(db_column='_option', max_length=255)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'ali_log_ecom'


class AliLogIpay(models.Model):
    ipayorderid = models.CharField(max_length=255)
    inv_no = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    pay_method = models.CharField(max_length=255)
    resp_code = models.CharField(max_length=255)
    resp_desc = models.CharField(max_length=255)
    coupon_status = models.CharField(max_length=255)
    coupon_serial = models.CharField(max_length=255)
    coupon_password = models.CharField(max_length=255)
    coupon_ref = models.CharField(max_length=255)
    billtype = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_log_ipay'


class AliLogKtc(models.Model):
    ref1 = models.CharField(max_length=255)
    src = models.CharField(max_length=255)
    prc = models.CharField(max_length=255)
    ord = models.CharField(max_length=255)
    holder = models.CharField(max_length=255)
    successcode = models.CharField(max_length=255)
    ref2 = models.CharField(max_length=255)
    payref = models.CharField(db_column='payRef', max_length=255)  # Field name made lowercase.
    amt = models.CharField(max_length=255)
    cur = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    authid = models.CharField(db_column='authId', max_length=255)  # Field name made lowercase.
    payerauth = models.CharField(db_column='payerAuth', max_length=255)  # Field name made lowercase.
    sourcelp = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_log_ktc'


class AliLogWallet(models.Model):
    rcode = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()
    mcode = models.CharField(max_length=255)
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    evoucher = models.DecimalField(max_digits=15, decimal_places=2)
    eautoship = models.DecimalField(max_digits=15, decimal_places=2)
    ecom = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_log_wallet'


class AliLrDef(models.Model):
    lr_id = models.IntegerField()
    lr_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ali_lr_def'


class AliMc(models.Model):
    bid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
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
    checkcheck = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_mc'


class AliMember(models.Model):
    mcode = models.CharField(unique=True, max_length=255)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    name_e = models.CharField(max_length=255)
    posid = models.CharField(max_length=255)
    mdate = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    national = models.CharField(max_length=255)
    id_tax = models.CharField(max_length=255)
    id_card = models.CharField(max_length=255)
    id_card_img = models.CharField(max_length=250)
    id_card_img_date = models.DateTimeField()
    zip = models.CharField(max_length=255)
    home_t = models.CharField(max_length=255)
    office_t = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    mcode_acc = models.CharField(max_length=255)
    bonusrec = models.CharField(max_length=255)
    bankcode = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    acc_type = models.CharField(max_length=255)
    acc_no = models.CharField(max_length=255)
    acc_no_img = models.CharField(max_length=250)
    acc_no_img_date = models.DateTimeField()
    acc_name = models.CharField(max_length=255)
    acc_prov = models.CharField(max_length=255)
    sv_code = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    sp_name = models.CharField(max_length=255)
    sp_code2 = models.CharField(max_length=255)
    sp_name2 = models.CharField(max_length=255)
    upa_code = models.CharField(max_length=255)
    upa_name = models.CharField(max_length=255)
    lr = models.CharField(max_length=255)
    complete = models.CharField(max_length=255)
    compdate = models.CharField(max_length=255)
    modate = models.CharField(max_length=255)
    usercode = models.CharField(max_length=255)
    name_b = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    status = models.IntegerField()
    mar_name = models.CharField(max_length=100)
    mar_age = models.IntegerField()
    email = models.CharField(max_length=50)
    beneficiaries = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    districtid = models.CharField(db_column='districtId', max_length=255)  # Field name made lowercase.
    amphurid = models.CharField(db_column='amphurId', max_length=255)  # Field name made lowercase.
    provinceid = models.CharField(db_column='provinceId', max_length=255)  # Field name made lowercase.
    fax = models.CharField(max_length=20)
    inv_code = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    oid = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)
    pos_cur1 = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=255)
    pos_cur3 = models.CharField(max_length=255)
    pos_cur4 = models.CharField(max_length=255)
    pos_cur_tmp = models.CharField(max_length=255)
    rpos_cur4 = models.IntegerField()
    pos_cur3_date = models.DateField()
    memdesc = models.CharField(max_length=40)
    cmp = models.CharField(max_length=10)
    cmp2 = models.CharField(max_length=255)
    cmp3 = models.CharField(max_length=255)
    ccmp = models.CharField(max_length=255)
    ccmp2 = models.CharField(max_length=255)
    ccmp3 = models.CharField(max_length=255)
    address = models.TextField()
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    soi = models.CharField(max_length=255)
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    eatoship = models.DecimalField(max_digits=15, decimal_places=2)
    ecom = models.DecimalField(max_digits=15, decimal_places=2)
    bmdate1 = models.CharField(max_length=255)
    bmdate2 = models.CharField(max_length=255)
    bmdate3 = models.CharField(max_length=255)
    cbmdate1 = models.CharField(max_length=255)
    cbmdate2 = models.CharField(max_length=255)
    cbmdate3 = models.CharField(max_length=255)
    online = models.IntegerField()
    cname_f = models.CharField(max_length=255)
    cname_t = models.CharField(max_length=255)
    cname_e = models.CharField(max_length=255)
    cname_b = models.CharField(max_length=255)
    cbirthday = models.CharField(max_length=255)
    cnational = models.CharField(max_length=255)
    cid_tax = models.CharField(max_length=255)
    cid_card = models.CharField(max_length=255)
    caddress = models.TextField()
    cbuilding = models.CharField(max_length=255)
    cvillage = models.CharField(max_length=255)
    cstreet = models.CharField(max_length=255)
    csoi = models.CharField(max_length=255)
    czip = models.CharField(max_length=255)
    chome_t = models.CharField(max_length=255)
    coffice_t = models.CharField(max_length=255)
    cmobile = models.CharField(max_length=255)
    cfax = models.CharField(max_length=255)
    csex = models.CharField(max_length=255)
    cemail = models.CharField(max_length=255)
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255)  # Field name made lowercase.
    iname_f = models.CharField(max_length=255)
    iname_t = models.CharField(max_length=255)
    irelation = models.CharField(max_length=255)
    iphone = models.CharField(max_length=255)
    iid_card = models.CharField(max_length=255)
    status_doc = models.IntegerField()
    status_expire = models.IntegerField()
    status_terminate = models.IntegerField()
    terminate_date = models.DateTimeField()
    status_suspend = models.IntegerField()
    suspend_date = models.DateTimeField()
    status_blacklist = models.IntegerField()
    status_ato = models.IntegerField()
    sletter = models.IntegerField()
    sinv_code = models.CharField(max_length=255)
    txtoption = models.TextField()
    setregis = models.IntegerField()
    slr = models.CharField(max_length=11)
    locationbase = models.IntegerField()
    cid_mobile = models.CharField(max_length=255)
    bewallet = models.DecimalField(max_digits=15, decimal_places=2)
    bvoucher = models.DecimalField(max_digits=15, decimal_places=2)
    voucher = models.DecimalField(max_digits=15, decimal_places=2)
    manager = models.CharField(max_length=255)
    mtype = models.IntegerField()
    mtype1 = models.IntegerField()
    mtype2 = models.IntegerField()
    mvat = models.IntegerField()
    uidbase = models.CharField(max_length=255)
    exp_date = models.DateField()
    head_code = models.CharField(max_length=255)
    pv_l = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c = models.DecimalField(max_digits=15, decimal_places=2)
    hpv_l = models.DecimalField(max_digits=15, decimal_places=2)
    hpv_c = models.DecimalField(max_digits=15, decimal_places=2)
    pv_l_nextmonth = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c_nextmonth = models.DecimalField(max_digits=15, decimal_places=2)
    pv_l_lastmonth1 = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c_lastmonth1 = models.DecimalField(max_digits=15, decimal_places=2)
    pv_l_lastmonth2 = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c_lastmonth2 = models.DecimalField(max_digits=15, decimal_places=2)
    rcode_star = models.IntegerField()
    bunit = models.IntegerField()
    province = models.CharField(max_length=11)
    line_id = models.CharField(max_length=255)
    facebook_name = models.CharField(max_length=255)
    type_com = models.IntegerField()
    exp_pos = models.DateField()
    exp_pos_60 = models.DateField()
    trip_private = models.DecimalField(max_digits=15, decimal_places=2)
    trip_team = models.DecimalField(max_digits=15, decimal_places=2)
    myfile1 = models.CharField(max_length=255)
    myfile2 = models.CharField(max_length=255)
    cline_id = models.CharField(max_length=255)
    cfacebook_name = models.CharField(max_length=255)
    profile_img = models.CharField(max_length=255)
    atocom = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    line_depth = models.IntegerField(blank=True, null=True)
    line_lft = models.IntegerField(blank=True, null=True)
    line_rgt = models.IntegerField(blank=True, null=True)
    ocert = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_member'


class AliMember20180525(models.Model):
    mcode = models.CharField(unique=True, max_length=255)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    name_e = models.CharField(max_length=255)
    posid = models.CharField(max_length=255)
    mdate = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    national = models.CharField(max_length=255)
    id_tax = models.CharField(max_length=255)
    id_card = models.CharField(max_length=255)
    id_card_img = models.CharField(max_length=250)
    id_card_img_date = models.DateTimeField()
    zip = models.CharField(max_length=255)
    home_t = models.CharField(max_length=255)
    office_t = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    mcode_acc = models.CharField(max_length=255)
    bonusrec = models.CharField(max_length=255)
    bankcode = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    acc_type = models.CharField(max_length=255)
    acc_no = models.CharField(max_length=255)
    acc_no_img = models.CharField(max_length=250)
    acc_no_img_date = models.DateTimeField()
    acc_name = models.CharField(max_length=255)
    acc_prov = models.CharField(max_length=255)
    sv_code = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    sp_name = models.CharField(max_length=255)
    sp_code2 = models.CharField(max_length=255)
    sp_name2 = models.CharField(max_length=255)
    upa_code = models.CharField(max_length=255)
    upa_name = models.CharField(max_length=255)
    lr = models.CharField(max_length=255)
    complete = models.CharField(max_length=255)
    compdate = models.CharField(max_length=255)
    modate = models.CharField(max_length=255)
    usercode = models.CharField(max_length=255)
    name_b = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    status = models.IntegerField()
    mar_name = models.CharField(max_length=100)
    mar_age = models.IntegerField()
    email = models.CharField(max_length=50)
    beneficiaries = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    districtid = models.CharField(db_column='districtId', max_length=255)  # Field name made lowercase.
    amphurid = models.CharField(db_column='amphurId', max_length=255)  # Field name made lowercase.
    provinceid = models.CharField(db_column='provinceId', max_length=255)  # Field name made lowercase.
    fax = models.CharField(max_length=20)
    inv_code = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    oid = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)
    pos_cur1 = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=255)
    pos_cur3 = models.CharField(max_length=255)
    pos_cur4 = models.CharField(max_length=255)
    pos_cur_tmp = models.CharField(max_length=255)
    rpos_cur4 = models.IntegerField()
    pos_cur3_date = models.DateField()
    memdesc = models.CharField(max_length=40)
    cmp = models.CharField(max_length=10)
    cmp2 = models.CharField(max_length=255)
    cmp3 = models.CharField(max_length=255)
    ccmp = models.CharField(max_length=255)
    ccmp2 = models.CharField(max_length=255)
    ccmp3 = models.CharField(max_length=255)
    address = models.TextField()
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    soi = models.CharField(max_length=255)
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    eatoship = models.DecimalField(max_digits=15, decimal_places=2)
    ecom = models.DecimalField(max_digits=15, decimal_places=2)
    bmdate1 = models.CharField(max_length=255)
    bmdate2 = models.CharField(max_length=255)
    bmdate3 = models.CharField(max_length=255)
    cbmdate1 = models.CharField(max_length=255)
    cbmdate2 = models.CharField(max_length=255)
    cbmdate3 = models.CharField(max_length=255)
    online = models.IntegerField()
    cname_f = models.CharField(max_length=255)
    cname_t = models.CharField(max_length=255)
    cname_e = models.CharField(max_length=255)
    cname_b = models.CharField(max_length=255)
    cbirthday = models.CharField(max_length=255)
    cnational = models.CharField(max_length=255)
    cid_tax = models.CharField(max_length=255)
    cid_card = models.CharField(max_length=255)
    caddress = models.TextField()
    cbuilding = models.CharField(max_length=255)
    cvillage = models.CharField(max_length=255)
    cstreet = models.CharField(max_length=255)
    csoi = models.CharField(max_length=255)
    czip = models.CharField(max_length=255)
    chome_t = models.CharField(max_length=255)
    coffice_t = models.CharField(max_length=255)
    cmobile = models.CharField(max_length=255)
    cfax = models.CharField(max_length=255)
    csex = models.CharField(max_length=255)
    cemail = models.CharField(max_length=255)
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255)  # Field name made lowercase.
    iname_f = models.CharField(max_length=255)
    iname_t = models.CharField(max_length=255)
    irelation = models.CharField(max_length=255)
    iphone = models.CharField(max_length=255)
    iid_card = models.CharField(max_length=255)
    status_doc = models.IntegerField()
    status_expire = models.IntegerField()
    status_terminate = models.IntegerField()
    terminate_date = models.DateTimeField()
    status_suspend = models.IntegerField()
    suspend_date = models.DateTimeField()
    status_blacklist = models.IntegerField()
    status_ato = models.IntegerField()
    sletter = models.IntegerField()
    sinv_code = models.CharField(max_length=255)
    txtoption = models.TextField()
    setregis = models.IntegerField()
    slr = models.CharField(max_length=11)
    locationbase = models.IntegerField()
    cid_mobile = models.CharField(max_length=255)
    bewallet = models.DecimalField(max_digits=15, decimal_places=2)
    bvoucher = models.DecimalField(max_digits=15, decimal_places=2)
    voucher = models.DecimalField(max_digits=15, decimal_places=2)
    manager = models.CharField(max_length=255)
    mtype = models.IntegerField()
    mtype1 = models.IntegerField()
    mtype2 = models.IntegerField()
    mvat = models.IntegerField()
    uidbase = models.CharField(max_length=255)
    exp_date = models.DateField()
    head_code = models.CharField(max_length=255)
    pv_l = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c = models.DecimalField(max_digits=15, decimal_places=2)
    hpv_l = models.DecimalField(max_digits=15, decimal_places=2)
    hpv_c = models.DecimalField(max_digits=15, decimal_places=2)
    pv_l_nextmonth = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c_nextmonth = models.DecimalField(max_digits=15, decimal_places=2)
    pv_l_lastmonth1 = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c_lastmonth1 = models.DecimalField(max_digits=15, decimal_places=2)
    pv_l_lastmonth2 = models.DecimalField(max_digits=15, decimal_places=2)
    pv_c_lastmonth2 = models.DecimalField(max_digits=15, decimal_places=2)
    rcode_star = models.IntegerField()
    bunit = models.IntegerField()
    province = models.CharField(max_length=11)
    line_id = models.CharField(max_length=255)
    facebook_name = models.CharField(max_length=255)
    type_com = models.IntegerField()
    exp_pos = models.DateField()
    exp_pos_60 = models.DateField()
    trip_private = models.DecimalField(max_digits=15, decimal_places=2)
    trip_team = models.DecimalField(max_digits=15, decimal_places=2)
    myfile1 = models.CharField(max_length=255)
    myfile2 = models.CharField(max_length=255)
    cline_id = models.CharField(max_length=255)
    cfacebook_name = models.CharField(max_length=255)
    profile_img = models.CharField(max_length=255)
    atocom = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_member_20180525'


class AliMemberShow(models.Model):
    mcode = models.CharField(max_length=255)
    mdate = models.DateField()
    id = models.BigAutoField(primary_key=True)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fast = models.DecimalField(max_digits=15, decimal_places=2)
    weakstrong = models.DecimalField(max_digits=15, decimal_places=2)
    matching = models.DecimalField(max_digits=15, decimal_places=2)
    upa_code = models.CharField(max_length=255)
    upa_name = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    sp_name = models.CharField(max_length=255)
    lv = models.IntegerField()
    lr = models.IntegerField()
    pos_cur = models.CharField(max_length=255)
    pos_cur1 = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=20)
    uid = models.CharField(max_length=255)
    totpv = models.DecimalField(max_digits=15, decimal_places=2)
    thismonth = models.DecimalField(max_digits=15, decimal_places=2)
    nextmonth = models.DecimalField(max_digits=15, decimal_places=2)
    sadate = models.DateField()
    okok = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_member_show'


class AliMemberTmp(models.Model):
    transtype = models.IntegerField()
    paytype = models.IntegerField()
    paydate = models.DateTimeField()
    credittype = models.IntegerField()
    sendtype = models.IntegerField()
    cstreet = models.CharField(max_length=255)
    mcode = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255, blank=True, null=True)
    name_t = models.CharField(max_length=255, blank=True, null=True)
    name_e = models.CharField(max_length=255, blank=True, null=True)
    posid = models.CharField(max_length=2, blank=True, null=True)
    mdate = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    national = models.CharField(max_length=20, blank=True, null=True)
    id_tax = models.CharField(max_length=10, blank=True, null=True)
    id_card = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    home_t = models.CharField(max_length=20, blank=True, null=True)
    office_t = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    mcode_acc = models.CharField(max_length=7, blank=True, null=True)
    bonusrec = models.CharField(max_length=1, blank=True, null=True)
    bankcode = models.CharField(max_length=2, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acc_type = models.CharField(max_length=20, blank=True, null=True)
    acc_no = models.CharField(max_length=20, blank=True, null=True)
    acc_name = models.CharField(max_length=255, blank=True, null=True)
    acc_prov = models.CharField(max_length=20, blank=True, null=True)
    sv_code = models.CharField(max_length=20, blank=True, null=True)
    sp_code = models.CharField(max_length=255, blank=True, null=True)
    sp_name = models.CharField(max_length=255, blank=True, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    upa_name = models.CharField(max_length=255, blank=True, null=True)
    lr = models.IntegerField(blank=True, null=True)
    complete = models.CharField(max_length=1, blank=True, null=True)
    compdate = models.CharField(max_length=255, blank=True, null=True)
    modate = models.CharField(max_length=255, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    name_b = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    status = models.IntegerField()
    mar_name = models.CharField(max_length=100)
    mar_age = models.IntegerField()
    email = models.CharField(max_length=50)
    beneficiaries = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    districtid = models.IntegerField(db_column='districtId')  # Field name made lowercase.
    amphurid = models.IntegerField(db_column='amphurId')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='provinceId')  # Field name made lowercase.
    fax = models.CharField(max_length=20)
    inv_code = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)
    pos_cur1 = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=255)
    pos_cur3 = models.CharField(max_length=255)
    pos_cur4 = models.CharField(max_length=255)
    rpos_cur4 = models.IntegerField()
    memdesc = models.CharField(max_length=40)
    cmp = models.CharField(max_length=10)
    cmp2 = models.CharField(max_length=255)
    cmp3 = models.CharField(max_length=255)
    ccmp = models.CharField(max_length=255)
    ccmp2 = models.CharField(max_length=255)
    ccmp3 = models.CharField(max_length=255)
    address = models.TextField()
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    soi = models.CharField(max_length=255)
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    bmdate1 = models.CharField(max_length=255)
    bmdate2 = models.CharField(max_length=255)
    bmdate3 = models.CharField(max_length=255)
    cbmdate1 = models.CharField(max_length=255)
    cbmdate2 = models.CharField(max_length=255)
    cbmdate3 = models.CharField(max_length=255)
    online = models.IntegerField()
    cname_f = models.CharField(max_length=255)
    cname_t = models.CharField(max_length=255)
    cname_e = models.CharField(max_length=255)
    cname_b = models.CharField(max_length=255)
    cbirthday = models.CharField(max_length=255)
    cnational = models.CharField(max_length=255)
    cid_tax = models.CharField(max_length=255)
    cid_card = models.CharField(max_length=255)
    caddress = models.TextField()
    cbuilding = models.CharField(max_length=255)
    cvillage = models.CharField(max_length=255)
    csoi = models.CharField(max_length=255)
    czip = models.CharField(max_length=255)
    chome_t = models.CharField(max_length=255)
    coffice_t = models.CharField(max_length=255)
    cmobile = models.CharField(max_length=255)
    cfax = models.CharField(max_length=255)
    csex = models.CharField(max_length=255)
    cemail = models.CharField(max_length=255)
    cdistrictid = models.IntegerField(db_column='cdistrictId')  # Field name made lowercase.
    camphurid = models.IntegerField(db_column='camphurId')  # Field name made lowercase.
    cprovinceid = models.IntegerField(db_column='cprovinceId')  # Field name made lowercase.
    iname_f = models.CharField(max_length=255)
    iname_t = models.CharField(max_length=255)
    irelation = models.CharField(max_length=255)
    iphone = models.CharField(max_length=255)
    iid_card = models.CharField(max_length=255)
    status_doc = models.IntegerField()
    status_expire = models.IntegerField()
    status_terminate = models.IntegerField()
    terminate_date = models.DateTimeField()
    status_suspend = models.IntegerField()
    suspend_date = models.DateTimeField()
    status_blacklist = models.IntegerField()
    status_ato = models.IntegerField()
    sletter = models.IntegerField()
    sinv_code = models.CharField(max_length=255)
    txtoption = models.TextField()
    mcode_ref = models.CharField(max_length=255)
    cancel = models.IntegerField()
    sbook = models.IntegerField()
    sbinv_code = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    cid_mobile = models.CharField(max_length=255)
    bewallet = models.DecimalField(max_digits=15, decimal_places=2)
    bvoucher = models.DecimalField(max_digits=15, decimal_places=2)
    voucher = models.DecimalField(max_digits=15, decimal_places=2)
    manager = models.CharField(max_length=255)
    mtype = models.CharField(max_length=255)
    uidbase = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_member_tmp'


class AliMm(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    lr = models.IntegerField(blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    gpv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=10)
    npos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'ali_mm'


class AliMmbonus(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    tot_pv = models.DecimalField(max_digits=12, decimal_places=5)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    bonus = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    pos_cur = models.CharField(max_length=255)
    pstatus = models.IntegerField()
    prcode = models.IntegerField()
    pmonth = models.CharField(max_length=255)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()
    chk_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_mmbonus'


class AliMmobile(models.Model):
    mcode = models.CharField(max_length=7, blank=True, null=True)
    rcode = models.IntegerField(blank=True, null=True)
    dl = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    coupon = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    sync = models.CharField(max_length=1, blank=True, null=True)
    web = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_mmobile'


class AliMmodesc(models.Model):
    mcode = models.CharField(max_length=7, blank=True, null=True)
    rcode = models.IntegerField(blank=True, null=True)
    cmcode = models.CharField(max_length=7, blank=True, null=True)
    level = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    csano = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_mmodesc'


class AliMoround(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.CharField(max_length=5, blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)
    fsano = models.CharField(max_length=7, blank=True, null=True)
    tsano = models.CharField(max_length=7, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_moround'


class AliMpv(models.Model):
    bid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=5, blank=True, null=True)
    npos = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_mpv'


class AliMsaled(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=255)
    mcode = models.CharField(max_length=7, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    weight = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    uidbase = models.CharField(max_length=255)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_msaled'


class AliMsaleh(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sano1 = models.BigIntegerField()
    sadate = models.DateField(blank=True, null=True)
    sctime = models.DateTimeField()
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_ref = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    tot_weight = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtoption = models.TextField()
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtinternet = models.DecimalField(db_column='txtInternet', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtdiscount = models.DecimalField(db_column='txtDiscount', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtother = models.DecimalField(db_column='txtOther', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255)  # Field name made lowercase.
    discount = models.CharField(max_length=255)
    print = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    hcancel = models.IntegerField()
    caddress = models.TextField()
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255)  # Field name made lowercase.
    czip = models.CharField(max_length=255)
    sender = models.IntegerField()
    sender_date = models.DateField()
    receive = models.IntegerField()
    receive_date = models.DateField()
    asend = models.IntegerField()
    ato_type = models.IntegerField()
    ato_id = models.IntegerField()
    online = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    htotal = models.DecimalField(max_digits=15, decimal_places=2)
    hdate = models.DateField()
    scheck = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    rcode = models.IntegerField()
    bmcauto = models.IntegerField()
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    cmobile = models.CharField(max_length=255)
    uid_sender = models.CharField(max_length=255)
    uid_receive = models.CharField(max_length=255)
    mbase = models.CharField(max_length=255)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    locationbase = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'ali_msaleh'


class AliMyPv(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=5)
    pv_exp = models.DecimalField(max_digits=15, decimal_places=2)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=1)
    pmonth = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'ali_my_pv'


class AliNation(models.Model):
    nation = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_nation'


class AliNews(models.Model):
    head = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    dates = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1)
    popup = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ali_news'


class AliOmbonus(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    bonus = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    pos_cur = models.CharField(max_length=255)
    adjust = models.DecimalField(max_digits=15, decimal_places=2)
    pstatus = models.IntegerField()
    prcode = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_ombonus'


class AliOon(models.Model):
    oon = models.IntegerField()
    sms_credits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_oon'


class AliOstockd(models.Model):
    sano = models.IntegerField(blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_coden = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    inv_refn = models.CharField(max_length=255)
    rccode = models.CharField(max_length=255)
    stockist = models.CharField(max_length=255)
    pcode = models.CharField(max_length=255, blank=True, null=True)
    pdesc = models.CharField(max_length=40, blank=True, null=True)
    unit = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ctax = models.IntegerField()
    group_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_ostockd'


class AliOstockh(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sano1 = models.CharField(max_length=255)
    sadate = models.DateField(blank=True, null=True)
    sctime = models.DateTimeField()
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_coden = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    inv_refn = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    sa_mtype = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    uid_ref = models.CharField(max_length=255)
    cancel = models.IntegerField()
    txtoption = models.TextField()
    sender = models.CharField(max_length=255)
    sender_date = models.DateTimeField()
    receive = models.IntegerField()
    receive_date = models.DateTimeField()
    uid_receive = models.CharField(max_length=255)
    status = models.IntegerField()
    print = models.IntegerField()
    rccode = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    mapping_code = models.CharField(max_length=255)
    rrcode = models.CharField(max_length=255)
    auto = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_ostockh'


class AliPackageInvcode(models.Model):
    pcode = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_package_invcode'


class AliPairbonus(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    pair = models.DecimalField(max_digits=15, decimal_places=0)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    bonus = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_pairbonus'


class AliPayment(models.Model):
    payment_name = models.CharField(max_length=255)
    order_by = models.IntegerField()
    payment_ref = models.CharField(max_length=255)
    rep_column = models.CharField(max_length=2555)
    payment_column = models.CharField(max_length=255)
    shows = models.IntegerField()
    shows_ewallet = models.IntegerField()
    shows_mem_edit = models.IntegerField()
    shows_member = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_payment'


class AliPaymentBranch(models.Model):
    inv_code = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_payment_branch'


class AliPaymentType(models.Model):
    payment_id = models.IntegerField()
    pay_desc = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)
    shows = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_payment_type'


class AliPc(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    mposi = models.CharField(max_length=10, blank=True, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    bposi = models.CharField(max_length=10, blank=True, null=True)
    level = models.DecimalField(max_digits=15, decimal_places=0)
    gen = models.DecimalField(max_digits=15, decimal_places=0)
    btype = models.CharField(max_length=10, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    percer = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_pc'


class AliPmbonus(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    status = models.CharField(max_length=2)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    pvb = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    mdate = models.DateField()
    month_pv = models.CharField(max_length=10)
    mpos = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_pmbonus'


class AliPoschange(models.Model):
    mcode = models.CharField(max_length=255)
    pos_before = models.CharField(max_length=11, blank=True, null=True)
    pos_after = models.CharField(max_length=11, blank=True, null=True)
    date_change = models.DateField(blank=True, null=True)
    date_update = models.DateField()
    type = models.IntegerField(blank=True, null=True)
    uid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_poschange'


class AliPosition(models.Model):
    posid = models.AutoField(primary_key=True)
    posshort = models.CharField(max_length=5, blank=True, null=True)
    posname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    posimg = models.CharField(max_length=50, blank=True, null=True)
    posavt = models.CharField(max_length=255)
    posutab = models.CharField(max_length=10, blank=True, null=True)
    posdtab = models.CharField(max_length=10, blank=True, null=True)
    posdesc = models.CharField(max_length=50, blank=True, null=True)
    ud = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_position'


class AliPosition2(models.Model):
    posid = models.AutoField(primary_key=True)
    posshort = models.CharField(max_length=3, blank=True, null=True)
    posname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    posimg = models.CharField(max_length=50, blank=True, null=True)
    posutab = models.CharField(max_length=10, blank=True, null=True)
    posdtab = models.CharField(max_length=10, blank=True, null=True)
    posdesc = models.CharField(max_length=50, blank=True, null=True)
    ud = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_position2'


class AliPospv(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    opos = models.CharField(max_length=255, blank=True, null=True)
    npos = models.CharField(max_length=255, blank=True, null=True)
    name_t = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255, blank=True, null=True)
    upa_code = models.CharField(max_length=255)
    lr = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_pospv'


class AliPospvTmp(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    opos = models.CharField(max_length=255, blank=True, null=True)
    npos = models.CharField(max_length=255, blank=True, null=True)
    name_t = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255, blank=True, null=True)
    lr = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_pospv_tmp'


class AliPpv(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=5, blank=True, null=True)
    npos = models.CharField(max_length=5, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_ppv'

class AliPromotion(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    rdate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()
    rtype = models.IntegerField()
    firstseat = models.DecimalField(max_digits=15, decimal_places=2)
    secondseat = models.DecimalField(max_digits=15, decimal_places=2)
    rincrease = models.DecimalField(max_digits=15, decimal_places=2)
    rurl = models.TextField()
    calc_date = models.DateTimeField()
    tshow = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_promotion'


class AliPround(models.Model):
    rid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)
    fsano = models.CharField(max_length=7, blank=True, null=True)
    tsano = models.CharField(max_length=7, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    calc = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()
    fpdate = models.DateField()
    tpdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_pround'


class AliRc(models.Model):
    bid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    mposi = models.CharField(max_length=10, blank=True, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    bposi = models.CharField(max_length=10, blank=True, null=True)
    level = models.DecimalField(max_digits=15, decimal_places=0)
    gen = models.DecimalField(max_digits=15, decimal_places=0)
    btype = models.CharField(max_length=10, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2)
    percer = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    checkcheck = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_rc'


class AliRccode(models.Model):
    rccode = models.CharField(max_length=255)
    rccode_desc = models.CharField(max_length=255)
    mapping_code = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_rccode'


class AliReportCron(models.Model):
    start_cron_cal = models.DateTimeField()
    finish_cron_cal = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ali_report_cron'


class AliReportMember(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    mdate = models.DateField()
    expdate = models.DateField()
    pvdate = models.DateField()
    pos_cur = models.CharField(max_length=255)
    pos_cur4 = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=255)
    pos_cur1 = models.CharField(max_length=255)
    new_member = models.IntegerField()
    new_sup = models.IntegerField()
    new_ex = models.IntegerField()
    sup_ex = models.IntegerField()
    pvmonth = models.IntegerField()
    auto_tot = models.DecimalField(max_digits=15, decimal_places=2)
    pv_l = models.IntegerField()
    pv_c = models.IntegerField()
    tpos_cur = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    sp_name = models.CharField(max_length=255)
    lr = models.IntegerField()
    report1 = models.CharField(max_length=255)
    status_ato = models.CharField(max_length=255)
    status_member = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_report_member'


class AliReportPoint(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    point = models.IntegerField()
    monthpv = models.CharField(max_length=255)
    carry_l = models.IntegerField()
    carry_c = models.IntegerField()
    ro_l = models.IntegerField()
    ro_c = models.IntegerField()
    all_l = models.IntegerField()
    all_c = models.IntegerField()
    allpv = models.IntegerField()
    pos_cur = models.CharField(max_length=255)
    new_sponsor = models.IntegerField()
    new_sup = models.IntegerField()
    new_ex = models.IntegerField()
    sup_ex = models.IntegerField()
    travelpoint = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_report_point'


class AliReportPoint1(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    point = models.IntegerField()
    monthpv = models.CharField(max_length=255)
    carry_l = models.IntegerField()
    carry_c = models.IntegerField()
    ro_l = models.IntegerField()
    ro_c = models.IntegerField()
    all_l = models.IntegerField()
    all_c = models.IntegerField()
    allpv = models.IntegerField()
    pos_cur = models.CharField(max_length=255)
    new_sponsor = models.IntegerField()
    new_sup = models.IntegerField()
    new_ex = models.IntegerField()
    sup_ex = models.IntegerField()
    travelpoint = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_report_point1'


class AliReportPromotion(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    sp_code = models.CharField(max_length=255)
    sp_name = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=255)
    fdate = models.DateField()
    tdate = models.DateField()
    tot_pv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_report_promotion'


class AliReportPromotion1(models.Model):
    sp_code = models.CharField(max_length=255)
    sp_name = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=255)
    fdate = models.DateField()
    tdate = models.DateField()
    tot_pv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_report_promotion1'


class AliRsaled(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=255, blank=True, null=True)
    pdesc = models.CharField(max_length=40, blank=True, null=True)
    mcode = models.CharField(max_length=7, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_rsaled'


class AliRsaleh(models.Model):
    sano = models.BigIntegerField(blank=True, null=True)
    sano1 = models.BigIntegerField()
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_ref = models.CharField(max_length=255)
    mcode = models.CharField(max_length=20, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtoption = models.TextField()
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255)  # Field name made lowercase.
    txtcash = models.CharField(db_column='txtCash', max_length=255)  # Field name made lowercase.
    txtfuture = models.CharField(db_column='txtFuture', max_length=255)  # Field name made lowercase.
    txttransfer = models.CharField(db_column='txtTransfer', max_length=255)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    txtcredit1 = models.CharField(db_column='txtCredit1', max_length=255)  # Field name made lowercase.
    txtcredit2 = models.CharField(db_column='txtCredit2', max_length=255)  # Field name made lowercase.
    txtcredit3 = models.CharField(db_column='txtCredit3', max_length=255)  # Field name made lowercase.
    txtinternet = models.CharField(db_column='txtInternet', max_length=255)  # Field name made lowercase.
    txtdiscount = models.CharField(db_column='txtDiscount', max_length=255)  # Field name made lowercase.
    txtother = models.CharField(db_column='txtOther', max_length=255)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255)  # Field name made lowercase.
    asend = models.IntegerField()
    asend_date = models.DateField()
    discount = models.CharField(max_length=255)
    print = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ali_rsaleh'


class AliRscode(models.Model):
    rccode = models.CharField(max_length=255)
    rccode_desc = models.CharField(max_length=255)
    mapping_code = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_rscode'


class AliSaleEwallet(models.Model):
    rcode = models.IntegerField()
    yokma = models.DecimalField(max_digits=15, decimal_places=2)
    buy = models.DecimalField(max_digits=15, decimal_places=2)
    used = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.CharField(max_length=255)
    tdate = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_sale_ewallet'


class AliSaleHold(models.Model):
    rcode = models.IntegerField()
    yokma = models.DecimalField(max_digits=15, decimal_places=2)
    buy = models.DecimalField(max_digits=15, decimal_places=2)
    used = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.CharField(max_length=255)
    tdate = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_sale_hold'


class AliSc(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    mpos = models.CharField(max_length=10, blank=True, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_sc'


class AliSending(models.Model):
    sid = models.AutoField(primary_key=True)
    locationbase = models.CharField(max_length=255)
    minpv = models.IntegerField()
    maxpv = models.IntegerField()
    minweight = models.DecimalField(max_digits=15, decimal_places=2)
    maxweight = models.DecimalField(max_digits=15, decimal_places=2)
    inbound_pcode = models.CharField(db_column='inbound-pcode', max_length=255)  # Field renamed to remove unsuitable characters.
    outbound_pcode = models.CharField(db_column='outbound-pcode', max_length=255)  # Field renamed to remove unsuitable characters.
    overweight_pcode = models.CharField(db_column='overweight-pcode', max_length=255)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ali_sending'


class AliSmbonus(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.DecimalField(max_digits=15, decimal_places=2)
    bonus = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    pos_cur = models.CharField(max_length=255)
    adjust = models.DecimalField(max_digits=15, decimal_places=2)
    pstatus = models.IntegerField()
    prcode = models.IntegerField()
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_smbonus'


class AliSms(models.Model):
    mcode = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    mobile_desc = models.TextField()
    mobile_date = models.CharField(max_length=14)
    send_date = models.CharField(max_length=14)
    mobile_status = models.CharField(max_length=255)
    mobile_credits = models.CharField(max_length=255)
    credit_balance = models.IntegerField()
    recieve_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ali_sms'


class AliSpecialPoint(models.Model):
    vip_id = models.IntegerField()
    sadate = models.DateField()
    mcode = models.CharField(max_length=20)
    sa_type = models.CharField(max_length=2)
    tot_pv = models.DecimalField(max_digits=10, decimal_places=2)
    uid = models.CharField(max_length=255)
    heal_mouth = models.CharField(max_length=6)
    ttime = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ali_special_point'


class AliSpecialPointGroup(models.Model):
    vip_id = models.IntegerField()
    sadate = models.DateField(blank=True, null=True)
    mcode = models.CharField(max_length=20, blank=True, null=True)
    sa_type = models.CharField(max_length=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    heal_mouth = models.CharField(max_length=6, blank=True, null=True)
    ttime = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ali_special_point_group'


class AliSponsor(models.Model):
    mcode = models.CharField(max_length=7)
    sponsor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_sponsor'


class AliStdesc(models.Model):
    mcode = models.CharField(max_length=7, blank=True, null=True)
    rcode = models.IntegerField(blank=True, null=True)
    cmcode = models.CharField(max_length=7, blank=True, null=True)
    level = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    csano = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_stdesc'


class AliStockcardE(models.Model):
    mcode = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    inv_action = models.CharField(max_length=255)
    sano = models.CharField(max_length=255)
    sano_ref = models.CharField(max_length=255)
    pcode = models.CharField(max_length=255)
    pdesc = models.CharField(max_length=255)
    in_amount = models.DecimalField(max_digits=15, decimal_places=2)
    out_amount = models.DecimalField(max_digits=15, decimal_places=2)
    sadate = models.DateField()
    rdate = models.DateTimeField()
    rccode = models.CharField(max_length=255)
    yokma = models.IntegerField()
    balance = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    uid = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_stockcard_e'


class AliStockcardR(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)
    inv_ref = models.CharField(max_length=255)
    inv_action = models.CharField(max_length=255)
    sano = models.CharField(max_length=255)
    sano_ref = models.CharField(max_length=255)
    pcode = models.CharField(max_length=255)
    pdesc = models.CharField(max_length=255)
    in_qty = models.IntegerField()
    in_price = models.DecimalField(max_digits=15, decimal_places=2)
    in_amount = models.DecimalField(max_digits=15, decimal_places=2)
    out_qty = models.IntegerField()
    out_price = models.DecimalField(max_digits=15, decimal_places=2)
    out_amount = models.DecimalField(max_digits=15, decimal_places=2)
    sadate = models.DateField()
    rdate = models.DateTimeField()
    rccode = models.CharField(max_length=255)
    yokma = models.IntegerField()
    balance = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    uid = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    cancel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_stockcard_r'





class AliStockeep(models.Model):
    mcode = models.CharField(max_length=255, blank=True, null=True)
    rcode = models.IntegerField(blank=True, null=True)
    dl = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    coupon = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    paydate = models.DateField(blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    sync = models.CharField(max_length=1, blank=True, null=True)
    web = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_stockeep'


class AliStocks(models.Model):
    sano = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)
    inv_code1 = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255)
    pcode = models.CharField(max_length=255)
    yokma = models.IntegerField()
    qty = models.IntegerField()
    amt = models.IntegerField()
    sdate = models.DateField()
    stime = models.TimeField()
    status = models.CharField(max_length=255)
    remark = models.TextField()
    uid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_stocks'


class AliSubuser(models.Model):
    uid = models.AutoField(primary_key=True)
    usercode = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    object1 = models.CharField(max_length=1, blank=True, null=True)
    object2 = models.CharField(max_length=1, blank=True, null=True)
    object3 = models.CharField(max_length=1, blank=True, null=True)
    object4 = models.CharField(max_length=1, blank=True, null=True)
    object5 = models.CharField(max_length=1, blank=True, null=True)
    accessright = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_subuser'


class AliSupplier(models.Model):
    sup_code = models.CharField(max_length=7, blank=True, null=True)
    sup_desc = models.CharField(max_length=255, blank=True, null=True)
    sup_type = models.IntegerField()
    address = models.TextField()
    districtid = models.IntegerField(db_column='districtId')  # Field name made lowercase.
    amphurid = models.IntegerField(db_column='amphurId')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='provinceId')  # Field name made lowercase.
    zip = models.CharField(max_length=5)
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_supplier'


class AliSyscomm(models.Model):
    cid = models.AutoField(primary_key=True)
    faststart = models.CharField(max_length=1, blank=True, null=True)
    binary = models.CharField(max_length=1, blank=True, null=True)
    weekstrong = models.CharField(max_length=1, blank=True, null=True)
    trinary = models.CharField(max_length=1, blank=True, null=True)
    unilevel = models.CharField(max_length=1, blank=True, null=True)
    matching = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_syscomm'


class AliTax(models.Model):
    cid = models.AutoField(primary_key=True)
    locationbase = models.CharField(max_length=255)
    minaccamount = models.DecimalField(max_digits=15, decimal_places=2)
    maxaccamount = models.DecimalField(max_digits=15, decimal_places=2)
    vatlocal = models.IntegerField()
    vatforeign = models.IntegerField()
    taxlocal = models.DecimalField(max_digits=15, decimal_places=2)
    taxforeign = models.DecimalField(max_digits=15, decimal_places=2)
    mtype = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_tax'


class AliTempAd(models.Model):
    mcode = models.CharField(max_length=7, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    lr1 = models.CharField(max_length=2, blank=True, null=True)
    rcode_l = models.CharField(max_length=5, blank=True, null=True)
    level_l = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    mcode_l = models.CharField(max_length=7, blank=True, null=True)
    sano_l = models.CharField(max_length=7, blank=True, null=True)
    rcode_r = models.CharField(max_length=5, blank=True, null=True)
    level_r = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    mcode_r = models.CharField(max_length=7, blank=True, null=True)
    sano_r = models.CharField(max_length=7, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_temp_ad'


class AliTmbonus(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    pos_cur = models.CharField(max_length=255)
    mb2su = models.IntegerField()
    mb2ex = models.IntegerField()
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2)
    left_pv = models.DecimalField(max_digits=15, decimal_places=2)
    right_pv = models.DecimalField(max_digits=15, decimal_places=2)
    balance_pv = models.DecimalField(max_digits=15, decimal_places=2)
    tpoint = models.DecimalField(max_digits=15, decimal_places=2)
    spoint = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_tmbonus'


class AliTmbonus1(models.Model):
    mcode = models.CharField(max_length=255)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    rcode = models.IntegerField()
    smallbig = models.IntegerField()
    point = models.DecimalField(max_digits=15, decimal_places=2)
    seats = models.IntegerField()
    fdate = models.DateField()
    tdate = models.DateField()
    locationbase = models.IntegerField()
    firstseatpoint = models.DecimalField(max_digits=15, decimal_places=2)
    secondseatpoint = models.DecimalField(max_digits=15, decimal_places=2)
    function_count = models.IntegerField()
    groupvp = models.IntegerField()
    couple = models.IntegerField()
    pos_cur = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_tmbonus1'


class AliTransferEwalletConfirm(models.Model):
    mcode = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    sadate = models.DateField()
    sctime = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    img_pay = models.TextField()
    approved_uid = models.CharField(max_length=255)
    approved_sctime = models.DateTimeField()
    approved_status = models.IntegerField()
    cancel_uid = models.CharField(max_length=255)
    cancel_sctime = models.DateTimeField()
    cancel_status = models.IntegerField()
    last_sctime = models.DateTimeField()
    sano_ref = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_transfer_ewallet_confirm'


class AliTransferewalletH(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sano1 = models.BigIntegerField()
    sadate = models.DateField(blank=True, null=True)
    sctime = models.DateTimeField()
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_ref = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    tot_weight = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtoption = models.TextField()
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255)  # Field name made lowercase.
    txtcash = models.CharField(db_column='txtCash', max_length=255)  # Field name made lowercase.
    txtfuture = models.CharField(db_column='txtFuture', max_length=255)  # Field name made lowercase.
    txttransfer = models.CharField(db_column='txtTransfer', max_length=255)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    txtcredit1 = models.CharField(db_column='txtCredit1', max_length=255)  # Field name made lowercase.
    txtcredit2 = models.CharField(db_column='txtCredit2', max_length=255)  # Field name made lowercase.
    txtcredit3 = models.CharField(db_column='txtCredit3', max_length=255)  # Field name made lowercase.
    txtinternet = models.CharField(db_column='txtInternet', max_length=255)  # Field name made lowercase.
    txtdiscount = models.CharField(db_column='txtDiscount', max_length=255)  # Field name made lowercase.
    txtother = models.CharField(db_column='txtOther', max_length=255)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255)  # Field name made lowercase.
    discount = models.CharField(max_length=255)
    print = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    hcancel = models.IntegerField()
    caddress = models.TextField()
    cdistrictid = models.IntegerField(db_column='cdistrictId')  # Field name made lowercase.
    camphurid = models.IntegerField(db_column='camphurId')  # Field name made lowercase.
    cprovinceid = models.IntegerField(db_column='cprovinceId')  # Field name made lowercase.
    czip = models.CharField(max_length=255)
    sender = models.IntegerField()
    sender_date = models.DateField()
    receive = models.IntegerField()
    receive_date = models.DateField()
    asend = models.IntegerField()
    ato_type = models.IntegerField()
    ato_id = models.IntegerField()
    online = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    htotal = models.DecimalField(max_digits=15, decimal_places=2)
    hdate = models.DateField()
    scheck = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    rcode = models.IntegerField()
    bmcauto = models.IntegerField()
    transtype = models.IntegerField()
    paytype = models.IntegerField()
    sendtype = models.IntegerField()
    credittype = models.IntegerField()
    paydate = models.DateTimeField()
    locationbase = models.IntegerField()
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    mbase = models.CharField(max_length=255)
    crate = models.DecimalField(max_digits=11, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'ali_transferewallet_h'


class AliTransfersaleD(models.Model):
    sano = models.CharField(max_length=7, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=20, blank=True, null=True)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=255)
    mcode = models.CharField(max_length=7, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=15, decimal_places=2)
    weight = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    locationbase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_transfersale_d'


class AliTransfersaleH(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sano1 = models.BigIntegerField()
    sadate = models.DateField(blank=True, null=True)
    sctime = models.DateTimeField()
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_ref = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    tot_weight = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtoption = models.TextField()
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255)  # Field name made lowercase.
    txtcash = models.CharField(db_column='txtCash', max_length=255)  # Field name made lowercase.
    txtfuture = models.CharField(db_column='txtFuture', max_length=255)  # Field name made lowercase.
    txttransfer = models.CharField(db_column='txtTransfer', max_length=255)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    txtcredit1 = models.CharField(db_column='txtCredit1', max_length=255)  # Field name made lowercase.
    txtcredit2 = models.CharField(db_column='txtCredit2', max_length=255)  # Field name made lowercase.
    txtcredit3 = models.CharField(db_column='txtCredit3', max_length=255)  # Field name made lowercase.
    txtinternet = models.CharField(db_column='txtInternet', max_length=255)  # Field name made lowercase.
    txtdiscount = models.CharField(db_column='txtDiscount', max_length=255)  # Field name made lowercase.
    txtother = models.CharField(db_column='txtOther', max_length=255)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255)  # Field name made lowercase.
    discount = models.CharField(max_length=255)
    print = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    pay_type = models.CharField(max_length=255)
    hcancel = models.IntegerField()
    caddress = models.TextField()
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255)  # Field name made lowercase.
    czip = models.CharField(max_length=255)
    sender = models.IntegerField()
    sender_date = models.DateField()
    receive = models.IntegerField()
    receive_date = models.DateField()
    asend = models.IntegerField()
    ato_type = models.IntegerField()
    ato_id = models.IntegerField()
    online = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    htotal = models.DecimalField(max_digits=15, decimal_places=2)
    hdate = models.DateField()
    scheck = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    rcode = models.IntegerField()
    bmcauto = models.IntegerField()
    transtype = models.IntegerField()
    paytype = models.IntegerField()
    sendtype = models.IntegerField()
    credittype = models.IntegerField()
    paydate = models.DateTimeField()
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    locationbase = models.IntegerField()
    mbase = models.CharField(max_length=255)
    cname = models.CharField(max_length=255)
    cmobile = models.CharField(max_length=255)
    crate = models.DecimalField(max_digits=11, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'ali_transfersale_h'


class AliTripBonus(models.Model):
    aid = models.AutoField(primary_key=True)
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    pv_private = models.DecimalField(max_digits=15, decimal_places=2)
    pv_team = models.DecimalField(max_digits=15, decimal_places=2)
    pv_use_private = models.DecimalField(max_digits=15, decimal_places=2)
    pv_use_team = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_private = models.DecimalField(max_digits=15, decimal_places=2)
    total_pv_team = models.DecimalField(max_digits=15, decimal_places=2)
    fdate = models.DateField()
    tdate = models.DateField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_trip_bonus'


class AliTripPv(models.Model):
    bid = models.AutoField(primary_key=True)
    rcode = models.IntegerField(blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    upa_code = models.CharField(max_length=255, blank=True, null=True)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mpos = models.CharField(max_length=5, blank=True, null=True)
    npos = models.CharField(max_length=5, blank=True, null=True)
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_trip_pv'


class AliTround(models.Model):
    rcode = models.IntegerField()
    rname = models.CharField(max_length=255)
    detail = models.TextField()
    fdate = models.DateField()
    tdate = models.DateField()
    rtype = models.IntegerField()
    firstseat = models.DecimalField(max_digits=15, decimal_places=2)
    secondseat = models.DecimalField(max_digits=15, decimal_places=2)
    rincrease = models.DecimalField(max_digits=15, decimal_places=2)
    rurl = models.CharField(max_length=255)
    remark = models.TextField()
    calc = models.CharField(max_length=255)
    calc_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ali_tround'


class AliUpv(models.Model):
    rcode = models.IntegerField()
    mcode = models.CharField(max_length=255)
    bmbonus = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_pv = models.DecimalField(max_digits=15, decimal_places=2)
    sano = models.IntegerField()
    sadate = models.DateField()
    fdate = models.DateField()
    tdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'ali_upv'


class AliUser(models.Model):
    uid = models.AutoField(primary_key=True)
    usercode = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    usertype = models.IntegerField(blank=True, null=True)
    object1 = models.IntegerField(blank=True, null=True)
    object2 = models.IntegerField(blank=True, null=True)
    object3 = models.IntegerField(blank=True, null=True)
    object4 = models.IntegerField(blank=True, null=True)
    object5 = models.IntegerField(blank=True, null=True)
    object6 = models.IntegerField()
    object7 = models.IntegerField()
    object8 = models.IntegerField()
    object9 = models.IntegerField()
    object10 = models.IntegerField()
    inv_ref = models.CharField(max_length=20, blank=True, null=True)
    accessright = models.TextField(blank=True, null=True)
    code_ref = models.CharField(max_length=255)
    checkbackdate = models.IntegerField()
    limitcredit = models.IntegerField()
    mtype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_user'


class AliVoucher(models.Model):
    sano = models.CharField(unique=True, max_length=255, blank=True, null=True)
    rcode = models.IntegerField()
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.CharField(max_length=1, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtmoney = models.DecimalField(db_column='txtMoney', max_digits=15, decimal_places=2)  # Field name made lowercase.
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkwithdraw = models.CharField(db_column='chkWithdraw', max_length=255)  # Field name made lowercase.
    chktransfer_in = models.CharField(db_column='chkTransfer_in', max_length=255)  # Field name made lowercase.
    chktransfer_out = models.CharField(db_column='chkTransfer_out', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtwithdraw = models.DecimalField(db_column='txtWithdraw', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer_in = models.DecimalField(db_column='txtTransfer_in', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txttransfer_out = models.DecimalField(db_column='txtTransfer_out', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255)  # Field name made lowercase.
    optionwithdraw = models.CharField(db_column='optionWithdraw', max_length=255)  # Field name made lowercase.
    optiontransfer_in = models.CharField(db_column='optionTransfer_in', max_length=255)  # Field name made lowercase.
    optiontransfer_out = models.CharField(db_column='optionTransfer_out', max_length=255)  # Field name made lowercase.
    txtoption = models.TextField()
    ewallet = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ipay = models.CharField(max_length=255)
    checkportal = models.IntegerField()
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)
    locationbase = models.IntegerField()
    chkcommission = models.CharField(db_column='chkCommission', max_length=255)  # Field name made lowercase.
    txtcommission = models.DecimalField(db_column='txtCommission', max_digits=15, decimal_places=2)  # Field name made lowercase.
    optioncommission = models.CharField(db_column='optionCommission', max_length=255)  # Field name made lowercase.
    mbase = models.CharField(max_length=244)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    echeck = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_voucher'


class AliWebcfg(models.Model):
    cid = models.AutoField(primary_key=True)
    web_cfg = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_webcfg'


class Amphur(models.Model):
    amphurid = models.IntegerField(db_column='amphurId', primary_key=True)  # Field name made lowercase.
    amphurname = models.CharField(db_column='amphurName', max_length=30)  # Field name made lowercase.
    amphurnameeng = models.CharField(db_column='amphurNameEng', max_length=30, blank=True, null=True)  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='provinceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'amphur'


class AmphurPostcode(models.Model):
    amphur_id = models.PositiveIntegerField(db_column='AMPHUR_ID', primary_key=True)  # Field name made lowercase.
    post_code = models.PositiveIntegerField(db_column='POST_CODE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'amphur_postcode'
        unique_together = (('amphur_id', 'post_code'),)


class Chkbmbonus(models.Model):
    mcode = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    pos_cur = models.CharField(max_length=255)
    countsp = models.IntegerField()
    status_11 = models.IntegerField()
    status_12 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chkbmbonus'


class District(models.Model):
    districtid = models.IntegerField(db_column='districtId', primary_key=True)  # Field name made lowercase.
    districtname = models.CharField(db_column='districtName', max_length=255)  # Field name made lowercase.
    districtnameeng = models.CharField(db_column='districtNameEng', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amphurid = models.IntegerField(db_column='amphurId')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='provinceId')  # Field name made lowercase.
    zipcode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'district'


class MemberTerminate(models.Model):
    mcode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'member_terminate'


class Province(models.Model):
    provinceid = models.IntegerField(db_column='provinceId', primary_key=True)  # Field name made lowercase.
    provincename = models.CharField(db_column='provinceName', max_length=255)  # Field name made lowercase.
    provincenameeng = models.CharField(db_column='provinceNameEng', max_length=255)  # Field name made lowercase.
    region = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'province'


class TblActivityEn(models.Model):
    act_id = models.AutoField(primary_key=True)
    act_name = models.CharField(max_length=255)
    desc_s = models.TextField()
    desc_l = models.TextField()
    image = models.CharField(max_length=200)
    short = models.CharField(max_length=5)
    imageslide = models.CharField(db_column='imageSlide', max_length=100)  # Field name made lowercase.
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    slideshow = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'tbl_activity_en'


class TblActivityTh(models.Model):
    act_id = models.AutoField(primary_key=True)
    short = models.CharField(max_length=5)
    act_name = models.CharField(max_length=255)
    desc_s = models.TextField()
    desc_l = models.TextField()
    image = models.CharField(max_length=200)
    imageslide = models.CharField(db_column='imageSlide', max_length=100)  # Field name made lowercase.
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    slideshow = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'tbl_activity_th'
