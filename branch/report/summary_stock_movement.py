from collections import OrderedDict
from datetime import datetime

from django.db.models import Sum, Max
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from core.report.excel import ExcelTemplateReport
from ..models import StockStatement


class ExcelSummaryStockMovement(ExcelTemplateReport):
    """
    a class for generate excel object that represent all product's Stock Movement in branch.
    Excel object can save to an excel file or response via http request file.
    This class inherit class `ExcelTemplateReport` also you can use a method in ExcelTemplateReport or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        branch (str): branch code identify branch that interested
    """
    template_file = './templates/report/branch/summary_stock_movement.xlsx'

    class Meta:
        title = 'Stock Movement'
        sheet_name = 'Summary'
        file_name = 'stock_movement'
        head_file = 'Stock Movement'
        content_start_col = 1
        content_start_row = 10
        head_start_col = 3
        head_start_row = 7
        head = {
            'fields': []
        }

    def __init__(self, **kwargs):
        super(ExcelSummaryStockMovement, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        if isinstance(self.start, str):
            self.start = datetime.strptime(self.start, '%Y-%m-%d').date()

        self.end = kwargs.get('end', None)
        if isinstance(self.end, str):
            self.end = datetime.strptime(self.end, '%Y-%m-%d').date()

        self.branch = kwargs.get('branch', None)
        self.queryset = self.get_query_set(self.branch, self.start, self.end)

    def create_head(self):
        """
        a method to process data to create Header of table in excel object
        """
        self.work_sheet['E4'] = self.start.strftime('%Y-%m-%d')
        self.work_sheet['G4'] = self.end.strftime('%Y-%m-%d')
        if self.branch:
            self.work_sheet['E5'] = self.branch
        super(ExcelSummaryStockMovement, self).create_head()

    def build_row_meta(self, row_index, data, **kwargs):
        """
        a method for index data with cell row

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :return: (:obj:`dictionary`)
        """
        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('date', {'data': self.start.strftime('%Y-%m'), 'alignment': self.style['align_center']}),
            ('pcode', {'data': data['pcode']}),
            ('in_qty', {'data': data['sum_in_qty'], 'alignment': self.style['align_right']}),
            ('in_price', {'data': data['max_in_price'], 'alignment': self.style['align_right'],
                          'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('in_amount', {'data': data['sum_in_amount'], 'alignment': self.style['align_right'],
                           'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('out_qty', {'data': data['sum_out_qty'], 'alignment': self.style['align_right']}),
            ('out_price', {'data': data['max_out_price'], 'alignment': self.style['align_right'],
                           'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('out_amount', {'data': data['sum_out_amount'], 'alignment': self.style['align_right'],
                            'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('balance', {'data': '', 'alignment': self.style['align_right']}),
            ('price', {'data': '', 'alignment': self.style['align_right'],
                       'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('amount', {'data': '', 'alignment': self.style['align_right'],
                        'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('for_doc', {'data': ''}),
            ('ref', {'data': ''}),
            ('client_name', {'data': ''}),
        ])
        return meta

    def get_query_set(self, branch, start, end):
        """
        a method to process data

        :param branch: (str): branch code

        :param start: (:obj:`date`) start date

        :param end: (:obj:`date`) end date

        :return: (:obj:`django queryset object`) query data
        """
        if branch == 'HQ':
            query_set = StockStatement.objects.filter(to_branch=branch)
        else:
            query_set = StockStatement.objects.filter(branch_name=branch)

        query_set = query_set.filter(date_issue__range=(start, end)).exclude(cancel=1) \
            .values('pcode') \
            .annotate(
            sum_in_qty=Sum('in_qty'), \
            max_in_price=Max('in_price'), \
            sum_in_amount=Sum('in_amount'), \
            sum_out_qty=Sum('out_qty'), \
            max_out_price=Max('out_price'), \
            sum_out_amount=Sum('out_amount')
        ).values('pcode', 'sum_in_qty', 'max_in_price', 'sum_in_amount', 'sum_out_qty', 'max_out_price',
                 'sum_out_amount') \
            .order_by('pcode')
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

        return

    def process_data(self):
        """
        a method to process data in excel object by call method `create_head` and `fill_row`
        """
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        for x in self.queryset:
            self.fill_row(count, x, row=current_row)
            count += 1
            current_row += 1

    @property
    def file_name(self):
        """
        a method to named a excel object

        :return: (str): excel object's file name
        """
        name = '{}'.format(
            self.Meta.file_name + '_' + self.branch + '_' + self.start.strftime('%Y-%m-%d') + '_' + self.end.strftime(
                '%Y-%m-%d'))
        return '{}.xlsx'.format(name)
