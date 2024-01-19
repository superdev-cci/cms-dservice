import datetime
from collections import OrderedDict
from datetime import date
from django.db.models import Prefetch, Sum
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1, BUILTIN_FORMATS

from core.report.excel import ExcelTemplateReport
from core.report.summary import ExcelMonthSummaryReport
from ecommerce.models import SaleInvoice


class SoldMonthlyPaymentSummary(ExcelMonthSummaryReport):
    template_file = './templates/report/ecommerce/sold_summary.xlsx'
    select_bill = ('A', 'H', 'L', 'B', 'PM')

    class Meta:
        title = 'Sold summary'
        sheet_name = 'Summary'
        file_name = 'sold_payment_summary'
        head_file = 'Sold summary'
        head_start_col = 3
        head_start_row = 7
        head = {
            'fields': ['CASH', 'TRANSFER', 'CREDIT', 'VOUCHER', 'T2P', 'TC','TOTAL']
        }
        content_start_col = 1
        content_start_row = 8

    def __init__(self, **kwargs):
        super(SoldMonthlyPaymentSummary, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        if isinstance(self.start, str):
            self.start = datetime.datetime.strptime(self.start, '%Y-%m-%d').date()

        self.end = kwargs.get('end', None)
        if isinstance(self.end, str):
            self.end = datetime.datetime.strptime(self.end, '%Y-%m-%d').date()

    def create_head(self, *args):

        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')
        Meta = self.Meta
        start_row = Meta.head_start_row
        start_col = Meta.head_start_col
        for x in Meta.head['fields']:
            self.work_sheet.cell(row=start_row, column=start_col).value = x
            start_col += 1

    def build_row_meta(self, row_index, data, date_issue, **kwargs):
        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('date', {'data': date_issue, 'alignment': self.style['align_center']}),
            ('cash', {
                'data': data['cash'],
                'number_format': BUILTIN_FORMATS[3]
            }),
            ('transfer', {
                'data': data['transfer'],
                'number_format': BUILTIN_FORMATS[3]
            }),
            ('credit', {
                'data': data['credit'],
                'number_format': BUILTIN_FORMATS[3]
            }),
            ('voucher', {
                'data': data['voucher'],
                'number_format': BUILTIN_FORMATS[3]
            }),
            ('t2p', {
                'data': data['t2p'],
                'number_format': BUILTIN_FORMATS[3]
            }),
            ('TC', {
                'data': data['tc'],
                'number_format': BUILTIN_FORMATS[3]
            }),
            ('total', {
                'data': data['total'],
                'number_format': BUILTIN_FORMATS[3]
            }),
        ])
        return meta

    def get_query_set(self, date_issue):
        start, end = self.calculate_period(date_issue)
        query_set = SaleInvoice.objects.filter(sadate__range=(start, end),
                                               sa_type__in=self.select_bill,
                                               ).exclude(cancel=1) \
            .aggregate(total=Sum('total'), cash=Sum('txtcash'), transfer=Sum('txttransfer'),
                       credit=Sum('txtcredit1'), voucher=Sum('txtvoucher'), t2p=Sum('txtinternet'), tc=Sum('txttc'))
        # query_set = query_set.select_related('bill_type', 'member', 'create_by__user', 'branch')

        return query_set

    def fill_sum_row(self, last_row):
        current_col = self.Meta.content_start_col + 5
        start_row = self.Meta.content_start_row
        cell = self.get_cell(current_col, last_row)

        for i in range(current_col, current_col + 7):
            cell_range = self.get_string_cell_range(i, start_row, i, last_row - 1)
            cell.value = '=SUM({})'.format(cell_range)
            cell.number_format = FORMAT_NUMBER_COMMA_SEPARATED1
            self.apply_border(cell)
            cell = self.next_cell(cell, 1, 0)

        return

    def process_data(self):
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        pool = {}
        m_range = self._calculate_month_range(self.start, self.end)
        for x in m_range:
            current = x.strftime('%Y-%b')
            # print(current)
            query_set = self.get_query_set(x)
            pool[current] = query_set
        #
        for k, v in pool.items():
            # print('{}: {}'.format(k, v))
            self.fill_row(count, v, k, row=current_row)
            count += 1
            current_row += 1

        return

    @property
    def file_name(self):
        name = '{}'.format(self.Meta.file_name)
        return '{}.xlsx'.format(name)
