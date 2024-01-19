from django.db.models import Sum
from django.db.models.functions import TruncMonth
from core.mixin import MonthMixIn
from members.models import Member
from commission.models import CumulativeMonth, AutoShipStatement, PvTransferStatement
from ecommerce.models import SaleStatement


class MemberFriendchiseCheck(MonthMixIn):

    def __init__(self, member_code, *args, **kwargs):
        self.member = Member.objects.get(member_code=member_code)

    def get_all_data(self, start, end):
        month_range = self._calculate_month_range(start, end)
        data = {}
        query = AutoShipStatement.objects.filter(member=self.member,
                                                 date_issue__range=(start, end)).select_related('member')
        all_cumulative = {x.date_issue.strftime('%b'): x for x in query}
        # print(all_cumulative)
        for d in month_range:
            start_date, end_date = self._calculate_period(d)
            m_key = start_date.strftime('%b')
            data[m_key] = False
            if m_key in all_cumulative:
                if all_cumulative[m_key].value >= 2200:
                    data[m_key] = True
        return data

    def get_all_buy_data(self, start, end):
        month_range = self._calculate_month_range(start, end)
        data = {}
        query = SaleStatement.objects.filter(member=self.member,
                                             date_issue__range=(start, end),
                                             bill_type__code='HL').exclude(bill_state__code='CL') \
            .select_related('member') \
            .annotate(month=TruncMonth('date_issue')) \
            .values('member__member_code', 'month').annotate(total=Sum('pv')).order_by('-member')

        query_pv = PvTransferStatement.objects.filter(member=self.member,
                                                      date_issue__range=(start, end),
                                                      bill_type__code='HPV').exclude(bill_state__code='CL') \
            .select_related('member') \
            .annotate(month=TruncMonth('date_issue')) \
            .values('member__member_code', 'month').annotate(total=Sum('value')).order_by('-member')
        all_cumulative = {x['month'].strftime('%b'): x for x in query}
        all_transfer = {x['month'].strftime('%b'): x for x in query_pv}
        # print(all_cumulative)
        for d in month_range:
            start_date, end_date = self._calculate_period(d)
            m_key = start_date.strftime('%b')
            if m_key in all_cumulative:
                data[m_key] = all_cumulative[m_key]['total']
            else:
                data[m_key] = 0

            if m_key in all_transfer:
                data[m_key] += all_transfer[m_key]['total']

            #     if all_cumulative[m_key]['total'] >= 40000:
            #         data[m_key] = True
        return data
