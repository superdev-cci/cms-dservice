from collections import OrderedDict
from datetime import datetime

from django.db.models import Count
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from core.report.excel import ExcelTemplateReport
from ..models import BranchGoodsSnapRemainingStatement, BranchGoodsSnapRemainingItem
from ..serializers import BranchGoodsSnapRemainingStatementSerializer


class ExcelSnapRemaining(ExcelTemplateReport):
    """
    a class for generate excel object that represent a current all product's stock in branch.
    Excel object can save to an excel file or response via http request file.
    This class inherit class `ExcelTemplateReport` also you can use a method in ExcelTemplateReport or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        branch (str): branch code identify branch that interested
    """
    template_file = './templates/report/branch/snap_remaining.xlsx'

    class Meta:
        title = 'Snap Remaining'
        file_name = 'snap_remaining'+''
        head_file = 'Snap Remaining'
        content_start_col = 1
        content_start_row = 8
        head_start_col = 3
        head_start_row = 7
        head = {
            'fields': []
        }

    def __init__(self, **kwargs):
        super(ExcelSnapRemaining, self).__init__(**kwargs)
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
        super(ExcelSnapRemaining, self).create_head()

    def build_row_meta(self, row_index, data, **kwargs):
        """
        a method for index data with cell row

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :return: (:obj:`dictionary`)
        """
        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('date', {'data': data['date'], 'alignment': self.style['align_center']}),
        ])
        for i in self.Meta.head['fields']:
            meta.update({i: {'data': data['items'][i], 'alignment': self.style['align_right']}})
        return meta

    def get_query_set(self, branch, start, end):
        """
        a method to process data

        :param branch: (str): branch code

        :param start: (:obj:`date`) start date

        :param end: (:obj:`date`) end date

        :return: (:obj:`django queryset object`) query data
        """
        result = []
        qs = BranchGoodsSnapRemainingItem.objects.filter(statement__date_issue__range=(start, end)).values(
            'product__pcode').annotate(total=Count('product')).order_by('product__pcode')
        for k in qs:
            self.Meta.head['fields'].append(k['product__pcode'])

        query_set = BranchGoodsSnapRemainingStatement.objects\
            .filter(branch__inv_code=branch, date_issue__range=(start, end)).prefetch_related('items', 'items__product')
        jsons = BranchGoodsSnapRemainingStatementSerializer(query_set, many=True).data
        for j in jsons:
            tmp = {
                'date': j['date_issue'],
                'items': {}
            }
            for i in j['items']:
                tmp['items'][i['product']] = i['qty']
            for h in self.Meta.head['fields']:
                if h not in tmp['items']:
                    tmp['items'][h] = 0
            result.append(tmp)
        result.sort(key=lambda item: item['date'], reverse=False)
        return result

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
        name = '{}'.format(self.Meta.file_name+'_'+self.branch+'_'+self.start.strftime('%Y-%m-%d')+'_'+self.end.strftime('%Y-%m-%d'))
        return '{}.xlsx'.format(name)
