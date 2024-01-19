from django.db import models
from django.db.models import Sum
from ..models import Product, Promotion


class SaleInvoice(models.Model):
    """
    a class represent Sale Invoice detail
    """
    BILL_STATE_TYPE_CHOICE = (
        ('OR', 'ORDER'),
        ('PP', 'PaymentPending'),
        ('CA', 'Cancel'),
        ('CM', 'Completed'),
        ('PS', 'PrepareShip'),
        ('SH', 'Shipped')
    )

    sano = models.CharField(max_length=255, blank=True, null=True)
    pano = models.CharField(max_length=255, blank=True, null=True)
    sadate = models.DateField(max_length=255, blank=True, null=True)
    sctime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    inv_code = models.CharField(max_length=255, blank=True, null=True)
    inv_ref = models.CharField(max_length=255, blank=True, null=True)
    mcode = models.CharField(max_length=255, blank=True, null=True)
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    sp_code = models.CharField(max_length=255, blank=True, null=True)
    sp_pos = models.CharField(max_length=10, blank=True, null=True)
    name_f = models.CharField(max_length=255, blank=True, null=True)
    name_t = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_vat = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_net = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_invat = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_exvat = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    customer_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_pv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tot_bv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tot_fv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_sppv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tot_weight = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    usercode = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    trnf = models.IntegerField(blank=True, null=True)
    sa_type = models.CharField(max_length=2, blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    uid_branch = models.CharField(max_length=20, blank=True, null=True)
    lid = models.CharField(max_length=255, blank=True, null=True)
    dl = models.CharField(max_length=1, blank=True, null=True)
    cancel = models.IntegerField(blank=True, null=True)
    send = models.IntegerField(blank=True, null=True)  # { 0: register bill, 1: send, 2: don't send }
    txtoption = models.TextField(blank=True, null=True)
    chkcash = models.CharField(db_column='chkCash', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chkfuture = models.CharField(db_column='chkFuture', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    chktransfer = models.CharField(db_column='chkTransfer', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    chkcredit1 = models.CharField(db_column='chkCredit1', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    chkcredit2 = models.CharField(db_column='chkCredit2', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    chkcredit3 = models.CharField(db_column='chkCredit3', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    chkcredit4 = models.CharField(db_column='chkCredit4', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    chkinternet = models.CharField(db_column='chkInternet', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    chkdiscount = models.CharField(db_column='chkDiscount', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    chkother = models.CharField(db_column='chkOther', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    txtcash = models.DecimalField(db_column='txtCash', max_digits=15, decimal_places=2, blank=True,
                                  null=True)  # Field name made lowercase.
    txtfuture = models.DecimalField(db_column='txtFuture', max_digits=15,
                                    decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txttransfer = models.DecimalField(db_column='txtTransfer', max_digits=15,
                                      decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ewallet = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    txtcredit1 = models.DecimalField(db_column='txtCredit1', max_digits=15,
                                     decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txtcredit2 = models.DecimalField(db_column='txtCredit2', max_digits=15,
                                     decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txtcredit3 = models.DecimalField(db_column='txtCredit3', max_digits=15,
                                     decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txtcredit4 = models.DecimalField(db_column='txtCredit4', max_digits=15,
                                     decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txtinternet = models.DecimalField(db_column='txtInternet', max_digits=15,
                                      decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txtdiscount = models.DecimalField(db_column='txtDiscount', max_digits=15,
                                      decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    txtother = models.DecimalField(db_column='txtOther', max_digits=15, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    txtsending = models.DecimalField(db_column='txtSending', max_digits=15,
                                     decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    optioncash = models.CharField(db_column='optionCash', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    optionfuture = models.CharField(db_column='optionFuture', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    optiontransfer = models.CharField(db_column='optionTransfer', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    optioncredit1 = models.CharField(db_column='optionCredit1', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    optioncredit2 = models.CharField(db_column='optionCredit2', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    optioncredit3 = models.CharField(db_column='optionCredit3', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    optioncredit4 = models.CharField(db_column='optionCredit4', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    optioninternet = models.CharField(db_column='optionInternet', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    optiondiscount = models.CharField(db_column='optionDiscount', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    optionother = models.CharField(db_column='optionOther', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    discount = models.CharField(max_length=255, blank=True, null=True)
    print = models.IntegerField(blank=True, null=True)
    ewallet_before = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ewallet_after = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ipay = models.CharField(max_length=255, blank=True, null=True)
    pay_type = models.CharField(max_length=255, blank=True, null=True)
    hcancel = models.IntegerField(blank=True, null=True)
    caddress = models.TextField(blank=True, null=True)
    cdistrictid = models.CharField(db_column='cdistrictId', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    camphurid = models.CharField(db_column='camphurId', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    cprovinceid = models.CharField(db_column='cprovinceId', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    czip = models.CharField(max_length=255, blank=True, null=True)
    sender = models.IntegerField(blank=True, null=True)
    sender_date = models.DateField(blank=True, null=True)
    receive = models.IntegerField(blank=True, null=True)
    receive_date = models.DateField(blank=True, null=True)
    asend = models.IntegerField(blank=True, null=True)
    ato_type = models.IntegerField(blank=True, null=True)
    ato_id = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    hpv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    htotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    hdate = models.DateField(blank=True, null=True)
    scheck = models.CharField(max_length=255, blank=True, null=True)
    checkportal = models.IntegerField(blank=True, null=True)
    rcode = models.IntegerField(blank=True, null=True)
    bmcauto = models.IntegerField(blank=True, null=True)
    cancel_date = models.DateTimeField(blank=True, null=True)
    uid_cancel = models.CharField(max_length=255, blank=True, null=True)
    cname = models.CharField(max_length=255, blank=True, null=True)
    cmobile = models.CharField(max_length=255, blank=True, null=True)
    uid_sender = models.CharField(max_length=255, blank=True, null=True)
    uid_receive = models.CharField(max_length=255, blank=True, null=True)
    mbase = models.CharField(max_length=255, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    locationbase = models.IntegerField(blank=True, null=True)
    crate = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=100, blank=True, null=True)
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
    selectdiscount = models.CharField(db_column='selectDiscount', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    selectinternet = models.CharField(db_column='selectInternet', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    txtvoucher = models.DecimalField(db_column='txtVoucher', max_digits=15,
                                     decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    optionvoucher = models.CharField(db_column='optionVoucher', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    selectvoucher = models.CharField(db_column='selectVoucher', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    txttransfer1 = models.CharField(db_column='txtTransfer1', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    optiontransfer1 = models.CharField(db_column='optionTransfer1', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    selecttransfer1 = models.CharField(db_column='selectTransfer1', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    txttransfer2 = models.CharField(db_column='txtTransfer2', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    optiontransfer2 = models.CharField(db_column='optionTransfer2', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    selecttransfer2 = models.CharField(db_column='selectTransfer2', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    txttransfer3 = models.CharField(db_column='txtTransfer3', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    optiontransfer3 = models.CharField(db_column='optionTransfer3', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    selecttransfer3 = models.CharField(db_column='selectTransfer3', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    status_package = models.IntegerField(blank=True, null=True)
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
    bill_state = models.CharField(max_length=4, choices=BILL_STATE_TYPE_CHOICE, blank=True, null=True)
    order_number = models.CharField(max_length=64, null=True, blank=True)
    credit_note_number = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'ali_asaleh'
        verbose_name_plural = 'Sale Invoice'
        ordering = ('-sadate',)

    def __str__(self):
        return '{}:{}:{}'.format(self.bill_number, self.mcode, self.name_t)

    @staticmethod
    def get_daily_sales(current_date, bill_type):
        """
        a method get summary total of each branch in date

        :param current_date: (:obj:`datetime`)

        :param bill_type: (str): string code that identify bill type

        :return: (:obj:`django queryset`) summary total `Sale Invoice` of each branch in date
        """
        query_set = SaleInvoice.objects.filter(sadate=current_date, sa_type__in=bill_type, cancel=0) \
            .values('inv_code').annotate(total=Sum('total')).order_by('inv_code')
        return query_set

    @property
    def box_size(self):
        """
        Shipment box size of this invoice
        :return: (str): Shipment box size
        """
        return self.pano if self.pano else "L"

    @property
    def full_address_upper(self):
        """
        a method represent first half delivery address

        :return: (str): First half delivery address
        """
        _addr = self.caddress
        if self.cdistrictid != ' ':
            _addr = '{} ตำบล. {}'.format(_addr, self.cdistrictid)
        if self.camphurid != ' ':
            _addr = '{} อำเภอ.{}'.format(_addr, self.camphurid)
        return _addr

    @property
    def full_address_last(self):
        """
        a method represent second half delivery address

        :return: (str): Second half delivery address
        """
        _addr = ''
        if self.cprovinceid != ' ':
            _addr = '{} {}'.format(_addr, self.cprovinceid)
        if self.czip != ' ':
            _addr = '{} {}'.format(_addr, self.czip)
        return _addr

    @property
    def bill_number(self):
        """
        a method reprsent a bill number

        :return: (str): bill number
        """
        return self.sano

    def get_payments(self):
        """
        a method represent bill payment type and amount

        :return: (:obj:`dictionary`): bill payment detail
        """
        pool = {'type': 'เงินสด'}
        if self.txtcash:
            pool['cash'] = {
                'name': 'เงินสด',
                'value': self.txtcash,
                'option': self.optioncash
            }
        if self.txttransfer:
            pool['type'] = 'โอนเงิน'
            pool['transfer'] = {
                'name': 'โอนเงิน',
                'value': self.txttransfer,
                'option': self.optiontransfer
            }
        if self.txtcredit1:
            pool['type'] = 'เครดิต'
            pool['credit'] = {
                'name': 'เครดิต',
                'value': self.txtcredit1,
                'option': self.optioncredit1
            }
        if self.txttc:
            pool['type'] = 'เครดิต'
            pool['tc'] = {
                'name': 'เครดิดท่องเที่ยว',
                'value': self.txttc,
                'option': self.optiontc
            }
        if self.txtinternet:
            pool['type'] = 'เครดิต'
            pool['credit'] = {
                'name': 'Payment Gateway',
                'value': self.txtinternet,
                'option': self.optioninternet
            }
        return pool

    @property
    def create_by(self):
        """
        a method represent a user id who create a sale invoice

        :return: (int): user id
        """
        return self.uid

    @property
    def create_time(self):
        """
        a method represent when the invoice is created

        :return: (:obj:`datetime`): datetime that sale invoice created
        """
        return self.sctime

    @property
    def bill_weight(self):
        """
        a method represent summary weight's item in bill

        :return: (float): weight in kilogram unit
        """
        goods = self.items.all()
        pcode_list = goods.values_list("pcode", flat=True)
        weight_dict = {}
        sum_weight = 0.0
        for p in Product.objects.filter(pcode__in=pcode_list).values("pcode", "weight"):
            weight_dict[p["pcode"]] = float(p["weight"])
        for pm in Promotion.objects.filter(pcode__in=pcode_list).values("pcode", "weight"):
            weight_dict[pm["pcode"]] = float(pm["weight"])
        for i in goods:
            sum_weight += (float(i.qty) * weight_dict[i.pcode])
        return sum_weight / 1000
