import datetime
from datetime import date
from collections import OrderedDict
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1, BUILTIN_FORMATS
from core.report.summary import ExcelMonthSummaryReport
from ecommerce.report.sale.sale_with_member_nation import SaleInvoiceSummaryWithNation


class SaleInvoiceSummaryWithNationExcel(ExcelMonthSummaryReport):
    template_file = './templates/report/ecommerce/sold_summary.xlsx'

    class Meta:
        title = 'Sold summary'
        sheet_name = 'Summary'
        file_name = 'sold_with_nation_summary'
        head_file = 'Sold summary'
        head_start_col = 3
        head_start_row = 7
        content_start_col = 1
        content_start_row = 8

    def __init__(self, **kwargs):
        super(SaleInvoiceSummaryWithNationExcel, self).__init__(**kwargs)
        self.report = SaleInvoiceSummaryWithNation(**kwargs)
        self.nation = kwargs.get('nation')

    def create_head(self, *args):
        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')
        Meta = self.Meta
        start_row = Meta.head_start_row
        start_col = Meta.head_start_col
        for x, y in self.nation:
            self.work_sheet.cell(row=start_row, column=start_col).value = x
            start_col += 1
        return

    def build_row_meta(self, row_index, data, date_issue, **kwargs):
        meta = [
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('date', {'data': date_issue, 'alignment': self.style['align_center']}),
        ]
        for x, y in self.nation:
            if x in data:
                meta.append(
                    (x, {'data': data[x]['prices'], 'alignment': self.style['align_left'],
                         'number_format': BUILTIN_FORMATS[3]}),
                )
            else:
                meta.append(
                    (x, {'data': 0, 'alignment': self.style['align_left'],
                         'number_format': BUILTIN_FORMATS[3]}),
                )

        return OrderedDict(meta)

    def process_data(self):
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        pool = self.report.total

        for k, v in pool.items():
            self.fill_row(count, v, k, row=current_row)
            count += 1
            current_row += 1

        return

    @property
    def file_name(self):
        name = '{}'.format(self.Meta.file_name)
        return '{}.xlsx'.format(name)
