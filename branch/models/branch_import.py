from django.db import models


class BranchImportStock(models.Model):
    sano = models.IntegerField(blank=True, null=True)
    sadate = models.DateField(blank=True, null=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_code_to = models.CharField(max_length=255)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2)
    usercode = models.CharField(max_length=3, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)
    trnf = models.CharField(max_length=1, blank=True, null=True)
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
    discount = models.IntegerField()
    sender = models.IntegerField()
    sender_date = models.DateField()
    receive = models.IntegerField()
    receive_date = models.DateField()
    print = models.IntegerField()
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2)
    ewallett_before = models.DecimalField(max_digits=15, decimal_places=2)
    ewallett_after = models.DecimalField(max_digits=15, decimal_places=2)
    cancel_date = models.DateField()
    uid_cancel = models.CharField(max_length=255)

    class Meta:
        db_table = 'ali_import_stock_h'


class BranchImportStockItem(models.Model):
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
        db_table = 'ali_import_stock_d'