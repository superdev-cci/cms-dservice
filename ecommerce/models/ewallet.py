from django.db import models


class Ewallet(models.Model):
    sano = models.CharField(unique=True, max_length=255, blank=True, null=True)
    rcode = models.IntegerField()
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    name_f = models.CharField(max_length=255)
    name_t = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=255)
    trnf = models.CharField(max_length=1, blank= True, null=True)
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
    txtdiscount = models.DecimalField(db_column='txtDiscount', max_digits=15,
                                      decimal_places=2)  # Field name made lowercase.
    chktransfer_in = models.CharField(db_column='chkTransfer_in', max_length=255)  # Field name made lowercase.
    chktransfer_out = models.CharField(db_column='chkTransfer_out', max_length=255)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15,
                                    decimal_places=2)  # Field name made lowercase.
    txtinternet = models.DecimalField(db_column='txtInternet', max_digits=15,
                                      decimal_places=2)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15,
                                      decimal_places=2)  # Field name made lowercase.
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15,
                                     decimal_places=2)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15,
                                     decimal_places=2)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15,
                                     decimal_places=2)  # Field name made lowercase.
    txtwithdraw = models.DecimalField(db_column='txtWithdraw', max_digits=15,
                                      decimal_places=2)  # Field name made lowercase.
    txttransfer_in = models.DecimalField(db_column='txtTransfer_in', max_digits=15,
                                         decimal_places=2)  # Field name made lowercase.
    txttransfer_out = models.DecimalField(db_column='txtTransfer_out', max_digits=15,
                                          decimal_places=2)  # Field name made lowercase.
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
                                        decimal_places=2)  # Field name made lowercase.
    optioncommission = models.CharField(db_column='optionCommission', max_length=255)  # Field name made lowercase.
    mbase = models.CharField(max_length=244)
    crate = models.DecimalField(max_digits=11, decimal_places=6)
    echeck = models.CharField(max_length=255)
    sano_temp = models.CharField(max_length=255)
    selectcash = models.CharField(db_column='selectCash', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    selecttransfer = models.CharField(db_column='selectTransfer', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    selectcredit1 = models.CharField(db_column='selectCredit1', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    selectcredit2 = models.CharField(db_column='selectCredit2', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    selectcredit3 = models.CharField(db_column='selectCredit3', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    selectinternet = models.CharField(db_column='selectInternet', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    txttransfer1 = models.DecimalField(db_column='txtTransfer1', max_digits=15, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    optiontransfer1 = models.CharField(db_column='optionTransfer1', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    selecttransfer1 = models.CharField(db_column='selectTransfer1', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    txttransfer2 = models.DecimalField(db_column='txtTransfer2', max_digits=15, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    optiontransfer2 = models.CharField(db_column='optionTransfer2', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    selecttransfer2 = models.CharField(db_column='selectTransfer2', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    txttransfer3 = models.DecimalField(db_column='txtTransfer3', max_digits=15, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    optiontransfer3 = models.CharField(db_column='optionTransfer3', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    selecttransfer3 = models.CharField(db_column='selectTransfer3', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    image_transfer = models.TextField()
    txtvoucher = models.DecimalField(db_column='txtVoucher', max_digits=15,
                                     decimal_places=2)  # Field name made lowercase.
    id_ecom = models.CharField(max_length=255)
    cals = models.CharField(max_length=255)
    txtpremium = models.DecimalField(db_column='txtPremium', max_digits=15, decimal_places=2, blank=True,
                                     null=True)  # Field name made lowercase.
    chkpremium = models.CharField(db_column='chkPremium', max_length=8, blank=True,
                                  null=True)  # Field name made lowercase.
    selectpremium = models.CharField(db_column='selectPremium', max_length=8, blank=True,
                                     null=True)  # Field name made lowercase.
    optionpremium = models.CharField(db_column='optionPremium', max_length=128, blank=True,
                                     null=True)  # Field name made lowercase.
    txttc = models.DecimalField(db_column='txttc', max_digits=15, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    chktc = models.CharField(db_column='chktc', max_length=8, blank=True,
                             null=True)  # Field name made lowercase.
    selecttc = models.CharField(db_column='selecttc', max_length=8, blank=True,
                                null=True)  # Field name made lowercase.
    optiontc = models.CharField(db_column='optiontc', max_length=128, blank=True,
                                null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'ali_ewallet'
