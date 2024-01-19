from django.db.models import Sum
from member.models import Member
from commission.models import PvTransfer
from ecommerce.models import SaleInvoice
from commission.models import WeakStrongSummary
from commission.models import WeekRound


class PvStrongTeamCheck(object):

    def __init__(self, select_round):
        self.select_round = WeekRound.objects.get(rcode=select_round)
        return

    def calculate_strong_pv_team(self, select_round):
        querySet = WeakStrongSummary.objects.filter(rcode=select_round, quota__lt=0, total__lt=0).select_related('member')
        for x in querySet:
            pass

    def get_strong_pv(self, instance):
        member = instance.member
        weak_team = instance.weak_team
        period = self.select_round.period
        child_index = member.child_tree_meta

        filter_query = {
            'sadate__range': (period['start'], period['end']),
            'member__sponsor_lft__gt': member.sponsor_lft,
            'member__sponsor_rgt__gt': member.sponsor_rgt,
            'sa_type': 'A',
            'cancel': 0
        }

        if weak_team['dir'] == 'L':
            filter_query['member__line_lft__gt'] = child_index['L']['lft']
            filter_query['member__line_lft__gt'] = child_index['L']['rgt']
        else:
            filter_query['member__line_lft__gt'] = child_index['R']['lft']
            filter_query['member__line_lft__gt'] = child_index['R']['rgt']

        pv_statement = PvTransfer.objects.filter(**filter_query).aggregate(total_strong_pv=Sum('tot_pv'))
        sales_statement = SaleInvoice.objects.filter(**filter_query).aggregate(total_strong_pv=Sum('tot_pv'))

        return pv_statement + sales_statement