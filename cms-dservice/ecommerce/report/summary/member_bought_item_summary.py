from django.db.models import Sum

from ecommerce.models import SaleItem, PromotionItem
from ecommerce.report.base.sale import PureSaleItemSummary


class MemberBoughtItemSummary(PureSaleItemSummary):
    class Meta:
        model = SaleItem
        date_fields = 'sano_link__sadate'
        filter = {
            'sano_link__isnull': False
        }
        exclude = {
            'sano_link__cancel': 1,
            'sano_link__sa_type': 'I'
        }

        annotate = {
            'field': ('pcode', 'sano_link__mcode', 'sano_link__name_t', 'time'),
            'order': ('pcode', 'sano_link__mcode'),
            'function': {
                'total_prices': {
                    'fn': Sum,
                    'target': 'amt'
                },
                'total_qty': {
                    'fn': Sum,
                    'target': 'qty'
                }
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', 'daily')
        self.merge = kwargs.get('merge', True)
        return

    @property
    def total(self):
        pool = {}
        head_list = []
        code = []
        total = 0
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        all_promotion = {x.package: {'qty': x.qty, 'code': x.pcode} for x in
                         PromotionItem.objects.filter(pcode__in=self.select_item)}
        for x in queryset:
            # print(x)
            dt = x['time'].strftime('%Y-%m-%d')
            head_list.append(dt)
            member = x['sano_link__mcode']
            pcode = x['pcode']
            if pool.get(member) is None:
                pool[member] = {
                    'data': {},
                    'name': x['sano_link__name_t']
                }

            if pool[member]['data'].get(dt) is None:
                pool[member]['data'][dt] = {}

            if self.merge:
                if pcode in all_promotion:
                    count = float(x['total_qty']) * all_promotion[pcode]['qty']
                    pcode = all_promotion[pcode]['code']
                else:
                    count = float(x['total_qty'])
            else:
                count = float(x['total_qty'])
            code.append(pcode)
            if pcode in pool[member]['data'][dt]:
                pool[member]['data'][dt][pcode]['total_prices'] += float(x['total_prices'])
                pool[member]['data'][dt][pcode]['total_qty'] += count
            else:
                pool[member]['data'][dt][pcode] = {
                    'total_prices': float(x['total_prices']),
                    'total_qty': count,
                }
            total += count
        return pool, list(set(head_list)), list(set(code))

    @property
    def total_by_member(self):
        pool = {}
        head_list = []
        for k, v in self.total[0].items():
            pool[k] = {
                'name': v['name'],
                'data': {}
            }
            for values in v['data'].values():
                for pk, pv in values.items():
                    head_list.append(pk)
                    if pk in pool[k]['data']:
                        pool[k]['data'][pk]['total_prices'] += float(pv['total_prices'])
                        pool[k]['data'][pk]['total_qty'] += float(pv['total_qty'])
                    else:
                        pool[k]['data'][pk] = {
                            'total_prices': float(pv['total_prices']),
                            'total_qty': float(pv['total_qty']),
                        }

        return list(set(head_list)), pool
