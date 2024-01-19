import functools
import operator
from copy import deepcopy
import json
from django.db.models import Sum
from openpyxl import Workbook
from core.data_analyzed.statement import StatementGroup
from member.models import Member
from core.utility import dict_transfrom


class RebuildTree(StatementGroup):

    def __init__(self, *args, **kwargs):
        # super(RebuildTree, self).__init__(*args, **kwargs)
        self.context = kwargs
        self.start = kwargs.get('start', '')
        self.end = kwargs.get('end', '')

        self.member = Member.objects.get(mcode=kwargs.get('member'))
        self.tree_selector = self.member.child_tree_meta
        self.tree = {}
        self.statement = {}

    def process(self, depth=None):
        left_sel = self.tree_selector.get('L', None)
        right_sel = self.tree_selector.get('R', None)

        if left_sel is not None:
            left = self.create_tree(left_sel, depth)
        else:
            left = None

        if right_sel is not None:
            right = self.create_tree(right_sel, depth)
        else:
            right = None

        self.tree = self.add_node(left, right, None)

        if left:
            self.tree['total'] += left['total']

        if right:
            self.tree['total'] += right['total']

        # return self.tree
        return self.tree

    def create_tree(self, selector, depth=None):
        meta = getattr(self, 'Meta', None)
        if meta is None:
            raise AttributeError('Meta class must defined')

        if hasattr(meta, 'annotates'):
            annotates = meta.annotates
        else:
            raise AttributeError('sum must defined')

        y = self.get_statement_queryset(self.start, self.end, selector)
        z = y.values('member',
                     'member__level', 'member__honor',
                     'member__name_t',
                     'member__line_depth', 'member__line_lft', 'member__line_rgt',
                     'member__mcode')
        annotate_list = {}
        for k, v in annotates.items():
            annotate_list[k] = Sum(v)
        z = z.annotate(**annotate_list).order_by('member__line_depth', )

        pool = {}
        if len(z):
            all_data = [x for x in z]
            for x in all_data:
                new_item = self.create_instance(x['member__mcode'], x)
                pool[x['member__mcode']] = new_item

            all_data = sorted(pool.values(), key=lambda x: x['lft'])

            node = self.rebuild_tree(all_data, depth, 0)
        else:
            node = None

        return node

    def rebuild_tree(self, pool, max_depth, depth):

        if max_depth is not None:
            if depth >= max_depth:
                return

        if len(pool) is 0:
            return
        lft = pool[0]['lft']
        rgt = pool[-1]['rgt']
        query = Member.objects.filter(line_lft__lte=lft, line_rgt__gte=rgt) \
            .order_by('-line_lft')
        # .prefetch_related('down_line')\

        node = query.first()
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
            left_node = self.rebuild_tree(left_pool, max_depth, depth + 1)
        elif len(left_pool) is 1:
            left_node = {
                **left_pool[0],
                'child': {
                    'left': None,
                    'right': None
                }
            }
        else:
            left_node = None

        if len(right_pool) > 1:
            right_pool = sorted(right_pool, key=lambda x: x['lft'])
            right_node = self.rebuild_tree(right_pool, max_depth, depth + 1)
        elif len(right_pool) is 1:
            right_node = {
                **right_pool[0],
                'child': {
                    'left': None,
                    'right': None
                }
            }
        else:
            right_node = None

        node_data = self.add_node(left_node, right_node, pool, node)
        # node_data['total'] = functools.reduce(operator.add, [x['total'] for x in pool], 0)

        return node_data

    def create_instance(self, key, data):
        return {
            'code': key,
            'name': '{}'.format(data['member__name_t']),
            'level': data['member__level'],
            'honor': data['member__honor'],
            'depth': data['member__line_depth'],
            'lft': data['member__line_lft'],
            'rgt': data['member__line_rgt'],
            'total': int(data['total']),
            'child': []
        }
