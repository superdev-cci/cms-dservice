from openpyxl.reader.excel import load_workbook
from core.report.excel.excel_report_base import ExcelReportBase
from openpyxl.drawing.image import Image


class ExcelTemplateReport(ExcelReportBase):
    template_file = None

    def __init__(self, *args, **kwargs):
        self.wb = load_workbook(self.get_template_file())
        self.work_sheet = self.wb.active
        self.fill_logo()

        pass

    def get_template_file(self):
        assert self.template_file is not None, (
                "'%s' should either include a `template_file` attribute, "
                "or override the `get_template_file()` method."
                % self.__class__.__name__
        )
        return self.template_file

    def fill_logo(self):
        cell = self.work_sheet['A1']
        img = Image('./templates/report/logo_cci.jpg')
        img.width = 160
        img.height = 120
        # img.anchor(cell, anchortype='oneCell')
        # img.drawing.top = 100
        # op_img.drawing.left = 1
        self.work_sheet.add_image(img, 'A1')

    def build_row_meta(self, *args, **kwargs):
        raise NotImplemented

    def fill_row(self, *args, **kwargs):
        row = kwargs.get('row')
        current_col = self.Meta.content_start_col

        cell = self.get_cell(current_col, row)
        cell.border = self.style['full_border']

        meta = self.build_row_meta(*args, **kwargs)

        for k, v in meta.items():
            cell = self.fill_data(cell, v)
        return

    def fill_data(self, cell, row_data):
        cell.value = row_data['data']
        number_format = row_data.get('number_format')
        if number_format is not None:
            cell.number_format = number_format

        alignment = row_data.get('alignment')
        if alignment is not None:
            cell.alignment = alignment

        fill = row_data.get('fill')
        if fill is not None:
            cell.fill = fill

        self.apply_border(cell)
        return self.next_cell(cell, 1, 0)
