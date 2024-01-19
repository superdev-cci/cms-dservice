import datetime
from collections import OrderedDict
from datetime import date
from functools import reduce

from django.db.models import Prefetch, Sum
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from core.report.excel import ExcelTemplateReport
from core.report.summary import ExcelMonthSummaryReport
from ecommerce.models import SaleInvoice


class SoldMonthlySummary(ExcelMonthSummaryReport):
    template_file = './templates/report/ecommerce/sold_summary.xlsx'
    select_bill = ('A', 'H', 'L', 'B', 'PM', 'WI')

    # select_bill = ('A', 'H', 'L', 'B')
    class Meta:
        title = 'Sold summary'
        sheet_name = 'Summary'
        file_name = 'sold_monthly_summary'
        head_file = 'Sold summary'
        head_start_col = 3
        head_start_row = 7
        head = {
            'fields': ['BKK01', 'KL01', 'HY01', 'CRI01', 'DROPSHIP', 'Summary']
        }
        content_start_col = 1
        content_start_row = 8

    def __init__(self, **kwargs):
        super(SoldMonthlySummary, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        if isinstance(self.start, str):
            self.start = datetime.datetime.strptime(self.start, '%Y-%m-%d').date()
        elif self.start is None:
            self.start = datetime.date.today()

        self.end = kwargs.get('end', None)
        if isinstance(self.end, str):
            self.end = datetime.datetime.strptime(self.end, '%Y-%m-%d').date()
        elif self.end is None:
            self.end = datetime.date.today()

    @property
    def total(self):
        pool = {}
        m_range = self._calculate_month_range(self.start, self.end)
        for x in m_range:
            current = x.strftime('%Y-%b')
            # print(current)
            query_set = self.get_query_set(x)
            total_tc = 0
            pool[current] = {}
            for x1 in query_set:
                if x1['tc'] is None:
                    tc = 0
                else:
                    tc = float(x1['tc'])
                if current in pool:
                    pool[current][x1['inv_code']] = float(x1['total']) - float(x1['premium']) - tc
                else:
                    pool[current] = {
                        x1['inv_code']: float(x1['total']) - float(x1['premium']) - tc
                    }
                total_tc += tc
            for x1 in self.Meta.head['fields']:
                if x1 not in pool[current]:
                    pool[current][x1] = 0

            total = reduce(lambda x2, y: x2 + y, pool[current].values(), 0)
            pool[current]['total'] = total
            pool[current]['tc'] = total_tc

        return pool

    @property
    def monthly_summary(self):
        pool = self.total
        current = self.start.strftime('%Y-%b')
        return pool[current]['total']

    @property
    def monthly_summary_tc(self):
        pool = self.total
        current = self.start.strftime('%Y-%b')
        return pool[current]['tc']

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
            ('BKK01', {
                'data': data['BKK01'],
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1
            }),
            ('KL01', {
                'data': data['KL01'],
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1
            }),
            ('HY01', {
                'data': data['HY01'],
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1
            }),
            ('CRI01', {
                'data': data['CRI01'],
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1
            }),
            ('DROPSHIP', {
                'data': data.get('BKK02', 0),
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1
            }),
        ])
        return meta

    def get_query_set(self, date_issue):
        start, end = self.calculate_period(date_issue)
        query_set = SaleInvoice.objects.filter(sadate__range=(start, end),
                                               sa_type__in=self.select_bill,
                                               ).exclude(cancel=1) \
            .values('inv_code') \
            .annotate(total=Sum('total'), premium=Sum('txtpremium'), tc=Sum('txttc')) \
            .order_by('inv_code')

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
        pool = self.total

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
