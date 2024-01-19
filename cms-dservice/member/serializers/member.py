from rest_framework import serializers
from commission.report.holdpv_activity import PvActivityReport
from datetime import date, datetime
from ..models import Member
from commission.models import PvTransfer, MonthQualified, WeakStrongSummary, WeakStrongCurrentRoundStack
from ecommerce.models import SaleInvoice
from django.db.models import Sum


class MemberShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'honor', 'level', 'mcode', 'name_t', 'name_b', 'mobile', 'email', 'address', 'districtid',
                  'amphurid', 'provinceid', 'zip', 'line_id', 'status_terminate', 'status_suspend')


class MemberSerializer(serializers.ModelSerializer):
    member_code = serializers.CharField(source='mcode')
    name = serializers.CharField(source='name_t')
    hold_pv = serializers.CharField(source='hpv')
    district = serializers.CharField(source='districtid')
    amphur = serializers.CharField(source='amphurid')
    province = serializers.CharField(source='provinceid')
    post_code = serializers.CharField(source='zip')
    register_date = serializers.CharField(source='mdate')
    id_card = serializers.CharField(source='cmp')
    book_bank = serializers.CharField(source='cmp2')

    class Meta:
        model = Member
        fields = (
            'id', 'member_code', 'name', 'register_date', 'mobile', 'email', 'level', 'honor', 'hold_pv', 'address',
            'district', 'amphur', 'province', 'post_code', 'id_card', 'book_bank', 'full_address_upper',
            'full_address_last', 'mtype', 'mvat')

    def to_representation(self, instance):
        data = super(MemberSerializer, self).to_representation(instance)
        context = self.context
        if 'favorite' in context:
            if instance.code in context.get('favorite'):
                data['favorite'] = True
            else:
                data['favorite'] = False

        if 'head_member' in context:
            expect_list = ['PE', 'SE', 'EE', 'DE', 'CE']
            head_member = self.context.get('head_member')
            if head_member.honor in expect_list:
                if instance.honor in expect_list:
                    data['hold_pv'] = 0
                if instance.member_type != 'MB':
                    data['hold_pv'] = 0
            else:
                data['hold_pv'] = 0
        return data


class MemberChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('mcode', 'name_t',)


class MemberStatusSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    member_type = serializers.ReadOnlyField()
    group = serializers.SerializerMethodField()
    dis_qualified = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ('mcode', 'name_t', 'status', 'mobile', 'ocert', 'member_type', 'group', 'dis_qualified')

    def get_group(self, obj):
        return obj.get_group()

    def get_dis_qualified(self, obj):
        result = {
            'total': 0,
            'qualify': False,
            'group': 'MB',
            'require': 0
        }
        if obj.group is not None:
            start, end = PvActivityReport.get_month_range(date.today())
            total = 0
            pv_bought = PvActivityReport(start=start, end=end, get_type='monthly', mem_code=obj.code).result
            child_sale = SaleInvoice.objects.filter(sadate__range=(start, end), cancel=0, sa_type='H',
                                                    member__agency_ref=obj, inv_code='BKK02') \
                .aggregate(total=Sum('tot_pv'))

            child_sale_total = child_sale['total']

            if child_sale_total is None:
                child_sale_total = 0
            else:
                child_sale_total = float(child_sale_total)

            for k, v in pv_bought.items():
                total = v['in'] + v['transfer']
            result['total'] = total + child_sale_total
            result['qualify'] = total >= obj.group.status_qualified
            result['group'] = obj.group.code
            result['require'] = obj.group.status_qualified

        return result


class MemberDashboardSerializer(serializers.ModelSerializer):
    pv_collection = serializers.SerializerMethodField()
    pv_month_collection = serializers.SerializerMethodField()
    sum_month_weak = serializers.SerializerMethodField()
    prev_pv = serializers.SerializerMethodField()
    current_pv = serializers.SerializerMethodField()
    month_qualified = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = (
            'id', 'mcode', 'mdate', 'hpv', 'upa_code', 'upa_name', 'sp_code', 'sp_name', 'bmdate1', 'bmdate2',
            'bmdate3', 'cmp', 'cmp2', 'cmp3', 'pv_collection', 'pv_month_collection', 'sum_month_weak', 'prev_pv',
            'current_pv', 'month_qualified')

    def get_pv_collection(self, obj):
        temp1 = SaleInvoice.objects.filter(mcode=obj.mcode, cancel=0).aggregate(sum_pv=Sum('tot_pv'))
        temp2 = PvTransfer.objects.filter(mcode=obj.mcode, cancel=0).aggregate(sum_pv=Sum('tot_pv'))
        if temp1['sum_pv'] and temp2['sum_pv']:
            return temp1['sum_pv'] + temp2['sum_pv']
        elif temp1['sum_pv']:
            return temp1['sum_pv']
        else:
            return temp2['sum_pv']

    def get_pv_month_collection(self, obj):
        td = date.today()
        temp1 = SaleInvoice.objects.filter(mcode=obj.mcode, cancel=0, sadate__month=td.month,
                                           sadate__year=td.year).aggregate(sum_pv=Sum('tot_pv'))
        temp2 = PvTransfer.objects.filter(mcode=obj.mcode, cancel=0, sadate__month=td.month,
                                          sadate__year=td.year).aggregate(sum_pv=Sum('tot_pv'))
        if temp1['sum_pv'] and temp2['sum_pv']:
            return temp1['sum_pv'] + temp2['sum_pv']
        elif temp1['sum_pv']:
            return temp1['sum_pv']
        else:
            return temp2['sum_pv']

    def get_sum_month_weak(self, obj):
        td = date.today()
        temp = WeakStrongSummary.objects.filter(mcode=obj.mcode, date_issue__month=td.month,
                                                date_issue__year=td.year).aggregate(sum_balance=Sum('balance'))
        if temp['sum_balance']:
            return temp['sum_balance']
        else:
            return 0

    def get_prev_pv(self, obj):
        temp = WeakStrongSummary.objects.filter(mcode=obj.mcode).last()
        return {'prev_left': temp.previous_left, 'prev_right': temp.previous_right}

    def get_current_pv(self, obj):
        current_left_pv, current_right_pv = 0, 0
        td = date.today()
        tleft = WeakStrongCurrentRoundStack.objects.filter(upa_code=obj.mcode, tdate__gt=td, lr=0)
        for t in tleft:
            if t.fdate < td < t.tdate:
                current_left_pv += t.pv
        tright = WeakStrongCurrentRoundStack.objects.filter(upa_code=obj.mcode, tdate__gt=td, lr=1)
        for t in tright:
            if t.fdate < td < t.tdate:
                current_right_pv += t.pv
        return {'current_left': current_left_pv, 'current_right': current_right_pv}

    def get_month_qualified(self, obj):
        td = date.today()
        instance = MonthQualified.objects.filter(mcode=obj.mcode).last()
        if instance.mdate.month == td.month and instance.mdate.year == td.year:
            return True
        else:
            return False

