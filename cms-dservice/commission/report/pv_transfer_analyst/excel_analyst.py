from abc import ABC
from datetime import datetime

from member.models import Member
from commission.report.pv_transfer_analyst.pv_transfer_analyst import SummaryPvTransferInOutAnalyst, \
    PvTransferInnerOuterAnalyst, SummaryPvTransferAgencyAnalyst, SummaryPvTransferReceiverAnalyst, \
    SummaryPvTransferAnalyst
from core.report.excel import GenerateExcel


class ExcelSummaryPvTransferInOutAnalyst(GenerateExcel, ABC):
    """
    a class for generate excel object that represent agency member's summary PV transfer activity with their downline tree
    focus transfer in downline tree or out downline tree
    Excel object can save to an excel file or response via http request file.
    This class inherit class `GenerateExcel` also you can use a method in GenerateExcel or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        title = 'Summary'
        file_name = 'PvTransferInOutAnalyst_Summary'

    def __init__(self, *args, **kwargs):
        super(ExcelSummaryPvTransferInOutAnalyst, self).__init__(*args, **kwargs)
        self.report = SummaryPvTransferInOutAnalyst(*args, **kwargs)

    def write_column_set(self, sheet, start_row, start_col, data_list):
        """
        a method to write data in cell on worksheet

        :param sheet: (:obj:`worksheet`) worksheet of excel object

        :param start_row: row index

        :param start_col: column index

        :param data_list: (:obj:`dictionary`)
        """
        for i in data_list:
            sheet.cell(column=start_col, row=start_row, value=i["count"])
            sheet.cell(column=start_col + 1, row=start_row, value=i["min"])
            sheet.cell(column=start_col + 2, row=start_row, value=i["max"])
            sheet.cell(column=start_col + 3, row=start_row, value=i["sum_pv"])
            start_row += 1

    def write_on_sheet(self, sheet, ag_code, ag_name, start_row, data_dict):
        """
        a method to write data in worksheet on excel object

        :param sheet: (:obj:`worksheet`) worksheet of excel object

        :param ag_code: agency code

        :param ag_name: agency name

        :param start_row: row index

        :param data_dict: (:obj:`dictionary`)
        """
        sheet.cell(column=1, row=start_row, value=ag_code)
        sheet.cell(column=2, row=start_row, value=ag_name)
        self.write_column_set(sheet, start_row, 3, list(data_dict["all_bill"]))
        self.write_column_set(sheet, start_row, 7, list(data_dict["inner_bill"]))
        self.write_column_set(sheet, start_row, 11, list(data_dict["outer_bill"]))

    def create_header(self, sht):
        """
        a method to process data to create Header of table in sheet of excel object

        :param sht: (:obj:`worksheet`) worksheet's excel object
        """
        sht.merge_cells("A1:A2")
        sht["A1"] = "รหัส"
        sht.merge_cells("B1:B2")
        sht["B1"] = "ผู้ทำรายการ"
        bill_group = ["all_bill", "inner_bill", "outer_bill"]
        head_col_start = 3
        for index, bill in enumerate(bill_group):
            col_shift = 4 * index
            sht.merge_cells(start_column=(head_col_start + col_shift), end_column=(head_col_start + col_shift + 3),
                            start_row=1, end_row=1)
            sht.cell(column=(head_col_start + col_shift), row=1, value=bill)
            sht.cell(column=(head_col_start + col_shift), row=2, value="count")
            sht.cell(column=(head_col_start + col_shift + 1), row=2, value="min")
            sht.cell(column=(head_col_start + col_shift + 2), row=2, value="max")
            sht.cell(column=(head_col_start + col_shift + 3), row=2, value="sum")

    def fill_data(self):
        """
        a method to process data in excel object
        """
        summary = self.report.total
        sht = self.wb.active
        sht.title = "Y200"
        self.create_header(sht)
        row_start = 3
        for ag_code, data_list in summary.items():
            self.write_on_sheet(sht, ag_code, data_list["name"], row_start, data_list["y200"])
            row_start = sht.max_row + 1
        sht2 = self.wb.create_sheet("Y")
        self.create_header(sht2)
        row_start = 3
        for ag_code, data_list in summary.items():
            self.write_on_sheet(sht2, ag_code, data_list["name"], row_start, data_list["y"])
            row_start = sht2.max_row + 1
        sht3 = self.wb.create_sheet("A_AM")
        self.create_header(sht3)
        row_start = 3
        for ag_code, data_list in summary.items():
            self.write_on_sheet(sht3, ag_code, data_list["name"], row_start, data_list["a/am"])
            row_start = sht3.max_row + 1

    def process_data(self):
        """
        a method to process data in excel object
        """
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


class ExcelPvTransferInnerOuterAnalyst(GenerateExcel, ABC):
    """
    a class for generate excel object that represent agency member's PV transfer activity with their downline tree
    focus transfer in downline tree or out downline tree
    Excel object can save to an excel file or response via http request file.
    This class inherit class `GenerateExcel` also you can use a method in GenerateExcel or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        file_name = 'PvTransferInOutAnalyst_Person'

    def __init__(self, *args, **kwargs):
        super(ExcelPvTransferInnerOuterAnalyst, self).__init__(*args, **kwargs)
        self.report = PvTransferInnerOuterAnalyst(*args, **kwargs)

    def write_column_set(self, sheet, start_row, start_col, data_list):
        """
        a method to write data in cell on worksheet

        :param sheet: (:obj:`worksheet`) worksheet of excel object

        :param start_row: row index

        :param start_col: column index

        :param data_list: (:obj:`dictionary`)
        """
        for i in data_list:
            sheet.cell(column=start_col, row=start_row, value=i["mcode"])
            sheet.cell(column=start_col + 1, row=start_row, value=i["count"])
            sheet.cell(column=start_col + 2, row=start_row, value=i["min"])
            sheet.cell(column=start_col + 3, row=start_row, value=i["max"])
            sheet.cell(column=start_col + 4, row=start_row, value=i["sum_pv"])
            start_row += 1

    def write_on_sheet(self, sheet, ag_code, ag_name, start_row, data_dict):
        """
        a method to write data in worksheet on excel object

        :param sheet: (:obj:`worksheet`) worksheet of excel object

        :param ag_code: agency code

        :param ag_name: agency name

        :param start_row: row index

        :param data_dict: (:obj:`dictionary`)
        """
        sheet.cell(column=1, row=start_row, value=ag_code)
        sheet.cell(column=2, row=start_row, value=ag_name)
        self.write_column_set(sheet, start_row, 3, list(data_dict["all_bill"]))
        self.write_column_set(sheet, start_row, 8, list(data_dict["inner_bill"]))
        self.write_column_set(sheet, start_row, 13, list(data_dict["outer_bill"]))

    def create_header(self, sht):
        """
        a method to process data to create Header of table in sheet of excel object

        :param sht: (:obj:`worksheet`) worksheet's excel object
        """
        sht.merge_cells("A1:A2")
        sht["A1"] = "รหัส"
        sht.merge_cells("B1:B2")
        sht["B1"] = "ผู้ทำรายการ"
        bill_group = ["all_bill", "inner_bill", "outer_bill"]
        head_col_start = 3
        for index, bill in enumerate(bill_group):
            col_shift = 5 * index
            sht.merge_cells(start_column=(head_col_start + col_shift), end_column=(head_col_start + col_shift + 4),
                            start_row=1, end_row=1)
            sht.cell(column=(head_col_start + col_shift), row=1, value=bill)
            sht.cell(column=(head_col_start + col_shift), row=2, value="ผู้รับ")
            sht.cell(column=(head_col_start + col_shift + 1), row=2, value="count")
            sht.cell(column=(head_col_start + col_shift + 2), row=2, value="min")
            sht.cell(column=(head_col_start + col_shift + 3), row=2, value="max")
            sht.cell(column=(head_col_start + col_shift + 4), row=2, value="sum")

    def fill_data(self):
        """
        a method to process data in excel object
        """
        summary = self.report.total
        sht = self.wb.active
        sht.title = "Y200"
        self.create_header(sht)
        row_start = 3
        for ag_code, data_list in summary.items():
            self.write_on_sheet(sht, ag_code, data_list["name"], row_start, data_list["y200"])
            row_start = sht.max_row + 1
        sht2 = self.wb.create_sheet("Y")
        self.create_header(sht2)
        row_start = 3
        for ag_code, data_list in summary.items():
            self.write_on_sheet(sht2, ag_code, data_list["name"], row_start, data_list["y"])
            row_start = sht2.max_row + 1
        sht3 = self.wb.create_sheet("A_AM")
        self.create_header(sht3)
        row_start = 3
        for ag_code, data_list in summary.items():
            self.write_on_sheet(sht3, ag_code, data_list["name"], row_start, data_list["a/am"])
            row_start = sht3.max_row + 1

    def process_data(self):
        """
        a method to process data in excel object
        """
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


