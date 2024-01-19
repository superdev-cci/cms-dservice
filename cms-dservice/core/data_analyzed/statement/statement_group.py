import operator
from functools import reduce

from django.db.models import Q

from core.utility import dict_transfrom


class StatementGroup(object):

    def get_meta_class(self):
        return getattr(self, 'Meta')

    def get_statement_model(self):
        meta = getattr(self, 'Meta')
        return meta.statement_model

    def get_statement(self, start, end, stype, selector):
        queryset = self.get_statement_queryset(start, end, stype, selector)
        pool = {}

        for x in queryset:
            if pool.get(x.member.code) is None:
                pool[x.member.code] = {
                    'value': x.value,
                    'depth': x.member.line_depth,
                    'lft': x.member.line_lft,
                    'rgt': x.member.line_rgt,
                    'member': x.member.code,
                    'name': x.member.full_name,
                    'level': x.member.get_level(),
                    'instance': x.member,
                }
            else:
                pool[x.member.code]['value'] += x.value
                # pool[x.member.code]['from'].append(x.create_by.member.code)

        return dict_transfrom.dict_to_list(pool)

    def get_statement_queryset(self, start, end, selector):
        meta = self.get_meta_class()
        model = self.get_statement_model()
        date_field = meta.date_field
        queryset = model.objects.filter(Q(**{'{}__range'.format(date_field): (start, end)}),
                                        member__line_lft__gte=selector['lft'],
                                        member__line_rgt__lte=selector['rgt']
                                        )
        if hasattr(meta, 'satype'):
            queryset = queryset.filter(Q(**{meta.satype[0]: meta.satype[1]}))

        if hasattr(meta, 'exclude'):
            queries = []
            for k, v in meta.exclude.items():
                queries.append(~Q(**{k: v}))
            queryset = queryset.filter(reduce(operator.and_, queries))

        queryset = queryset.order_by('member__line_depth')

        if getattr(meta, 'statement_select_related'):
            queryset = queryset.select_related(*meta.statement_select_related)

        return self.get_extend_queryset(queryset)

    def get_extend_queryset(self, queryset):
        return queryset

    def add_node(self, left, right, extra_data, node=None):
        meta = getattr(self, 'Meta')
        member = getattr(self, 'member')
        if node is None:
            if member is None:
                raise AttributeError('Instance doesn\'t has member attribute')
        else:
            member = node

        data = {
            'total': 0,
            'child': {
                'left': left,
                'right': right
            }
        }
        for k, v in meta.member_detail.items():
            data[k] = getattr(member, v)

        return self.get_node_data(data, extra_data)

    def get_node_data(self, node, data):
        return node
