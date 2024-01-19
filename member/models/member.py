from django.db import models


class Member(models.Model):
    """
    a class model represent a member profile
    """
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
    id_card_img_date = models.DateTimeField(null=True, blank=True)
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
    acc_no_img_date = models.DateTimeField(null=True, blank=True)
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
    level = models.CharField(db_column='pos_cur', max_length=255)
    pos_cur1 = models.CharField(max_length=255)
    honor = models.CharField(db_column='pos_cur2', max_length=255)
    pos_cur3 = models.CharField(max_length=255)
    pos_cur4 = models.CharField(max_length=255)
    pos_cur_tmp = models.CharField(max_length=255)
    rpos_cur4 = models.IntegerField()
    pos_cur3_date = models.DateField(null=True, blank=True)
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
    terminate_date = models.DateTimeField(null=True, blank=True)
    status_suspend = models.IntegerField()
    suspend_date = models.DateTimeField(null=True, blank=True)
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
    exp_date = models.DateField(null=True, blank=True)
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
    exp_pos = models.DateField(null=True, blank=True)
    exp_pos_60 = models.DateField(null=True, blank=True)
    trip_private = models.DecimalField(max_digits=15, decimal_places=2)
    trip_team = models.DecimalField(max_digits=15, decimal_places=2)
    myfile1 = models.CharField(max_length=255)
    myfile2 = models.CharField(max_length=255)
    cline_id = models.CharField(max_length=255)
    cfacebook_name = models.CharField(max_length=255)
    profile_img = models.CharField(max_length=255)
    atocom = models.IntegerField()
    hpv = models.DecimalField(max_digits=15, decimal_places=2)
    ocert = models.IntegerField(default=0)
    line_rgt = models.IntegerField(null=True, blank=True)
    line_lft = models.IntegerField(null=True, blank=True)
    line_depth = models.IntegerField(null=True, blank=True)
    line_center = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey('MemberGroup', on_delete=models.SET_NULL, null=True)
    distributor_date = models.DateField(null=True, blank=True)
    vat_type = models.CharField(max_length=2, choices=(
        ('VT', 'VAT'),
        ('NV', 'NONE VAT'),
    ), blank=True, null=True)
    vat_group = models.ForeignKey('ClientVatType', on_delete=models.SET_NULL, null=True, blank=True)
    favorite = models.ManyToManyField('Member', related_name='subscribe')
    agency_ref = models.ForeignKey('Member', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='agency_child')
    sponsor_lft = models.IntegerField(null=True, blank=True)
    sponsor_rgt = models.IntegerField(null=True, blank=True)
    sponsor_depth = models.IntegerField(null=True, blank=True)
    tc_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        db_table = 'ali_member'
        verbose_name_plural = 'Member'
        ordering = ['-mdate']

    def __str__(self):
        return self.mcode

    @property
    def code(self):
        """
        a method represent a member code

        :return: (str): member code
        """
        return self.mcode

    @property
    def full_name(self):
        """
        a method represent a member's name

        :return: (str): member's name
        """
        return self.name_t

    @property
    def get_level(self):
        """
        a method represent a member's level or honor

        :return: (str): member's level
        """
        if self.honor != '':
            return self.honor
        return self.level

    @property
    def get_honor(self):
        """
        a method represent a member's honor

        :return: (str): member's honor
        """
        return self.honor

    @property
    def is_terminate(self):
        """
        a method represent a member's terminate status

        :return: (str): member's terminate status
        """
        return True if self.status_terminate else False

    @property
    def is_suspend(self):
        """
        a method represent a member's suspend status

        :return: (str): member's suspend status
        """
        return True if self.status_suspend else False

    @property
    def sponsor_child(self):
        """
        a method represent a member's downlines

        :return: (:obj:`django query object`): Member objects
        """
        return Member.objects.filter(sponsor_lft__gt=self.sponsor_lft, sponsor_rgt__lt=self.sponsor_rgt)

    @property
    def status(self):
        """
        a method represent a member's status

        :return: member's status (str): [`Normal`, `Terminate`, `Suspend`]
        """
        if self.is_terminate:
            return 'Terminate'
        if self.is_suspend:
            return 'Suspend'
        return 'Normal'

    @property
    def line_pos(self):
        """
        a method represent a member's side of upline

        :return: member's side (str): [`L`, `R`]
        """
        if self.lr == '1':
            return 'L'
        else:
            return 'R'

    @property
    def child_tree_meta(self):
        """
        a method represent a member's index of tree

        :return: (:obj:`dictionary`) index of tree
        """
        return {
            'R': {
                'lft': self.line_center,
                'rgt': self.line_rgt - 1
            },
            'L': {
                'lft': self.line_lft + 1,
                'rgt': self.line_center - 1
            }
        }

    @property
    def children(self):
        """
        a method represent a member's downline

        :return: (:obj:`django queryset`) member's downline
        """
        return self.down_lines.all()

    @property
    def down_lines(self):
        """
        a method represent a member's downline

        :return: (:obj:`django queryset`) member's downline
        """
        return Member.objects.filter(line_lft__gt=self.line_lft, line_rgt__lt=self.line_rgt)

    def is_child(self, obj):
        """
        a method for verify that `other member object` have been member's downline

        :param obj: (:obj:`Member object`): member object to verify

        :return: `True` if member object have been member's downline else `False`
        """
        if obj.line_lft > self.line_lft and obj.line_rgt < self.line_rgt:
            return True
        return False

    def is_sponsor_child(self, obj):
        """
        a method for verify that `other member object` have been member's sponsor line

        :param obj: (:obj:`Member object`): member object to verify

        :return: `True` if member object have been member's sponsor line else `False`
        """
        if obj.sponsor_lft > self.sponsor_lft and obj.sponsor_rgt < self.sponsor_rgt:
            return True
        return False

    def is_child_or_self(self, obj):
        """
        a method for verify that `other member object` have been member's downline or self

        :param obj: (:obj:`Member object`): member object to verify

        :return: `True` if member object have been member's downline or self else `False`
        """
        if obj.line_lft >= self.line_lft and obj.line_rgt <= self.line_rgt:
            return True
        return False

    def is_leaf_node(self):
        """
        a method for verify member have been leaf node in downline tree

        :return: `True` if member have been leaf node in downline tree else `False`
        """
        result = self.line_rgt - self.line_lft
        if result <= 1:
            return True
        return False

    def get_group(self):
        """
        a method represent a member's group

        :return: (str): member's group name
        """
        if self.group is None:
            return 'สมาชิก'
        else:
            if self.group.name == 'Member':
                return 'สมาชิก'
            else:
                return self.group.name

    @property
    def full_address_upper(self):
        """
        a method represent a member's first half address

        :return: (str): member's first half address
        """
        _addr = self.address
        if self.districtid != ' ':
            _addr = '{} ตำบล. {}'.format(_addr, self.districtid)
        if self.amphurid != ' ':
            _addr = '{} อำเภอ.{}'.format(_addr, self.amphurid)
        return _addr

    @property
    def full_address_last(self):
        """
        a method represent a member's second half address

        :return: (str): member's second half address
        """
        _addr = ''
        if self.provinceid != ' ':
            _addr = '{}{}'.format(_addr, self.provinceid)
        if self.zip != ' ':
            _addr = '{} {}'.format(_addr, self.zip)
        return _addr

    @property
    def member_type(self):
        """
        a method represent a member type

        :return: (str): member type
        """
        strdict = {0: "MB", 1: "FR", 2: "AG"}
        return strdict[self.mtype1]

    @staticmethod
    def verify_id_card(id_card):
        """
        a method for verify an id card

        :param id_card: (str): id card

        :return: True if input id card is correct else False
        """
        result = True
        if id_card is not None:
            if len(id_card) == 13:
                start_factor = 13
                sum_value = 0
                for i in range(0, 12):
                    sum_value += int(id_card[i]) * start_factor
                    start_factor -= 1
                div = sum_value % 11
                crc = 11 - div
                if str(crc)[-1] != id_card[-1]:
                    result = False
            else:
                result = False
        elif id_card == '':
            result = False
        return result
