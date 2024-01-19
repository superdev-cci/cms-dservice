import datetime
from collections import OrderedDict
from datetime import date
from django.db.models import Prefetch, Sum, Q
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1, BUILTIN_FORMATS

from core.mixin import MonthMixIn
from core.report.excel import ExcelTemplateReport
from core.report.summary import ExcelMonthSummaryReport
from ecommerce.models import SaleInvoice, \
    SaleItem, \
    Product, \
    Promotion, \
    PromotionItem


class SoldItemMonthlySummary(ExcelMonthSummaryReport):
    template_file = './templates/report/ecommerce/sold_daily_item_summary.xlsx'
    select_bill = ('A', 'H', 'L', 'B', 'PM')

    class Meta:
        title = 'Sold summary'
        sheet_name = 'Summary'
        file_name = 'sold_item_monthly_summary'
        head_file = 'Sold summary'
        head_start_col = 4
        head_start_row = 7
        content_start_col = 1
        content_start_row = 8

    def __init__(self, **kwargs):
        super(SoldItemMonthlySummary, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        if isinstance(self.start, str):
            self.start = datetime.datetime.strptime(self.start, '%Y-%m-%d').date()

        self.end = kwargs.get('end', None)
        if isinstance(self.end, str):
            self.end = datetime.datetime.strptime(self.end, '%Y-%m-%d').date()

        self.product_pool = {x.pcode: {
            'pdesc': x.pdesc,
            'prices': x.price,
            'pv': x.pv,
        } for x in Product.objects.all()}
        self.promotion_pool = {x.pcode: {
            'prices': x.price,
            'pv': x.pv,
            'items': []
        } for x in Promotion.objects.all()}
        for x in PromotionItem.objects.all():
            self.promotion_pool[x.package]['items'].append({
                'pcode': x.pcode,
                'qty': x.qty
            })

        self.select_item_pool = []
        self.date_pool = []
        return

    def create_head(self):
        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')
        # if self.promotion:
        #     self.work_sheet['G4'] = self.promotion.code
        #     self.work_sheet['H4'] = self.promotion.name
        # super(SoldItemDailySummary, self).create_head()

    def build_row_meta(self, row_index, data, pcode, **kwargs):
        column = []
        for x in self.date_pool:
            if x in data:
                column.append((x, {
                    'data': data[x],
                    'number_format': BUILTIN_FORMATS[3]
                }))
            else:
                column.append((x, {
                    'data': 0,
                    'number_format': BUILTIN_FORMATS[3]
                }))

        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('pcode', {'data': pcode, 'alignment': self.style['align_center']}),
            ('pdesc', {'data': self.product_pool[pcode]['pdesc'], 'alignment': self.style['align_center']}),
            *column
        ])
        return meta

    def get_query_set(self, date_issue):
        start, end = self.calculate_period(date_issue)
        query_set = SaleItem.objects.filter(sadate__range=(start, end), sano_link__cancel=0,)\
            .filter(~Q(sano_link__bill_state__in=('OR', 'CA', 'PP'))) \
            .values('pcode', 'pdesc') \
            .annotate(qty=Sum('qty')) \
            .order_by('pcode')
        # query_set = query_set.select_related('bill_type', 'member', 'create_by__user', 'branch')

        return query_set

    def fill_sum_row(self, last_row):
        current_col = self.Meta.content_start_col + 5
        start_row = self.Meta.content_start_row
        cell = self.get_cell(current_col, last_row)

        for i in range(current_col, current_col + 7):
            cell_range = self.get_string_cell_range(i, start_row, i, last_row - 1)
            cell.value = '=SUM({})'.format(cell_range)
            cell.number_format = FORMAT_NUMBER_COMMA_SEPARATED1
            self.apply_border(cell)
            cell = self.next_cell(cell, 1, 0)

        return

    def push_item(self, pool, item, qty):
        if item in pool:
            pool[item] += qty
        else:
            pool[item] = qty

        if item not in self.select_item_pool:
            self.select_item_pool.append(item)
        return

    def process_data(self):
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        pool = {}
        m_range = self._calculate_month_range(self.start, self.end)
        for x in m_range:
            current = x.strftime('%Y-%b')
            self.date_pool.append(current)
            query_set = self.get_query_set(x)
            pool[current] = {}
            for x in query_set:
                qty = x['qty']
                if x['pcode'] in self.product_pool:
                    self.push_item(pool[current], x['pcode'], qty)
                else:
                    if x['pcode'] not in self.promotion_pool:
                        continue
                    promotion = self.promotion_pool[x['pcode']]
                    for p in promotion['items']:
                        self.push_item(pool[current], p['pcode'], qty * p['qty'])

        self.select_item_pool = sorted(self.select_item_pool)

        start_row = self.Meta.head_start_row
        start_col = self.Meta.head_start_col
        for x in pool.keys():
            self.work_sheet.cell(row=start_row, column=start_col).value = x
            start_col += 1

        new_pool = {x: {} for x in self.select_item_pool}

        for k, v in pool.items():
            for k1, v1 in v.items():
                new_pool[k1][k] = v1

        for k, v in new_pool.items():
            self.fill_row(count, v, k, row=current_row)
            count += 1
            current_row += 1
        return

    @property
    def file_name(self):
        name = '{}'.format(self.Meta.file_name)
        return '{}.xlsx'.format(name)
