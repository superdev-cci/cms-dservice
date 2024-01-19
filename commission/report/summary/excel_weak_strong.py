from collections import OrderedDict

from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from core.report.excel import ExcelTemplateReport
from .summary_weak_strong import SummaryWeakStrong


class ExcelSummaryWeakStrong(ExcelTemplateReport):
    template_file = './templates/report/commission/summary_weak_strong.xlsx'

    class Meta:
        title = 'Summary Weak Strong'
        file_name = 'summary_weak_strong'
        head_file = 'Summary Weak Strong'
        content_start_col = 1
        content_start_row = 8
        head_start_col = 3
        head_start_row = 7
        head = {
            'fields': []
        }

    def __init__(self, *args, **kwargs):
        super(ExcelSummaryWeakStrong, self).__init__(*args, **kwargs)
        self.report = SummaryWeakStrong(*args, **kwargs)

    def create_head(self):
        self.work_sheet['E4'] = self.report.start.strftime('%Y-%m-%d')
        self.work_sheet['G4'] = self.report.end.strftime('%Y-%m-%d')
        self.work_sheet['E5'] = self.report.get_type
        super(ExcelSummaryWeakStrong, self).create_head()

    def build_row_meta(self, row_index, data, **kwargs):
        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('date', {'data': data['time'], 'alignment': self.style['align_center']}),
            ('mcode', {'data': data['mcode'], 'alignment': self.style['align_center']}),
            ('name', {'data': data['name'], 'alignment': self.style['align_center']}),
            ('total', {'data': data['total'], 'alignment': self.style['align_right'],
                       'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('balance', {'data': data['balance'], 'alignment': self.style['align_right'],
                          'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('current_left', {'data': data['current_left'], 'alignment': self.style['align_right'],
                            'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
            ('current_right', {'data': data['current_right'], 'alignment': self.style['align_right'],
                        'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
        ])
        return meta

    def fill_row(self, row_index, data, *args, **kwargs):
        row = kwargs.get('row')
        current_col = self.Meta.content_start_col
        count = row_index
        for k_time, v in data['data'].items():
            cell = self.get_cell(current_col, row)
            cell.border = self.style['full_border']
            current_meta = {
                'mcode': data['mcode'],
                'name': data['name'],
                'time': k_time,
                **v
            }
            meta = self.build_row_meta(count, current_meta, **kwargs)
            for write_key, write_value in meta.items():
                cell = self.fill_data(cell, write_value)
            row += 1
            count += 1
        return count

    def process_data(self):
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        for k, v in self.report.total.items():
            count += self.fill_row(count, v, row=current_row)
            current_row += 1

    @property
    def file_name(self):
        name = '{}'.format(
            self.Meta.file_name + '_' + self.report.start.strftime(
                '%Y-%m-%d') + '_' + self.report.end.strftime('%Y-%m-%d'))
        return '{}.xlsx'.format(name)
