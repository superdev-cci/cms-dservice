import calendar
import datetime

from django.db.models import Sum
from commission.models import WeekCommission


class CapLockInspect(object):
    cap_limit = 300

    def __init__(self, select_round, *args, **kwargs):
        self.member_match = []
        self.cms_adjust_pool = {}
        self.select_round = select_round

        self.total_pv = WeekCommission.get_total_pv(select_round)
        fast, ws = WeekCommission.get_total_bonus(select_round)
        self.total_cms = fast + ws
        self.total_ws = fast
        self.total_fast = ws

    @property
    def caplock_percent(self):
        return (self.total_cms / self.total_pv) * 100

    def calculate_paid_percent(self, value, pv_weak_team):
        return (value / pv_weak_team) * 100

    def print_caplock_result(self, instance):
        member = instance['member_instance']
        cms_instance = instance['cms_instance']
        new_cms = self.get_cms_group_with_factor(cms_instance, instance['tree_select'])
        paid_percent = self.calculate_paid_percent(new_cms, instance['pv_weak_team'])
        diff_percent = 100 - ((new_cms / instance['paid_total']) * 100)
        paid_diff = instance['paid_total'] - new_cms
        print('Befor adjust Member :{} / {} --> factor : {:.2f}, percent : {:.2f}, Weak team : {:,}'
              .format(member.code, member.full_name, instance['factor'], instance['paid_percent'],
                      instance['pv_weak_team']))
        print(
            'After adjust member :{} / {} --> Paid : {:,.2f}, '
            'percent : {:.2f}, Weak team : {:,}, Group direction : {}'.format(member.code, member.full_name, new_cms,
                                                                              paid_percent, instance['pv_weak_team'],
                                                                              instance['weak_dir']))
        print('Paid Diff : {:,.2f}, Percent diff : {:,.2f}'.format(paid_diff, diff_percent))

    def get_query_group(self, selector):
        query_set = self.cms_round.weekcommission_set.filter(member__line_lft__gte=selector['lft'],
                                                             member__line_rgt__lte=selector['rgt']) \
            .select_related('member', 'member__person')
        return query_set

    def get_sum_ws_group(self, selector):
        query_set = self.cms_round.weekcommission_set.filter(member__line_lft__gte=selector['lft'],
                                                             member__line_rgt__lte=selector['rgt'])
        sum_value = query_set.aggregate(sum_ws=Sum('ws'))
        sum_ws_cms = sum_value['sum_ws']
        return sum_ws_cms if sum_ws_cms is not None else 0

    def update_factor(self, instance, value, selector):
        query_set = self.get_query_group(selector)
        query_set.update(group_caplock_factor=value)
        instance.group_caplock_factor = value
        instance.save()

    def get_cms_group_with_factor(self, instance, selector):
        query_set = self.get_query_group(selector)
        sum_cms_result = query_set.aggregate(sum_ws=Sum('ws'))

        sum_cms = (sum_cms_result['sum_ws'] * instance.group_caplock_factor) + instance.ws_with_factor
        return sum_cms

    def process_over(self, instance):
        direction_meta = instance.member.child_tree_meta

        cumulative = self.cms_round.cumulative.get(summary__member=instance.member)
        weak_team_pv = cumulative.balance
        direction = cumulative.weak_team_direction
        sum_ws_cms = 0
        if direction == 'L':
            left = direction_meta.get('L')
            tree_select = left

            if left is not None:
                sum_ws_cms = self.get_sum_ws_group(left)
        else:
            right = direction_meta.get('R')
            tree_select = right

            if right is not None:
                sum_ws_cms = self.get_sum_ws_group(right)

        if sum_ws_cms is None:
            sum_ws_cms = 0

        if weak_team_pv != 0:
            paid_percent = ((sum_ws_cms + instance.ws) / weak_team_pv) * 100
        else:
            paid_percent = 0
        return {
            'paid_percent': paid_percent,
            'tree_select': tree_select,
            'sum_ws_cms': sum_ws_cms,
            'weak_team_pv': weak_team_pv,
            'direction': direction
        }

    def inspect(self, instance):

        # data = self.process_over(instance)
        data = WeekCommission.calculate_summary(self.select_round, instance.line_lft, instance.line_rgt)
        paid_percent = data['ws']['percent']
        # tree_select = data['tree_select']

        if paid_percent > 220:
            print('{} {} : {}'.format(instance.mcode, instance.full_name, paid_percent))
            # adjust_factor = self.cap_limit / paid_percent
            # self.cms_adjust_pool[instance.member.code] = {
            #     'member_instance': instance.member,
            #     'cms_instance': instance,
            #     'tree_select': tree_select,
            #     'factor': adjust_factor,
            #     'paid_total': sum_ws_cms + instance.ws,
            #     'paid_percent': paid_percent,
            #     'pv_weak_team': weak_team_pv,
            #     'weak_dir': direction
            # }
            # self.member_match.append(tree_select)

        return

    def is_skip(self, member):
        skip_inspect = False
        if member.is_leaf_node():
            return True
        for instance in self.member_match:
            if member.line_lft >= instance['lft'] and member.line_rgt <= instance['rgt']:
                skip_inspect = True
                break
        return skip_inspect

    def process(self):
        self.member_match = []
        self.cms_adjust_pool = {}
        query = WeekCommission.objects.select_related('member').filter(rcode=self.select_round, ws_bonus__gt=10000) \
            .order_by('-ws_bonus')

        for x in query:
            self.inspect(x.member)

        # print('Total cms : {:,.2f}'.format(self.total_cms))
        # print('Total ws : {:,.2f}'.format(self.total_ws))
        # print('Total fast : {:,.2f}'.format(self.total_fast))
        # print('Total pv : {:,.2f}'.format(self.total_pv))
        # print('Percent : {:,.2f}'.format(self.caplock_percent))

        for k, v in self.cms_adjust_pool.items():
            print('Member :{} / {} --> factor : {:.2f}, percent : {:.2f}, Weak team : {:,}'
                  .format(k, v['member_instance'].full_name, v['factor'], v['paid_percent'], v['pv_weak_team']))
        return

    def find_child_percent(self):
        for k, v in self.cms_adjust_pool.items():
            cms_query = self.get_query_group(v['tree_select']).order_by('-ws')
            for instance in cms_query:
                result = self.process_over(instance)
                if result['paid_percent'] >= 300:
                    print('Member : {} : {} -> Percent : {:.2f} Weak team: {:,} Bonus: {:,}'.format(
                        instance.member.code,
                        instance.member.full_name,
                        result['paid_percent'],
                        result['weak_team_pv'],
                        result['sum_ws_cms']
                    ))

    def update_adjust_group(self):
        for k, v in self.cms_adjust_pool.items():
            self.update_factor(v['cms_instance'], v['factor'], v['tree_select'])
        return

    def display_adjust_result(self):
        for k, v in self.cms_adjust_pool.items():
            self.print_caplock_result(v)

    def filter_pv_statement(self):
        selector = self.cms_adjust_pool

    def print_all_cms(self, instance):
        direction_meta = instance.member.child_tree_meta

        return

    def inspect_member(self, member):
        return
