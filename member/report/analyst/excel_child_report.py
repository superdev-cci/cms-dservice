from abc import ABC
from datetime import datetime

from core.report.excel import GenerateExcel
from member.models import Member
from .child_honor_activity import HonorActivityAnalystReport
from .child_new_vip_activity import NewVipActivityAnalystReport
from .child_receive_pv_activity import PvTransferActivityAnalystReport
from .child_sale_invoice_activity import SaleInvoiceActivityAnalystReport
from .child_ws_bonus_activity import WsBonusActivityAnalystReport


class ExcelChildActivityAnalyst(GenerateExcel, ABC):
    """
    a class for present data in sponsor tree of member in excel object
    that can save to an excel file or response via http request file.
    This class inherit class `GenerateExcel` also you can use a method in GenerateExcel or overwrite method

    data content

    * New distributor in sponsor tree
    * New Honor member in sponsor tree
    * Summary SaleInvoice in sponsor tree receive
    * Summary PV Transfer in sponsor tree receive
    * Summary WS Bonus in sponsor tree receive
    * People in sponsor tree who receive WS Bonus

    Attributes:
        start_date (:obj:`date`): a start date of interested data.
        end_date (:obj:`date`): a end date of interested data.
        mcode (str): member code of start point of sponsor tree
    """
    class Meta:
        title = 'Sponsor Child Activity Analyst'
        file_name = 'sponsor_child_activity'

    def __init__(self, *args, **kwargs):
        super(ExcelChildActivityAnalyst, self).__init__(*args, **kwargs)
        self.mcode = kwargs.get('mcode', None)
        self.start_date = datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        self.end_date = datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date()
        self.nva = NewVipActivityAnalystReport(*args, **kwargs)
        self.ha = HonorActivityAnalystReport(*args, **kwargs)
        self.sia = SaleInvoiceActivityAnalystReport(*args, **kwargs)
        self.pva = PvTransferActivityAnalystReport(*args, **kwargs)
        self.wba = WsBonusActivityAnalystReport(*args, **kwargs)
        self.month_list = NewVipActivityAnalystReport.month_diff_range(
            datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date(),
            datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        )

    def create_header(self):
        """
        a method to process data to create Header of table in excel object
        """
        sht = self.wb.active
        m_obj = Member.objects.get(mcode=self.mcode)
        sht["A1"] = m_obj.mcode + " " + m_obj.name_t
        col_start = 2
        for month in self.month_list:
            sht.cell(column=col_start, row=2, value=datetime.strftime(month, "%b-%Y"))
            col_start += 1

    def fill_data(self):
        """
        a method to process write a data on table in excel object
        """
        month_shift_index = {}
        for index, m in enumerate(self.month_list):
            month_shift_index[m.strftime("%b-%Y")] = index
        sht = self.wb.active
        col_start = 2
        for data in self.nva.total.values():
            sht.cell(column=1, row=3, value="จำนวน VIP เกิดใหม่ในผังผู้แนะนำ")
            for mth, val in data.items():
                sht.cell(column=col_start + month_shift_index[mth], row=3, value=val)
        for data in self.ha.total.values():
            sht.cell(column=1, row=4, value="จำนวนตำแหน่งเกียรติยศขึ้นใหม่ในผังผู้แนะนำ")
            for mth, val in data.items():
                tmp = ""
                for honor, c in val.items():
                    if c > 0:
                        tmp = tmp + honor + "(" + str(c) + ") / "
                sht.cell(column=col_start + month_shift_index[mth], row=4, value=tmp)
        for data in self.sia.total.values():
            sht.cell(column=1, row=5, value="ยอดซื้อภายในผังผู้แนะนำ")
            for mth, val in data.items():
                sht.cell(column=col_start + month_shift_index[mth], row=5, value=val["sum_total"])
        for data in self.pva.total.values():
            sht.cell(column=1, row=6, value="คะแนนที่คนในผังผู้แนะนำรับแจง")
            for mth, val in data.items():
                sht.cell(column=col_start + month_shift_index[mth], row=6, value=val["sum_pv"])
        for data in self.wba.total.values():
            sht.cell(column=1, row=7, value="ws_bonus ในผังผู้แนะนำ")
            sht.cell(column=1, row=8, value="จำนวนคนที่รับ ws_bonus")
            for mth, val in data.items():
                sht.cell(column=col_start + month_shift_index[mth], row=7, value=val["sum_bonus"])
                sht.cell(column=col_start + month_shift_index[mth], row=8, value=val["count"])

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
        name = '{}_{}'.format(
            self.Meta.file_name + self.start_date.strftime('%Y-%m-%d') + '_' + self.end_date.strftime('%Y-%m-%d'), self.mcode
        )
        return '{}.xlsx'.format(name)
