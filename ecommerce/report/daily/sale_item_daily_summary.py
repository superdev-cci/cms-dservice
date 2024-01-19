import datetime
from collections import OrderedDict
from datetime import date

from django.db.models import Sum
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from core.report.excel import ExcelTemplateReport
from ecommerce.models import SaleItem, Product, Promotion, PromotionItem


class SoldItemDailySummary(ExcelTemplateReport):
    """
    a class represent summary sold product
    This class inherit class `ExcelTemplateReport` also you can use a method in ExcelTemplateReport or overwrite method

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
    """
    template_file = './templates/report/ecommerce/sold_daily_item_summary.xlsx'
    select_bill = ('A', 'H', 'L', 'B', 'PM')

    class Meta:
        title = 'Sold summary'
        sheet_name = 'Summary'
        file_name = 'sold_item_summary'
        head_file = 'Sold summary'
        head_start_col = 4
        head_start_row = 7
        content_start_col = 1
        content_start_row = 8

    def __init__(self, **kwargs):
        super(SoldItemDailySummary, self).__init__(**kwargs)
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

    def create_head(self):
        """
        a method to process data to create Header of table in excel
        """
        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')

    def build_row_meta(self, row_index, data, pcode, **kwargs):
        """
        a method for index data with cell row

        :param row_index: (int) index of sheet row

        :param data: (:obj:`dictionary`) a content write in row

        :param pcode: (str) product code

        :return: (:obj:`dictionary`)
        """
        column = []
        for x in self.date_pool:
            if x in data:
                column.append((x, {
                    'data': data[x],
                    'number_format': FORMAT_NUMBER_COMMA_SEPARATED1
                }))
            else:
                column.append((x, {
                    'data': 0,
                    'number_format': FORMAT_NUMBER_COMMA_SEPARATED1
                }))

        meta = OrderedDict([
            ('no', {'data': row_index, 'alignment': self.style['align_center']}),
            ('pcode', {'data': pcode, 'alignment': self.style['align_center']}),
            ('pdesc', {'data': self.product_pool[pcode]['pdesc'], 'alignment': self.style['align_center']}),
            *column
        ])
        return meta

    def get_query_set(self, date_issue):
        """
        a method for process an information of SaleInvoice in interesting date

        :param date_issue: (str): string in date format

        :return: (:obj:`dictionary`)
        """
        query_set = SaleItem.objects.filter(sadate=date_issue, ).exclude(sano_link__cancel=1) \
            .values('pcode', 'pdesc').annotate(qty=Sum('qty')).order_by('pcode')
        return query_set

    def fill_sum_row(self, last_row):
        """
        a method for write summary data to last row

        :param last_row: index that identify last row
        """
        current_col = self.Meta.content_start_col + 5
        start_row = self.Meta.content_start_row
        cell = self.get_cell(current_col, last_row)

        for i in range(current_col, current_col + 7):
            cell_range = self.get_string_cell_range(i, start_row, i, last_row - 1)
            cell.value = '=SUM({})'.format(cell_range)
            cell.number_format = FORMAT_NUMBER_COMMA_SEPARATED1
            self.apply_border(cell)
            cell = self.next_cell(cell, 1, 0)

    def push_item(self, pool, item, qty):
        """
        a method for insert data(item and quality item) to pool data

        :param pool: (:obj:`dictionary`)

        :param item: (str)

        :param qty: (int)
        """
        if item in pool:
            pool[item] += qty
        else:
            pool[item] = qty

        if item not in self.select_item_pool:
            self.select_item_pool.append(item)

    def process_data(self):
        """
        a method to process data in excel object
        """
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        pool = {}
        in_process = True
        current_day = self.start
        while in_process:
            current = current_day.strftime('%Y-%m-%d')
            print(current_day.strftime('%Y-%m-%d'))
            self.date_pool.append(current)
            query_set = self.get_query_set(current_day)
            pool[current] = {}
            for x in query_set:
                qty = x['qty']
                if x['pcode'] in self.product_pool:
                    self.push_item(pool[current], x['pcode'], qty)
                else:
                    promotion = self.promotion_pool[x['pcode']]
                    for p in promotion['items']:
                        self.push_item(pool[current], p['pcode'], qty * p['qty'])
            try:
                next_day = current_day.replace(day=current_day.day + 1)
                if next_day.day > self.end.day:
                    in_process = False
                current_day = next_day
            except Exception as e:
                in_process = False

        self.select_item_pool = sorted(self.select_item_pool)
        start_row = self.Meta.head_start_row
        start_col = self.Meta.head_start_col
        for x in pool.keys():
            self.work_sheet.cell(row=start_row, column=start_col).value = x
            start_col += 1

        new_pool = {x: {} for x in self.select_item_pool}
        for k, v in pool.items():
            print('{}: {}'.format(k, v))
            for k1, v1 in v.items():
                new_pool[k1][k] = v1
        print(new_pool)
        for k, v in new_pool.items():
            print('{}: {}'.format(k, v))
            self.fill_row(count, v, k, row=current_row)
            count += 1
            current_row += 1

    def get_daily_sale(self, current_day):
        """
        a method for process an information on select date

        :param current_day: (:obj:`date object`)

        :return: (:obj:`dictionary`)
        """
        if current_day is None:
            current = datetime.date.today()
        else:
            current = datetime.datetime.strptime(current_day, '%Y-%m-%d').date()
        query_set = self.get_query_set(current.strftime('%Y-%m-%d'))
        date_str = current.strftime('%Y-%m-%d')
        pool = {date_str: {}}
        pool_desc = {}
        for x in query_set:
            if not x['pcode'].startswith('CCI'):
                continue
            qty = x['qty']
            pool_desc[x['pcode']] = {'description': x['pdesc']}

            if x['pcode'] in self.product_pool:
                self.push_item(pool[date_str], x['pcode'], int(qty))
            else:
                promotion = self.promotion_pool[x['pcode']]
                for p in promotion['items']:
                    self.push_item(pool[date_str], p['pcode'], int(qty * p['qty']))

        for k, v in pool[date_str].items():
            pool_desc[k]['qty'] = v

        return pool_desc

    @property
    def file_name(self):
        """
        a method to named a excel object

        :return: (str): excel object's file name
        """
        name = '{}'.format(self.Meta.file_name)
        return '{}.xlsx'.format(name)
