from collections import OrderedDict
from django.db.models import Sum
from commission.models import MonthPayment
from commission.serializers import MonthPaymentSerializer
from core.report.summary import PeriodSummaryBase
from .week_payment import ExcelWeekPayment
from member.models import Member


class MonthPaymentReport(PeriodSummaryBase):
    """
    a class represent member's monthly commission payment
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): (Optional) member code of interested person
        sum (boolean): (Optional) force data return in summary default is False
    """
    class Meta:
        model = MonthPayment
        date_fields = 'date_issue'

    def __init__(self, *args, **kwargs):
        super(MonthPaymentReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', 'monthly')
        self.mcode = kwargs.get('mcode', None)
        self.sum = kwargs.get('sum', False)

    def get_extend_queryset(self, queryset):
        """
        a method for filter queryset data

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        queryset = queryset.filter(paid_state='1')
        if self.mcode:
            queryset = queryset.filter(mcode=self.mcode)

        if self.sum is True:
            queryset = queryset.values('time', 'mcode', 'name_t').annotate(
                sum_total=Sum('total'),).order_by('-sum_total', 'mcode')
        return queryset

    @property
    def summary(self):
        """
        a method to process data return in summary data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            member_code = x['mcode']
            if member_code not in pool:
                pool[member_code] = {
                    'mcode': x['mcode'],
                    'name': x['name_t'],
                    'data': {}
                }

            data = x['sum_total']

            if self.get_type == 'daily':
                pool[member_code]['data'][x['time'].strftime('%Y-%m-%d')] = data
            elif self.get_type == 'monthly':
                pool[member_code]['data'][x['time'].strftime('%Y-%b')] = data
            elif self.get_type == 'quarter':
                pool[member_code]['data'][x['time'].strftime('%Y-%b')] = data
            elif self.get_type == 'yearly':
                pool[member_code]['data'][x['time'].strftime('%Y')] = data
        return pool

    @property
    def total(self):
        """
        a method to process data and reform to dictionary

        :return: (:obj:`dictionary`)
        """
        pool = {'personal': [], 'company_with_vat': [], 'company_no_vat': []}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        members = {x.mcode: x for x in Member.objects.filter(mcode__in=[y.mcode for y in queryset])}
        for x in queryset:
            m = members[x.mcode]
            if m.mtype == 1 and m.mvat == 1:
                pool['company_with_vat'].append(x)
            elif m.mtype == 1 and m.mvat == 0:
                pool['company_no_vat'].append(x)
            else:
                pool['personal'].append(x)
        return pool


class ExcelMonthPayment(ExcelWeekPayment):
    """
    a class for generate excel object that represent member's monthly commission payment.
    Excel object can save to an excel file or response via http request file.
    This class inherit class `ExcelWeekPayment` also you can use a method in ExcelWeekPayment or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): (Optional) member code of interested person
        sum (boolean): (Optional) force data return in summary default is False
    """
    class Meta:
        title = 'รายงาน Month Payment'
        file_name = 'month_payment'
        head_file = 'Month Payment'
        content_start_col = 1
        content_start_row = 8
        head_start_col = 2
        head_start_row = 7
        head = {
            'fields': ['mcode', 'name_t', 'mobile', 'email', 'address', 'id_card', 'id_tax', 'total', 'total_vat',
                       'transfer_fee', 'actual_pay']
        }

    def __init__(self, *args, **kwargs):
        super(ExcelMonthPayment, self).__init__(*args, **kwargs)
        self.report = MonthPaymentReport(*args, **kwargs)

    def build_row_meta(self, row_index, data, **kwargs):
        """
        a method for index data with cell row

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :return: (:obj:`dictionary`)
        """
        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']})
        ])
        new_row = row_index + self.Meta.content_start_row - 1
        for i in self.Meta.head['fields']:
            if i == 'address':
                meta.update({i: {
                    'data': data['member_info']['full_address_upper'] + data['member_info']['full_address_last'],
                    'alignment': self.style['align_center']}})
            elif i == 'email':
                meta.update({i: {'data': data['member_info']['email'], 'alignment': self.style['align_center']}})
            elif i == 'transfer_fee':
                meta.update({i: {'data': 30, 'alignment': self.style['align_center']}})
            elif i == 'total_vat':
                if data['member_info']['mtype'] == 1:
                    meta.update({i: {'data': "=ROUND((I" + str(new_row) + "-K" + str(new_row) + ")*0.03, 2)",
                                     'alignment': self.style['align_center']}})
                else:
                    meta.update({i: {'data': "=ROUND((I" + str(new_row) + "-K" + str(new_row) + ")*0.05, 2)",
                                     'alignment': self.style['align_center']}})
            elif i == 'actual_pay':
                if data['member_info']['mvat'] == 1:
                    meta.update({i: {'data': "=(I" + str(new_row) + "-K" + str(new_row) + "+ROUND((I" + str(
                        new_row) + "-K" + str(new_row) + ")*0.07, 2)-J" + str(new_row) + ")",
                                     'alignment': self.style['align_center']}})
                else:
                    meta.update(
                        {i: {'data': "=(I" + str(new_row) + "-K" + str(new_row) + "-J" + str(new_row) + ")",
                             'alignment': self.style['align_center']}})
            else:
                if i == 'name_t' and data['name_t'] == '':
                    meta.update({i: {'data': data['member_info']['name'], 'alignment': self.style['align_center']}})
                elif i == 'mobile':
                    meta.update({i: {'data': data['member_info']['mobile'], 'alignment': self.style['align_center']}})
                else:
                    meta.update({i: {'data': data[i], 'alignment': self.style['align_center']}})
        return meta

    def process_data(self):
        """
        a method to process data in excel object by call method `create_head` and `fill_row`
        """
        source = self.wb.active
        source.title = 'personal'
        self.create_head(source)
        for nm in ['company_with_vat', 'company_no_vat']:
            target = self.wb.copy_worksheet(source)
            target.title = nm
            self.create_head(target)
        for sheet_name, data_list in self.report.total.items():
            self.wb.active = self.wb.get_index(self.wb[sheet_name])
            count = 1
            current_row = self.Meta.content_start_row
            for v in MonthPaymentSerializer(data_list, many=True).data:
                count = self.fill_row(count, v, row=current_row)
                current_row += 1

