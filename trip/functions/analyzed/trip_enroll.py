import datetime
import functools
import operator

from django.db.models import Sum
from core.utility import dict_transfrom
from commission.models import WeekCommission
from core.mixin.trip_calculator_mixin import TripCalculatorMixin
from member.models import Member
from trip.functions import TripCalculator
from trip.models import Trip, TripApplication


class TripEnrollAnalyzed(TripCalculatorMixin):
    class Meta:
        statement_select_related = ('member',)
        member_detail = {
            'code': 'code',
            'name': 'full_name',
            'level': 'level',
            'honor': 'honor',
            'depth': 'line_depth',
            'lft': 'line_lft',
            'rgt': 'line_rgt',
        }

    def __init__(self, member, trip, *args, **kwargs):
        super(TripEnrollAnalyzed, self).__init__()
        if isinstance(trip, Trip):
            self.trip = trip
        else:
            self.trip = Trip.objects.get(code=trip)

        self.member = Member.objects.get(mcode=member)
        self.filter_type = kwargs.get('filter', None)
        self.treeDepth = kwargs.get('depth', 5)

    def get_overlap_enroll(self, trips):
        query = TripApplication.objects.filter(trip__in=trips,
                                               member__line_lft__gte=self.member.line_lft,
                                               member__line_rgt__lte=self.member.line_rgt
                                               ).values('member__mcode') \
            .annotate(total=Sum('balance_use')).order_by('total')

        return {x['member__mcode']: x['total'] for x in query}

    def calculate(self):
        # overlap_trip = self.get_overlap_trip(self.trip)
        # overlap_pool = self.get_overlap_enroll(overlap_trip)
        # overlap_trip = overlap_trip.first()
        trip_cumulative = WeekCommission.objects.filter(fdate__range=(self.trip.start, self.trip.end),
                                                        member__line_lft__gte=self.member.line_lft,
                                                        member__line_rgt__lte=self.member.line_rgt
                                                        ) \
            .values('mcode') \
            .annotate(total_balance=Sum('ws_bonus')).order_by('mcode').order_by('-total_balance')

        pool = {}

        for x in trip_cumulative:
            total_balance = int(x['total_balance'])
            if total_balance < (self.trip.balance / 4):
                continue

            mcode = x['mcode']
            calculator = TripCalculator(mcode)
            member = calculator.member
            new_balance, consume_with_previous, consume_with_overlap = calculator.get_trip_summary(member, self.trip)

            if new_balance < (self.trip.balance / 4):
                continue
            out_bound_trip = TripApplication.objects.filter(member__mcode=mcode, trip__trip_type='OS')
            if out_bound_trip.count() > 0:
                right = new_balance // self.trip.balance
                entry = 'Old'
            else:
                right = new_balance // (self.trip.balance - self.trip.balance_discount)
                entry = 'New'
            if right > self.trip.max_seat:
                right = self.trip.max_seat

            pool[mcode] = {
                'right': right,
                'balance': new_balance,
                'use_other_trip': consume_with_previous,
                'overlap_trip': consume_with_overlap,
                'entry_type': entry
            }

        members = Member.objects.filter(mcode__in=pool.keys())
        for x in members:
            pool[x.mcode]['name'] = x.full_name
            pool[x.mcode]['level'] = x.level
            pool[x.mcode]['status'] = x.status
            pool[x.mcode]['lft'] = x.line_lft
            pool[x.mcode]['rgt'] = x.line_rgt
            pool[x.mcode]['depth'] = x.line_depth
            pool[x.mcode]['child'] = []
            pool[x.mcode]['honor'] = x.honor
        return pool

    def create_tree(self):
        pool = self.calculate()
        all_data = sorted(pool.values(), key=lambda x: x['lft'])
        if self.filter_type is not None:
            all_data = [x for x in all_data if x['entry_type'] == self.filter_type]
        node = self.rebuild_tree(pool, all_data, self.treeDepth, 0, {'count': 1})
        return node

    def rebuild_tree(self, data, pool, max_depth, depth, count):
        # print('Entry :', depth, count)
        count['count'] += 1
        # print(datetime.datetime.now())
        if max_depth is not None:
            if depth >= max_depth:
                # print('max depth')
                return

        final = False
        if depth == max_depth:
            final = True
        if len(pool) is 0:
            return
        lft = pool[0]['lft']
        rgt = pool[-1]['rgt']
        query = Member.objects.filter(line_lft__lte=lft, line_rgt__gte=rgt) \
            .order_by('-line_lft')

        node = query.first()
        mask = False
        current_node = data.get(node.code, {})
        if node.code in data:
            mask = True
        current_node['mask'] = mask
        tree_selector = node.child_tree_meta

        if 'L' in tree_selector:
            left_pool = [x for x in pool if
                         x['lft'] >= tree_selector['L']['lft'] and x['rgt'] <= tree_selector['L']['rgt']]
        else:
            left_pool = []

        if 'R' in tree_selector:
            right_pool = [x for x in pool if
                          x['lft'] >= tree_selector['R']['lft'] and x['rgt'] <= tree_selector['R']['rgt']]
        else:
            right_pool = []
        if len(left_pool) > 1:
            left_pool = sorted(left_pool, key=lambda x: x['lft'])
            left_node = self.rebuild_tree(data, left_pool, max_depth, depth + 1, count)
        elif len(left_pool) is 1 and final is True:
            left_node = {
                **left_pool[0],
                'child': {
                    'left': None,
                    'right': None
                }
            }
        elif len(left_pool) is 1 and final is False:
            left_pool = sorted(left_pool, key=lambda x: x['lft'])
            left_node = self.rebuild_tree(data, left_pool, max_depth, depth + 1, count)
        else:
            left_node = None

        if len(right_pool) > 1:
            right_pool = sorted(right_pool, key=lambda x: x['lft'])
            right_node = self.rebuild_tree(data, right_pool, max_depth, depth + 1, count)
        elif len(right_pool) is 1 and final is True:
            right_node = {
                **right_pool[0],
                'child': {
                    'left': None,
                    'right': None
                }
            }
        elif len(right_pool) is 1 and final is False:
            right_pool = sorted(right_pool, key=lambda x: x['lft'])
            right_node = self.rebuild_tree(data, right_pool, max_depth, depth + 1, count)
        else:
            right_node = None

        node_data = self.add_node(left_node, right_node, current_node, node)
        node_data['total'] = functools.reduce(operator.add, [x['right'] for x in pool], 0)
        node_data['left_side'] = len(left_pool)
        node_data['right_side'] = len(right_pool)
        # node_data['total'] = functools.reduce(operator.add, [x['total'] for x in pool], 0)

        return node_data

    def add_node(self, left, right, extra_data, node=None):
        meta = getattr(self, 'Meta')
        member = getattr(self, 'member')
        if node is None:
            if member is None:
                raise AttributeError('Instance doesn\'t has member attribute')
        else:
            member = node

        data = {
            'child': {
                'left': left,
                'right': right
            }
        }
        for k, v in meta.member_detail.items():
            data[k] = getattr(member, v)

        return self.get_node_data(data, extra_data)

    def get_node_data(self, node, data):
        node['right'] = data.get('right', 0)
        node['mask'] = data.get('mask', False)
        node['balance'] = data.get('balance', 0)
        node['use_other_trip'] = data.get('use_other_trip', 0)
        node['entry_type'] = data.get('entry_type', 0)
        return node
