from abc import ABC
from datetime import datetime, timedelta

from django.core.exceptions import ObjectDoesNotExist

from core.report.excel import GenerateExcel
from ecommerce.models import Product
from ecommerce.report.analyst.sale_invoice import SaleInvoiceAnalyst
from ecommerce.report.analyst.sale_item import SaleItemAnalyst
from member.models import Member


class ExcelSaleInvoiceAnalyst(GenerateExcel, ABC):
    """
    a class for create excel file represent a `Chance of repeat purchases`
    This class inherit class `GenerateExcel` also you can use a method in GenerateExcel or overwrite method

    Attributes:
        start_date (:obj:`date`): a start date of interested data.
        end_date (:obj:`date`): a end date of interested data.
    """
    class Meta:
        title = 'Sale Invoice Analyst'
        file_name = 'sale_invoice_analyst'

    def __init__(self, *args, **kwargs):
        super(ExcelSaleInvoiceAnalyst, self).__init__(*args, **kwargs)
        self.report = SaleInvoiceAnalyst(*args, **kwargs)
        self.start_date = datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        self.end_date = datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date()

    def create_header(self):
        """
        a method to process data to create Header of table in excel
        """
        sht = self.wb.active
        sht.merge_cells("A1:A2")
        sht["A1"] = "รหัส"
        sht.merge_cells("B1:B2")
        sht["B1"] = "ผู้ทำรายการ"
        head_col_start = 3
        delta = (self.end_date - self.start_date).days
        sht.merge_cells(start_column=head_col_start, end_column=(head_col_start + delta), start_row=1, end_row=1)
        sht.cell(column=head_col_start, row=1, value="date_delta")
        for i in range(delta + 1):
            sht.cell(column=(head_col_start + i), row=2, value=i)

    def fill_data(self):
        """
        a method to process write a data on table in excel
        """
        sht = self.wb.active
        row_start = 3
        for mcode, data_dict in self.report.total.items():
            sht.cell(column=1, row=row_start, value=mcode)
            try:
                m = Member.objects.get(mcode=mcode)
                sht.cell(column=2, row=row_start, value=m.name_t)
            except ObjectDoesNotExist:
                sht.cell(column=2, row=row_start, value="ไม่พบ Member obj")
            col_start = 3
            for day_diff, count in data_dict.items():
                if day_diff:
                    sht.cell(column=col_start + int(day_diff), row=row_start, value=count)
            row_start = sht.max_row + 1

    def process_data(self):
        """
        a method to process data in excel object by call method `create_header` and `fill_data`
        """
        self.create_header()
        self.fill_data()

    @property
    def file_name(self):
        """
        a method to named a excel object

        :return: (str): excel object's file name
        """
        name = '{}'.format(
            self.Meta.file_name + self.report.start.strftime('%Y-%m-%d') + '_' + self.report.end.strftime('%Y-%m-%d')
        )
        return '{}.xlsx'.format(name)


class ExcelSaleItemAnalyst(GenerateExcel, ABC):
    """
    a class for create excel file represent Summarize products that are either sold individually
    or sold through promotions.
    This class inherit class `GenerateExcel` also you can use a method in GenerateExcel or overwrite method

    Attributes:
        start_date (:obj:`date`): a start date of interested data.
        end_date (:obj:`date`): a end date of interested data.
    """
    class Meta:
        title = 'Sale Item Analyst'
        file_name = 'sale_item_analyst'

    def __init__(self, *args, **kwargs):
        super(ExcelSaleItemAnalyst, self).__init__(*args, **kwargs)
        self.report = SaleItemAnalyst(*args, **kwargs)
        self.start_date = datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        self.end_date = datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date()

    def create_header(self):
        """
        a method to process data to create Header of table in excel
        """
        sht = self.wb.active
        sht.merge_cells("A1:A2")
        sht["A1"] = "รหัส"
        sht.merge_cells("B1:B2")
        sht["B1"] = "ชื่อสินค้า"
        head_col_start = 3
        current_dt = self.start_date
        while current_dt <= self.end_date:
            col_shift = (2 * (current_dt - self.start_date).days)
            sht.merge_cells(start_column=(head_col_start + col_shift), end_column=(head_col_start + col_shift + 1),
                            start_row=1, end_row=1)
            sht.cell(column=(head_col_start + col_shift), row=1, value=current_dt.strftime("%d/%m/%Y"))
            sht.cell(column=(head_col_start + col_shift), row=2, value="sku")
            sht.cell(column=(head_col_start + col_shift + 1), row=2, value="pro")
            current_dt = current_dt + timedelta(days=1)

    def fill_data(self):
        """
        a method to process write a data on table in excel
        """
        sht = self.wb.active
        row_start = 3
        for product_code, time_dict in self.report.total.items():
            sht.cell(column=1, row=row_start, value=product_code)
            sht.cell(column=2, row=row_start, value=Product.objects.get(pcode=product_code).pdesc)
            col_start = 3
            for dt, qty_dict in time_dict.items():
                col_shift = (2 * (dt - self.start_date).days)
                sht.cell(column=(col_start + col_shift), row=row_start, value=qty_dict["qty_single_unit"])
                sht.cell(column=(col_start + col_shift + 1), row=row_start, value=qty_dict["qty_from_promotion"])
            row_start = sht.max_row + 1

    def process_data(self):
        """
        a method to process data in excel object by call method `create_header` and `fill_data`
        """
        self.create_header()
        self.fill_data()

    @property
    def file_name(self):
        """
        a method to named a excel object

        :return: (str): excel object's file name
        """
        name = '{}'.format(
            self.Meta.file_name + self.report.start.strftime('%Y-%m-%d') + '_' + self.report.end.strftime('%Y-%m-%d')
        )
        return '{}.xlsx'.format(name)
