from abc import ABC
from collections import OrderedDict

from openpyxl.styles.numbers import BUILTIN_FORMATS

from core.mixin import MonthMixIn
from core.report.excel import ExcelTemplateReport
from ecommerce.report.summary import MemberBoughtItemSummary
from datetime import date


class MemberBoughtItemCodeSummaryExcel(MonthMixIn, ExcelTemplateReport, ABC):
    template_file = './templates/report/base.xlsx'

    class Meta:
        title = 'รายงานยอดซื้ออสินค้า'
        sheet_name = 'Summary'
        file_name = 'sale_item_code'
        head_start_col = 4
        head_start_row = 7
        head = {
            'fields': []
        }
        content_start_col = 1
        content_start_row = 8

    def __init__(self, *args, **kwargs):
        super(MemberBoughtItemCodeSummaryExcel, self).__init__(*args, **kwargs)
        self.report = MemberBoughtItemSummary(*args, **kwargs, get_type='monthly', merge=True)
        self.get_type = kwargs.get('get_type', 'monthly')
        self.select_code = kwargs.get('items', None)
        if self.select_code:
            self.select_code = self.select_code[0]

    def create_head(self, items):
        start_row = self.Meta.head_start_row
        start_col = self.Meta.head_start_col
        write_value = []
        for i in items:
            write_value.append(i)
        write_value.append('Total')
        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')

        for x in write_value:
            self.work_sheet.cell(row=start_row, column=start_col).value = x
            start_col += 1

        return

    def build_row_meta(self, row_index, items, mcode, data, **kwargs):
        meta = [
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('mcode', {'data': mcode, 'alignment': self.style['align_left']}),
            ('name', {'data': data['name'], 'alignment': self.style['align_left']}),
        ]
        count = 3
        for i in items:
            count += 1
            if i in data['data']:
                meta.append(('{}'.format(i), {'data': data['data'][i][self.select_code]['total_qty'],
                                              'number_format': BUILTIN_FORMATS[3],
                                              'alignment': self.style['align_right']}))
            else:
                meta.append(('{}'.format(i), {'data': 0,
                                              'number_format': BUILTIN_FORMATS[3],
                                              'alignment': self.style['align_right']}))

        cell_range = self.get_string_cell_range(4, kwargs['row'], count, kwargs['row'])
        meta.append(('sumall', {'data': '=SUM({})'.format(cell_range),
                                'number_format': BUILTIN_FORMATS[3],
                                'alignment': self.style['align_right']}))
        return OrderedDict(meta)

    def process(self):
        count = 1
        current_row = self.Meta.content_start_row
        pool, head_list, code = self.report.total
        head_list = sorted(head_list)
        self.create_head(head_list)
        for k, v in pool.items():
            self.fill_row(count, head_list, k, v, row=current_row)
            count += 1
            current_row += 1
        return

    @property
    def file_name(self):
        name = '{}_{}'.format(
            date.today().strftime('%Y-%b'),
            self.Meta.file_name)
        return '{}.xlsx'.format(name)
