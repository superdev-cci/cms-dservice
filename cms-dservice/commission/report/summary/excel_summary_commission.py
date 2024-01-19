from collections import OrderedDict

from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from core.report.excel import ExcelTemplateReport
from .summary_commission import SummaryCommission


class ExcelSummaryCommission(ExcelTemplateReport):
    """
    a class for generate excel object that represent summary of each member's commission
    (combine WeekCommission and MonthCommission)
    Excel object can save to an excel file or response via http request file.
    This class inherit class `ExcelTemplateReport` also you can use a method in ExcelTemplateReport or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): (Optional) member code of interested person
        honor (list): (Optional) member honor of interested group's member
    """
    template_file = './templates/report/commission/summary_commission.xlsx'

    class Meta:
        title = 'Summary Commission'
        file_name = 'summary_commission'
        head_file = 'Summary commission'
        content_start_col = 1
        content_start_row = 8
        head_start_col = 3
        head_start_row = 7
        head = {
            'fields': []
        }

    def __init__(self, *args, **kwargs):
        super(ExcelSummaryCommission, self).__init__(*args, **kwargs)
        self.report = SummaryCommission(*args, **kwargs)

    def create_head(self):
        """
        a method to process data to create Header of table in sheet of excel object
        """
        self.work_sheet['E4'] = self.report.week.start.strftime('%Y-%m-%d')
        self.work_sheet['G4'] = self.report.week.end.strftime('%Y-%m-%d')
        self.work_sheet['E5'] = self.report.week.get_type
        super(ExcelSummaryCommission, self).create_head()

    def build_row_meta(self, row_index, data, **kwargs):
        """
        a method for index data with cell row

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :return: (:obj:`dictionary`)
        """
        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('date', {'data': data['time'], 'alignment': self.style['align_center']}),
            ('mcode', {'data': data['mcode'], 'alignment': self.style['align_center']}),
            ('name', {'data': data['name'], 'alignment': self.style['align_center']}),
            ('total', {'data': int(data['total']), 'alignment': self.style['align_right'],
                       'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('ws_bonus', {'data': int(data['ws']), 'alignment': self.style['align_right'],
                          'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('fast_bonus', {'data': int(data['fast']), 'alignment': self.style['align_right'],
                            'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('resale', {'data': int(data['resale']), 'alignment': self.style['align_right'],
                        'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('matching', {'data': int(data['matching']), 'alignment': self.style['align_right'],
                          'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('all_sales', {'data': int(data['all_sales']), 'alignment': self.style['align_right'],
                           'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
        ])
        return meta

    def fill_row(self, row_index, data, *args, **kwargs):
        """
        a method for fill data to row by index

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :return: (int) last row index
        """
        row = kwargs.get('row')
        current_col = self.Meta.content_start_col
        count = row_index
        line_count = 1
        for k_time, v in data['data'].items():
            cell = self.get_cell(current_col, row)
            cell.border = self.style['full_border']
            current_meta = {
                'mcode': data['mcode'],
                'name': data['name'],
                'time': k_time,
                **v
            }
            print(count)
            meta = self.build_row_meta(count, current_meta, **kwargs)
            for write_key, write_value in meta.items():
                cell = self.fill_data(cell, write_value)
            row += 1
            line_count += 1
        return line_count

    def process_data(self):
        """
        a method to process data in excel object by call method `create_head` and `fill_row`
        """
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        for k, v in self.report.total.items():
            count += self.fill_row(count, v, row=current_row)
            current_row += 1

    @property
    def file_name(self):
        """
        a method to named a excel object

        :return: (str): excel object's file name
        """
        name = '{}_{}_{}'.format(self.Meta.file_name,
                                 self.report.week.start.strftime('%Y-%m-%d'),
                                 self.report.week.end.strftime('%Y-%m-%d')
                                 )
        return '{}.xlsx'.format(name)
