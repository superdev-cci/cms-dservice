import functools
import operator
from commission.models import PvTransfer
from core.data_analyzed.rebuild_tree import RebuildTree


class PvTransferInSponsorTree(RebuildTree):
    class Meta:
        statement_model = PvTransfer
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
        date_field = 'sadate'
        annotates = {
            'total': 'tot_pv'
        }
        exclude = {
            'tot_pv': 0,
            'remark': 'แจงสมัคร'
        }

    def __init__(self, *args, **kwargs):
        super(PvTransferInSponsorTree, self).__init__(*args, **kwargs)

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

    def get_extend_queryset(self, queryset):
        sponsor_child = self.member.sponsor_child().values_list("mcode", flat=True).order_by("mcode")
        return queryset.filter(mcode__in=sponsor_child)
