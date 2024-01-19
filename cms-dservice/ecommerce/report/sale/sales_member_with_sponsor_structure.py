from core.report.summary import PeriodSummaryBase
from member.models import Member
from .sales_with_sponsor_structure import SalesWithSponsorStructureJSONReport


class SalesMemberWithSponsorStructureJSONReport(PeriodSummaryBase):
    def __init__(self, *args, **kwargs):
        super(SalesMemberWithSponsorStructureJSONReport, self).__init__(*args, **kwargs)
        self.member_group = kwargs.get('group', None)
        return

    @property
    def total(self):
        raw_data = {}
        period = self._calculate_month_range(self.start, self.end)
        for member in Member.objects.filter(honor=self.member_group, status_terminate=0):
            sales = SalesWithSponsorStructureJSONReport(member=member, start=self.start, stop=self.end,
                                                        get_type='monthly')
            sales_data = sales.total
            raw_data[member.code] = {
                'name': member.full_name,
                'honor': member.get_honor,
                'data': {}
            }

            for x in period:
                current_month = x.strftime('%Y-%b')
                sales = 0

                if current_month in sales_data:
                    sales += sales_data[current_month]

                raw_data[member.code]['data'][current_month] = {
                    'sales': sales,
                }
        return raw_data
