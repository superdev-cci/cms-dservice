from abc import ABC
from collections import OrderedDict

from core.mixin import MonthMixIn
from core.report.excel import ExcelTemplateReport
from ecommerce.report.summary import MemberBoughtItemSummary
from datetime import date


class MemberBoughtItemSummaryExcel(MonthMixIn, ExcelTemplateReport, ABC):
    template_file = './templates/report/base.xlsx'

    class Meta:
        title = 'รายงานยอดซื้ออสินค้ารายชิ้น'
        sheet_name = 'Summary'
        file_name = 'sale_item'
        head_start_col = 4
        head_start_row = 7
        head = {
            'fields': []
        }
        content_start_col = 1
        content_start_row = 8

    def __init__(self, *args, **kwargs):
        super(MemberBoughtItemSummaryExcel, self).__init__(*args, **kwargs)
        self.report = MemberBoughtItemSummary(*args, **kwargs)
        self.select_item = kwargs.get('items', '')
        self.get_type = kwargs.get('get_type', 'daily')

    def create_head(self, items):
        start_row = self.Meta.head_start_row
        start_col = self.Meta.head_start_col
        write_value = []

        # diff = self.report.date_range
        # current_date = self.report.start

        for i in items:
            write_value.append(i)

        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')

        for x in write_value:
            self.work_sheet.cell(row=start_row, column=start_col).value = x
            start_col += 1

        return

    def build_row_meta(self, row_index, mcode, data, **kwargs):
        meta = [
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('mcode', {'data': mcode, 'alignment': self.style['align_left']}),
            ('name', {'data': data['name'], 'alignment': self.style['align_left']}),
        ]

        diff = self.report.date_range
        current_date = self.report.start
        for k, v in data['data'].items():
            meta.append((k, {'data': data['data'][k]['total_qty'], 'alignment': self.style['align_right']}))

        # for i in range(diff.days):
        #     date_str = current_date.strftime('%Y-%m-%d')
        #     if date_str in data['data']:
        #         pass
        #     else:
        #         meta.append(('{}'.format(date_str), {'data': 0,
        #                                              'alignment': self.style['align_right']}))
        #     current_date = self.get_next_key(current_date)
        return OrderedDict(meta)

    def process(self):
        count = 1
        current_row = self.Meta.content_start_row
        head_list, pool = self.report.total_by_member
        self.create_head(head_list)
        for k, v in pool.items():
            self.fill_row(count, k, v, row=current_row)
            count += 1
            current_row += 1
        return

    @property
    def file_name(self):
        name = '{}_{}'.format(
            date.today().strftime('%Y-%b'),
            self.Meta.file_name)
        return '{}.xlsx'.format(name)
