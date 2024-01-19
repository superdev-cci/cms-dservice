from .pv_bought_with_sponsor_structure import PvHoldInWithSponsorStructureReport
from .pv_transfer_in_with_sponsor_structure import PvTransferInWithSponsorStructureReport
from .pv_transfer_out_with_sponsor_structure import PvTransferOutWithSponsorStructureReport
from core.report.summary import PeriodSummaryBase
from member.models import Member


class PvInOutWithSponsorStructureJSON(PeriodSummaryBase):

    def __init__(self, *args, **kwargs):
        super(PvInOutWithSponsorStructureJSON, self).__init__(*args, **kwargs)
        self.member_group = kwargs.get('group', None)
        return

    @property
    def total(self):
        raw_data = {}
        period = self.month_diff_range(self.end, self.start)
        for member in Member.objects.filter(honor=self.member_group):
            transfer_in = PvTransferInWithSponsorStructureReport(member=member, start=self.start, stop=self.end,
                                                                 get_type='monthly')
            transfer_out = PvTransferOutWithSponsorStructureReport(member=member, start=self.start, stop=self.end,
                                                                   get_type='monthly')
            bought_in = PvHoldInWithSponsorStructureReport(member=member, start=self.start, stop=self.end,
                                                           get_type='monthly')

            bought_in_pool = bought_in.total
            transfer_in_pool = transfer_in.total
            transfer_out_pool = transfer_out.total

            raw_data[member.code] = {
                'name': member.full_name,
                'honor': member.get_honor,
                'data': {}
            }

            for x in period:
                current_month = x.strftime('%Y-%b')
                sales = 0
                total_in = 0
                total_out = 0

                if current_month in bought_in_pool:
                    sales += bought_in_pool[current_month]

                if current_month in transfer_in_pool:
                    total_in += transfer_in_pool[current_month]

                if current_month in transfer_out_pool:
                    total_out += transfer_out_pool[current_month]

                raw_data[member.code]['data'][current_month] = {
                    'sales': sales,
                    'in': total_in,
                    'out': total_out
                }
        return raw_data