class ExcelSummaryPvTransferAnalyst(GenerateExcel, ABC):
    """
    a class for generate excel object that represent agency member's PV transfer activity
    Excel object can save to an excel file or response via http request file.
    This class inherit class `GenerateExcel` also you can use a method in GenerateExcel or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
    """
    class Meta:
        file_name = 'pv_transfer_analyst'

    def __init__(self, *args, **kwargs):
        super(ExcelSummaryPvTransferAnalyst, self).__init__(*args, **kwargs)
        self.agency_view = SummaryPvTransferAgencyAnalyst(*args, **kwargs)
        self.receiver_view = SummaryPvTransferReceiverAnalyst(*args, **kwargs)
        self.report = SummaryPvTransferAnalyst(*args, **kwargs)
        self.month_list = SummaryPvTransferAnalyst.month_diff_range(
            datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date(),
            datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        )

    def write_single_sheet(self, sheet, data_dict):
        """
        a method to process header table and write data from dictionary

        :param sheet: (:obj:`worksheet`) worksheet's excel object

        :param data_dict: (:obj:`dictionary`)
        """
        sheet["A1"] = "รหัส"
        sheet["B1"] = "ชื่อผู้ทำรายการ"
        sheet["C1"] = "รหัสผู้รับ"
        sheet["D1"] = "ชื่อผู้รับ"
        sheet["E1"] = "month"
        sheet["F1"] = "bill_type"
        sheet["G1"] = "จำนวนรายการ"
        sheet["H1"] = "avg"
        sheet["I1"] = "min"
        sheet["J1"] = "max"
        start_row = 2
        for uid, data_list in data_dict.items():
            for data in data_list:
                sheet.cell(column=1, row=start_row, value=uid)
                sheet.cell(column=2, row=start_row, value=Member.objects.get(mcode=uid).name_t)
                sheet.cell(column=3, row=start_row, value=data["mcode"])
                sheet.cell(column=4, row=start_row, value=data["member__name_t"])
                sheet.cell(column=5, row=start_row, value=data["time"].strftime("%b-%Y"))
                sheet.cell(column=6, row=start_row, value=data["sa_type"])
                sheet.cell(column=7, row=start_row, value=data["count"])
                sheet.cell(column=8, row=start_row, value=data["avg"])
                sheet.cell(column=9, row=start_row, value=data["min"])
                sheet.cell(column=10, row=start_row, value=data["max"])
                start_row += 1

    def create_summary_header(self, sht):
        """
        a method to process data to create Header of table in sheet of excel object

        :param sht: (:obj:`worksheet`) worksheet's excel object
        """
        sht.merge_cells("A1:A2")
        sht["A1"] = "รหัส"
        sht.merge_cells("B1:B2")
        sht["B1"] = "ผู้ทำรายการ"
        head_col_start = 3
        for index, mth in enumerate(self.month_list):
            col_shift = 4 * index
            sht.merge_cells(start_column=(head_col_start + col_shift), end_column=(head_col_start + col_shift + 3),
                            start_row=1, end_row=1)
            sht.cell(column=(head_col_start + col_shift), row=1, value=mth.strftime("%b-%Y"))
            sht.cell(column=(head_col_start + col_shift), row=2, value="Y200")
            sht.cell(column=(head_col_start + col_shift + 1), row=2, value="YF")
            sht.cell(column=(head_col_start + col_shift + 2), row=2, value="YM")
            sht.cell(column=(head_col_start + col_shift + 3), row=2, value="A/AM")

    def process_data(self):
        """
        a method to process data in excel object
        """
        pool_sum = self.agency_view.total
        pool_mcode = self.receiver_view.total
        pool_data = self.report.total
        sht = self.wb.active
        sht.title = "Summary_AG_view"
        self.create_summary_header(sht)
        bill_type_shift_index = {"y200": 1, "yf": 2, "ym": 3, "a/am": 4}
        month_shift_index = {}
        for index, m in enumerate(self.month_list):
            month_shift_index[m.strftime("%b-%Y")] = index
        start_row = 3
        for uid, data_list in pool_sum.items():
            for bill_type, query_list in data_list.items():
                for i in query_list:
                    sht.cell(column=1, row=start_row, value=uid)
                    sht.cell(column=2, row=start_row, value=Member.objects.get(mcode=uid).name_t)
                    current_col = 2 + (
                            bill_type_shift_index[bill_type] + (month_shift_index[i["time"].strftime("%b-%Y")] * 4))
                    if sht.cell(column=current_col, row=start_row).value is None:
                        sht.cell(column=current_col, row=start_row, value=i["count"])
                    else:
                        sht.cell(column=current_col, row=start_row).value += i["count"]
            start_row += 1
        msht = self.wb.create_sheet("Summary_mcode_view")
        self.create_summary_header(msht)
        start_row = 3
        for mcode, data_dict in pool_mcode.items():
            for bill_type, item_list in data_dict.items():
                for i in item_list:
                    msht.cell(column=1, row=start_row, value=i["mcode"])
                    msht.cell(column=2, row=start_row, value=i["name_t"])
                    current_col = 2 + (
                            bill_type_shift_index[bill_type] + (month_shift_index[i["time"].strftime("%b-%Y")] * 4))
                    if msht.cell(column=current_col, row=start_row).value is None:
                        msht.cell(column=current_col, row=start_row, value=i["count"])
                    else:
                        msht.cell(column=current_col, row=start_row).value += i["count"]
            start_row += 1
        for bill_type, data_dict in pool_data.items():
            if bill_type == "a/am":
                ws = self.wb.create_sheet("a_am")
            else:
                ws = self.wb.create_sheet(bill_type)
            self.write_single_sheet(ws, data_dict)

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