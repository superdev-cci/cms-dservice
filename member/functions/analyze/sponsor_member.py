from core.mixin import MonthMixIn
from members.models import Member


class MemberSponsor(MonthMixIn):

    def __init__(self, member_code, *args, **kwargs):
        self.member = Member.objects.get(member_code=member_code)

    def find_sponser_depth_count(self, member_entry, depth, max_depth, last_date):
        if depth == (max_depth - 1):
            return member_entry.sponsor_child.filter(register_date__lte=last_date).count()

        count = member_entry.sponsor_child.filter(register_date__lte=last_date).count()

        for x in member_entry.sponsor_child.filter(register_date__lte=last_date):
            count += self.find_sponser_depth_count(x, depth+1, max_depth, last_date)

        return count

    def get_all_data(self, start, end):
        month_range = self._calculate_month_range(start, end)
        data = {}
        for d in month_range:
            start_date, end_date = self._calculate_period(d)
            m_key = start_date.strftime('%b')
            # queryset = Member.objects.filter(sponsor=self.member, register_date__range=(start_date, end_date))
            total = self.find_sponser_depth_count(self.member, 0, 4, end_date)
            data[m_key] = total
            # data[m_key] = queryset.count()

        return data

    def get_org_count(self, start, end):
        month_range = self._calculate_month_range(start, end)
        data = {}
        for d in month_range:
            start_date, end_date = self._calculate_period(d)
            m_key = start_date.strftime('%b')
            queryset = Member.objects.filter(sponsor=self.member, register_date__range=(start_date, end_date))
            data[m_key] = queryset.count()

        return data

