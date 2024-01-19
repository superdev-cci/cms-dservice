import functools
import operator
from copy import deepcopy
import json
from django.db.models import Sum
from openpyxl import Workbook
from commission.models import PvTransfer, WeekCommission
from core.data_analyzed.rebuild_tree import RebuildTree
from core.data_analyzed.statement import StatementGroup
from member.models import Member
from core.utility import dict_transfrom


class WeakTeamTree(RebuildTree):
    class Meta:
        statement_model = WeekCommission
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
        date_field = 'fdate'
        annotates = {
            'total': 'ws_bonus'
        }
        exclude = {
            'ws_bonus': 0
        }

    def __init__(self, *args, **kwargs):
        super(WeakTeamTree, self).__init__(*args, **kwargs)

    def get_node_data(self, node, data):
        if data is None:
            return node
        node['total'] = functools.reduce(operator.add, [x['total'] for x in data], 0)
        return node

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
