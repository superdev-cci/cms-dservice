from collections import OrderedDict

from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1, BUILTIN_FORMATS

from core.mixin import MonthMixIn
from core.report.excel import ExcelTemplateReport
from .summary_month_commission import SummaryMonthCommission


class ExcelSummaryMonthCommission(MonthMixIn, ExcelTemplateReport):
    """
    a class for generate excel object that represent summary of each member's month commission.
    Excel object can save to an excel file or response via http request file.
    This class inherit class `ExcelTemplateReport` also you can use a method in ExcelTemplateReport or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        mcode (str): (Optional) member code of interested person
        honor (list): (Optional) member honor of interested group's member
    """
    template_file = './templates/report/commission/summary_month_commission.xlsx'

    class Meta:
        title = 'Month Commission'
        file_name = 'month_commission' + ''
        head_file = 'Month commission'
        content_start_col = 1
        content_start_row = 8
        head_start_col = 5
        head_start_row = 7
        head = {
            'fields': []
        }

    def __init__(self, *args, **kwargs):
        super(ExcelSummaryMonthCommission, self).__init__(*args, **kwargs)
        self.report = SummaryMonthCommission(*args, **kwargs)

    def create_head(self):
        """
        a method to process data to create Header of table in sheet of excel object
        """
        self.work_sheet['E4'] = self.report.start.strftime('%Y-%m-%d')
        self.work_sheet['G4'] = self.report.end.strftime('%Y-%m-%d')
        self.work_sheet['E5'] = self.report.get_type
        fields = []
        # super(ExcelSummaryMonthCommission, self).create_head()
        diff = self.month_diff_range(self.report.end, self.report.start)
        for x in diff:
            fields.append('{}-Matching'.format(x.strftime('%b')))
            # fields.append('{}-AllSales'.format(x.strftime('%b')))
            # fields.append('{}-Total'.format(x.strftime('%b')))

        super(ExcelSummaryMonthCommission, self).create_head()
        start_row = self.Meta.head_start_row
        start_col = self.Meta.head_start_col
        for x in fields:
            self.work_sheet.cell(row=start_row, column=start_col).value = x
            self.work_sheet.cell(row=start_row, column=start_col).border = self.style['full_border']
            start_col += 1

    def build_row_meta(self, row_index, data, **kwargs):
        """
        a method for index data with cell row

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :return: (:obj:`dictionary`)
        """
        meta = [
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('date', {'data': '-', 'alignment': self.style['align_center']}),
            ('mcode', {'data': data['mcode'], 'alignment': self.style['align_center']}),
            ('name', {'data': data['name'], 'alignment': self.style['align_center']}),
        ]

        diff = self.month_diff_range(self.report.end, self.report.start)
        for x in diff:
            month = x.strftime('%Y-%b')
            current_month = data['data'].get(month, None)
            if current_month is None:
                meta.append(('{}-1'.format(month), {'data': 0, 'alignment': self.style['align_right']}))
                # meta.append(('{}-2'.format(month), {'data': 0, 'alignment': self.style['align_right']}))
                # meta.append(('{}-3'.format(month), {'data': 0, 'alignment': self.style['align_right']}))
                # meta.append(('{}-3'.format(month), {'data': 0, 'alignment': self.style['align_right']}))
            else:
                matching = current_month.get('matching', 0)
                all_sales = current_month.get('all_sales', 0)
                total = current_month.get('total', 0)
                meta.append(('{}-1'.format(month), {
                    'data': matching,
                    'alignment': self.style['align_right'],
                    'number_format': BUILTIN_FORMATS[3]
                }))
                # meta.append(('{}-2'.format(month), {
                #     'data': all_sales,
                #     'alignment': self.style['align_right'],
                # }))
                # meta.append(('{}-3'.format(month), {
                #     'data': total,
                #     'alignment': self.style['align_right'],
                # }))
        return OrderedDict(meta)

    # def fill_row(self, row_index, data, *args, **kwargs):
    #     """
    #     a method for fill data to row by index
    #
    #     :param row_index: (int) index of sheet row
    #
    #     :param data: (:obj:`dictionary`) a content write in row
    #
    #     :return: (int) last row index
    #     """
    #     row = kwargs.get('row')
    #     current_col = self.Meta.content_start_col
    #     count = row_index
    #     for k_time, v in data['data'].items():
    #         cell = self.get_cell(current_col, row)
    #         cell.border = self.style['full_border']
    #         current_meta = {
    #             'mcode': data['mcode'],
    #             'name': data['name'],
    #             'time': k_time,
    #             **v
    #         }
    #         meta = self.build_row_meta(count, current_meta, **kwargs)
    #         for write_key, write_value in meta.items():
    #             cell = self.fill_data(cell, write_value)
    #         row += 1
    #         count += 1
    #     return count

    def process_data(self):
        """
        a method to process data in excel object by call method `create_head` and `fill_row`
        """
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        for k, v in self.report.total.items():
            self.fill_row(count, v, row=current_row)
            count += 1
            current_row += 1

    @property
    def file_name(self):
        """
        a method to named a excel object

        :return: (str): excel object's file name
        """
        name = '{}'.format(
            self.Meta.file_name + '_' + self.report.start.strftime(
                '%Y-%m-%d') + '_' + self.report.end.strftime('%Y-%m-%d'))
        return '{}.xlsx'.format(name)
