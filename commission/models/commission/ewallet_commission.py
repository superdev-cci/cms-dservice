from django.db import models


class EwalletCommission(models.Model):
    sano = models.CharField(max_length=255, blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.CharField(max_length=1, blank=True, null=True)
    sa_type = models.CharField(max_length=2)
    uid = models.CharField(max_length=255)
    lid = models.CharField(max_length=255)
    dl = models.CharField(max_length=1)
    cancel = models.IntegerField()
    send = models.IntegerField()
    txtmoney = models.DecimalField(db_column='txtMoney', max_digits=15, decimal_places=3)  # Field name made lowercase.
    chkcash = models.CharField(db_column='chkCash', max_length=255)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255)  # Field name made lowercase.
    chkwithdraw = models.CharField(db_column='chkWithdraw', max_length=255)  # Field name made lowercase.
    chktransfer_in = models.CharField(db_column='chkTransfer_in', max_length=255)  # Field name made lowercase.
    chktransfer_out = models.CharField(db_column='chkTransfer_out', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=3)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15,
                                    decimal_places=3)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15,
                                      decimal_places=3)  # Field name made lowercase.
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15,
                                     decimal_places=3)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15,
                                     decimal_places=3)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15,
                                     decimal_places=3)  # Field name made lowercase.
    txtwithdraw = models.DecimalField(db_column='txtWithdraw', max_digits=15,
                                      decimal_places=3)  # Field name made lowercase.
    txttransfer_in = models.DecimalField(db_column='txtTransfer_in', max_digits=15,
                                         decimal_places=3)  # Field name made lowercase.
    txttransfer_out = models.DecimalField(db_column='txtTransfer_out', max_digits=15,
                                          decimal_places=3)  # Field name made lowercase.
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
    txtcommission = models.DecimalField(db_column='txtCommission', max_digits=15,
                                        decimal_places=3)  # Field name made lowercase.
    optioncommission = models.CharField(db_column='optionCommission', max_length=255)  # Field name made lowercase.
    mbase = models.CharField(max_length=244)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    rcode = models.IntegerField()
    echeck = models.CharField(max_length=255)
    cmbonus = models.IntegerField()

    class Meta:
        db_table = 'ali_ewallet_commission'
