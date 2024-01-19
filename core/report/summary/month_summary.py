import calendar
import datetime
from abc import ABC

from core.report.excel import ExcelTemplateReport


class ExcelMonthSummaryReport(ExcelTemplateReport, ABC):

    def __init__(self, *args, **kwargs):
        super(ExcelMonthSummaryReport, self).__init__(*args, **kwargs)
        return

    def calculate_period(self, date):
        month = calendar.monthrange(date.year, date.month)
        last_date = month[1]
        start = date.replace(day=1)
        end = date.replace(day=last_date)
        return start, end

    def _calculate_month_range(self, start, end):
        month_range = []
        start_month = start.month
        end_month = end.month

        if start_month > end_month:
            return None

        diff = (end_month - start_month) + 1

        for i in range(diff):
            month_range.append(start.replace(month=start_month + i))
        return month_range

    def create_head_column(self, column, row):
        cell = self.get_cell(column, row)
        for i in self.Meta.head_column_meta:
            cell.value = i
            cell.alignment = self.style['align_center']
            self.apply_border(cell)
            cell = self.next_cell(cell, 1, 0)
        return

    def create_head(self, months, *args):
        start_col = self.Meta.head_start_col
        start_row = self.Meta.head_start_row
        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = datetime.date.today().strftime('%d/%b/%Y')
        merge_rage = self.Meta.head_merge_rage

        for i in months:
            start_cell = self.work_sheet[self.get_string_cell(start_col, start_row)]
            if merge_rage > 1:
                self.merge_cell(start_cell, merge_rage, 0,
                                self.style['full_border'],
                                self.style['align_center'])
            else:
                start_cell.alignment = self.style['align_center']
                self.apply_border(start_cell)
            start_cell.value = i.strftime('%b')
            if getattr(self.Meta, 'head_column_meta', None):
                self.create_head_column(start_col, start_row + 1)
            start_col += merge_rage

        if getattr(self.Meta, 'head_column_suffix_meta', None):
            for x in self.Meta.head_column_suffix_meta:
                cell = self.get_cell(start_col, start_row)
                cell.value = x
                cell.alignment = self.style['align_center']
                self.apply_border(cell)

    def save_file(self, ):
        self.wb.save(self.file_name)
