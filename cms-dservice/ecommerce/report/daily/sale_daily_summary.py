import datetime
from collections import OrderedDict
from datetime import date
from django.db.models import Prefetch, Sum
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from core.report.excel import ExcelTemplateReport
from ecommerce.models import SaleInvoice


class SoldDailySummary(ExcelTemplateReport):
    """
    a class represent summary sold product each branch
    This class inherit class `ExcelTemplateReport` also you can use a method in ExcelTemplateReport or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
    """
    template_file = './templates/report/ecommerce/sold_summary.xlsx'
    select_bill = ("A", "H", "L", "B", "WI")

    class Meta:
        title = 'Sold summary'
        sheet_name = 'Summary'
        file_name = 'sold_summary'
        head_file = 'Sold summary'
        head_start_col = 3
        head_start_row = 7
        head = {
            'fields': ['BKK01', 'KL01', 'HY01', 'CRI01', 'DROPSHIP', 'Summary']
        }
        content_start_col = 1
        content_start_row = 8

    def __init__(self, **kwargs):
        super(SoldDailySummary, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        if isinstance(self.start, str):
            self.start = datetime.datetime.strptime(self.start, '%Y-%m-%d').date()
        self.end = kwargs.get('end', None)
        if isinstance(self.end, str):
            self.end = datetime.datetime.strptime(self.end, '%Y-%m-%d').date()

    def create_head(self):
        """
        a method to process data to create Header of table in excel
        """
        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')
        super(SoldDailySummary, self).create_head()

    def build_row_meta(self, row_index, data, date_issue, **kwargs):
        """
        a method for index data with cell row

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :param date_issue: (str) string in date format

        :return: (:obj:`dictionary`)
        """
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
        """
        a method for process an information of SaleInvoice in interesting date

        :param date_issue: (str): string in date format

        :return: (:obj:`dictionary`)
        """
        query_set = SaleInvoice.objects.filter(sadate=date_issue, sa_type__in=self.select_bill).exclude(cancel=1) \
            .values('inv_code').annotate(total=Sum('total'), total_tc=Sum('txttc')).order_by('inv_code')
        return query_set

    def fill_sum_row(self, last_row):
        """
        a method for write summary data to last row

        :param last_row: index that identify last row
        """
        current_col = self.Meta.content_start_col + 5
        start_row = self.Meta.content_start_row
        cell = self.get_cell(current_col, last_row)
        for i in range(current_col, current_col + 7):
            cell_range = self.get_string_cell_range(i, start_row, i, last_row - 1)
            cell.value = '=SUM({})'.format(cell_range)
            cell.number_format = FORMAT_NUMBER_COMMA_SEPARATED1
            self.apply_border(cell)
            cell = self.next_cell(cell, 1, 0)

    def process_data(self):
        """
        a method to process data in excel object by call method `create_head` and `fill_row`
        """
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        pool = {}
        in_process = True
        current_day = self.start
        while in_process:
            current = current_day.strftime('%Y-%m-%d')
            query_set = self.get_query_set(current_day)
            pool[current] = {x['inv_code']: float(x['total']) for x in query_set}
            for x in self.Meta.head['fields']:
                if x not in pool[current]:
                    pool[current][x] = 0

            try:
                next_day = current_day.replace(day=current_day.day + 1)
                if next_day.day > self.end.day:
                    in_process = False
                current_day = next_day
            except Exception as e:
                in_process = False

        for k, v in pool.items():
            print('{}: {}'.format(k, v))
            self.fill_row(count, v, k, row=current_row)
            count += 1
            current_row += 1

    def process_notify(self):
        """
        a method to notify from process

        :return: (str): summary message
        """
        current_date = datetime.date.today()
        pool = {}
        tc_value = 0
        for x in self.get_query_set(current_date):
            pool[x['inv_code']] = float(x['total'])
            tc_value += float(x['total_tc']) if x['total_tc'] is not None else 0
        total = 0
        message = 'รายงานยอดขายประจำนวัน : {}\n'.format(current_date.strftime('%Y-%m-%d'))
        for k, v in pool.items():
            message += '{} : {:,} บาท\n'.format(k, v)
            total += v
        message += 'Total : {:,} บาท\n'.format(total)
        # message += 'รายจ่ายจากเครดิตท่องเที่ยว : {:,} บาท'.format(tc_value)
        return message

    def daily_summary(self, select_date=None):
        """
        a method for process an information on select date

        :param select_date: (:obj:`date object`)

        :return: (:obj:`dictionary`)
        """
        if select_date is None:
            current_date = datetime.date.today()
        else:
            current_date = datetime.datetime.strptime(select_date, '%Y-%m-%d').date()
        queryset = self.get_query_set(current_date.strftime('%Y-%m-%d'))
        pool = {x['inv_code']: float(x['total']) for x in queryset}
        total = 0
        result = {}
        for k, v in pool.items():
            total += v
            result[k] = v

        return {
            **result,
            'total': total
        }

    @property
    def file_name(self):
        """
        a method to named a excel object

        :return: (str): excel object's file name
        """
        name = '{}'.format(self.Meta.file_name)
        return '{}.xlsx'.format(name)
