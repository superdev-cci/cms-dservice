from abc import ABC
from datetime import datetime

from core.report.excel import GenerateExcel
from member.models import Member
from .new_member_activity import NewMemberPvTransferActivity, NewMemberSaleInvoiceActivity


class ExcelNewMemberActivityAnalyst(GenerateExcel, ABC):
    """
    a class for present an activity of member in distributor role in excel object
    that can save to an excel file or response via http request file.
    This class inherit class `GenerateExcel` also you can use a method in GenerateExcel or overwrite method

    data content

    * New Distributor Sale Invoice Activity
    * New Distributor Pv Transfer Activity

    Attributes:
        start_date (:obj:`date`): a start date of interested data.
        end_date (:obj:`date`): a end date of interested data.
    """
    class Meta:
        title = 'New Member Activity Analyst'
        file_name = 'new_member_activity'

    def __init__(self, *args, **kwargs):
        super(ExcelNewMemberActivityAnalyst, self).__init__(*args, **kwargs)
        self.start_date = datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        self.end_date = datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date()
        self.sia = NewMemberSaleInvoiceActivity(*args, **kwargs)
        self.pva = NewMemberPvTransferActivity(*args, **kwargs)
        self.month_list = NewMemberSaleInvoiceActivity.month_diff_range(
            datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date(),
            datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        )

    def create_header(self):
        """
        a method to process data to create Header of table in excel object
        """
        sht = self.wb.active
        sht["A1"] = "New Member Activity"
        sht["A3"] = "mcode"
        sht["B3"] = "name_t"
        sht["C3"] = "level"
        sht["D3"] = "honor"
        sht["E3"] = "sp_code"
        sht["F3"] = "sp_name"
        col_start = 7
        for month in self.month_list:
            sht.merge_cells(start_row=1, end_row=1, start_column=col_start, end_column=(col_start + 4))
            sht.cell(column=col_start, row=1, value=datetime.strftime(month, "%b-%Y"))
            sht.merge_cells(start_row=2, end_row=2, start_column=col_start, end_column=(col_start + 2))
            sht.cell(column=col_start, row=2, value="Sale")
            sht.merge_cells(start_row=2, end_row=2, start_column=(col_start + 3), end_column=(col_start + 4))
            sht.cell(column=(col_start + 3), row=2, value="PVTrans")
            sht.cell(column=col_start, row=3, value="count")
            sht.cell(column=(col_start + 1), row=3, value="total")
            sht.cell(column=(col_start + 2), row=3, value="pv")
            sht.cell(column=(col_start + 3), row=3, value="count")
            sht.cell(column=(col_start + 4), row=3, value="pv")
            col_start += 5

    def fill_data(self):
        """
        a method to process write a data on table in excel object
        """
        sht = self.wb.active
        row_start = 4
        col_start = 7
        member_list = Member.objects.filter(mcode__in=self.sia.new_member_list).order_by("mcode")
        for mc in member_list:
            sht.cell(column=1, row=row_start, value=mc.mcode)
            sht.cell(column=2, row=row_start, value=mc.name_t)
            sht.cell(column=3, row=row_start, value=mc.level)
            sht.cell(column=4, row=row_start, value=mc.honor)
            sht.cell(column=5, row=row_start, value=mc.sp_code)
            sht.cell(column=6, row=row_start, value=mc.sp_name)
            offset = 0
            pool = self.total
            for x in self.month_list:
                d = pool[mc.mcode].get(x.strftime("%b-%Y"), None)
                if d is not None:
                    sht.cell(column=col_start + offset, row=row_start, value=d["sale_count"])
                    sht.cell(column=col_start + offset + 1, row=row_start, value=d["sale_total"])
                    sht.cell(column=col_start + offset + 2, row=row_start, value=d["sale_pv"])
                    sht.cell(column=col_start + offset + 3, row=row_start, value=d["pv_trans_count"])
                    sht.cell(column=col_start + offset + 4, row=row_start, value=d["pv_trans_pv"])
                else:
                    sht.cell(column=col_start + offset, row=row_start, value=0)
                    sht.cell(column=col_start + offset + 1, row=row_start, value=0)
                    sht.cell(column=col_start + offset + 2, row=row_start, value=0)
                    sht.cell(column=col_start + offset + 3, row=row_start, value=0)
                    sht.cell(column=col_start + offset + 4, row=row_start, value=0)
                offset += 5
            row_start += 1

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
            self.Meta.file_name + self.start_date.strftime('%Y-%m-%d') + '_' + self.end_date.strftime('%Y-%m-%d')
        )
        return '{}.xlsx'.format(name)

    @property
    def total(self):
        """
        a method to process data from NewMemberSaleInvoiceActivity class and NewMemberPvTransferActivity class
        combine to dictionary that have member code is a key and sub-key is time period

        :return: (:obj:`dictionary`)
        """
        pool = {}
        sale_act = self.sia.total
        pv_act = self.pva.total
        for mc in self.sia.new_member_list:
            pool[mc] = {}
            for mth in self.month_list:
                if mc not in sale_act and mc not in pv_act:
                    continue
                if mc in sale_act or mc in pv_act:
                    pool[mc][mth.strftime("%b-%Y")] = {
                        "sale_count": 0,
                        "sale_total": 0,
                        "sale_pv": 0,
                        "pv_trans_count": 0,
                        "pv_trans_pv": 0
                    }
                if sale_act.get(mc, None):
                    sa = sale_act[mc].get(mth.strftime("%b-%Y"), None)
                    if sa is not None:
                        pool[mc][mth.strftime("%b-%Y")]["sale_count"] += sa["bill_qty"]
                        pool[mc][mth.strftime("%b-%Y")]["sale_total"] += sa["sum_total"]
                        pool[mc][mth.strftime("%b-%Y")]["sale_pv"] += sa["sum_pv"]
                if pv_act.get(mc, None):
                    pa = pv_act[mc].get(mth.strftime("%b-%Y"), None)
                    if pa is not None:
                        pool[mc][mth.strftime("%b-%Y")]["pv_trans_count"] += pa["bill_qty"]
                        pool[mc][mth.strftime("%b-%Y")]["pv_trans_pv"] += pa["sum_pv"]
        return pool
