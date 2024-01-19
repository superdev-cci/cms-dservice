import pandas as pd
from datetime import datetime
from member.models import Member
from member.report.analyst.child_new_vip_activity import NewVipActivityAnalystReport
from member.report.analyst.child_honor_activity import HonorActivityAnalystReport
from member.report.analyst.child_sale_invoice_activity import SaleInvoiceActivityAnalystReport
from member.report.analyst.child_receive_pv_activity import PvTransferActivityAnalystReport
from member.report.analyst.child_ws_bonus_activity import WsBonusActivityAnalystReport


class ExcelDataFrameSponsorChild(object):
    """
    a class that's collect data in sponsor tree of each member (this data exclude personal data).

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
        mcode_list (:obj:`list`) a list of member code that's interested
    """
    def __init__(self, *args, **kwargs):
        self.start_date = datetime.strptime(kwargs.get('start', None), "%Y-%m-%d").date()
        self.end_date = datetime.strptime(kwargs.get('end', None), "%Y-%m-%d").date()
        self.mcode_list = kwargs.get('mcode', [])

    @property
    def generate_pool_data(self):
        """
        a method to process data generate data in structure for DataFrame

        :return: (:obj:`dict`) dictionary for generate DataFrame
        """
        pool = {}
        for member_code in self.mcode_list:
            m_obj = Member.objects.get(mcode=member_code)
            nva = NewVipActivityAnalystReport(start=self.start_date, end=self.end_date, mcode=member_code).total
            ha = HonorActivityAnalystReport(start=self.start_date, end=self.end_date, mcode=member_code).for_dataframe
            sia = SaleInvoiceActivityAnalystReport(
                start=self.start_date, end=self.end_date, mcode=member_code).for_dataframe
            pva = PvTransferActivityAnalystReport(
                start=self.start_date, end=self.end_date, mcode=member_code).for_dataframe
            wba_count, wba_bonus = WsBonusActivityAnalystReport(
                start=self.start_date, end=self.end_date, mcode=member_code).for_dataframe
            pool[((member_code, m_obj.name_t, m_obj.honor, m_obj.level), "NDIS")] = nva[member_code]
            pool[((member_code, m_obj.name_t, m_obj.honor, m_obj.level), "NHOR")] = ha[member_code]
            pool[((member_code, m_obj.name_t, m_obj.honor, m_obj.level), "SAES")] = sia[member_code]
            pool[((member_code, m_obj.name_t, m_obj.honor, m_obj.level), "PVAT")] = pva[member_code]
            pool[((member_code, m_obj.name_t, m_obj.honor, m_obj.level), "WSBN")] = wba_bonus[member_code]
            pool[((member_code, m_obj.name_t, m_obj.honor, m_obj.level), "PSWS")] = wba_count[member_code]
        return pool

    @property
    def generate_excel(self):
        """
        a method that's generate Excel object from DataFrame

        :return: (:obj:`Openpyxl.excel`) Excel object for response
        """
        from io import BytesIO
        bio = BytesIO()
        df = pd.DataFrame.from_dict(self.generate_pool_data, orient="index")
        sort_df = df.sort_index(axis=0)
        sort_df.fillna(0)
        excel_file = pd.ExcelWriter(bio, engine='openpyxl')
        sort_df.to_excel(excel_file, header=True, encoding="utf-8", na_rep=0)
        return excel_file
