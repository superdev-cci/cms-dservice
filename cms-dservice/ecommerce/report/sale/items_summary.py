from django.db.models import Sum
from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleItem, Product, Promotion


class SaleItemSummaryReport(PeriodSummaryBase):
    """
    a class represent summary item sold (amount and quantity)
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        use_only_value (boolean): True/False default if False
        select_item (:obj:`list`): list of products
        select_group (str): product's group
    """
    sale_select = ('A', 'H', 'L', 'B', 'CF')

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

    def __init__(self, *args, **kwargs):
        super(SaleItemSummaryReport, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get('get_type', None)
        self.use_only_value = kwargs.get('only_value', False)
        if isinstance(self.use_only_value, str):
            self.use_only_value = True if self.use_only_value == 'true' else False
        self.select_bill = kwargs.get('bill', self.sale_select)
        if isinstance(self.select_bill, str):
            self.select_bill = self.select_bill.split(',')
        self.select_item = kwargs.get('item', None)
        if self.select_item is not None:
            self.select_item = self.select_item.split(',')
        self.select_group = kwargs.get('select_group', None)

    def filter_queryset(self, queryset):
        """
        a method for filter queryset by optional attribute (`use_only_value`, `select_item`, `select_group`)

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        queryset = super(SaleItemSummaryReport, self).filter_queryset(queryset)
        if self.use_only_value:
            queryset = queryset.filter(sano_link__sa_type__in=self.select_bill)
        if self.select_item:
            queryset = queryset.filter(pcode__in=self.select_item)
        if self.select_group:
            queryset = queryset.filter(pcode__startswith=self.select_group)
        return queryset

    def get_extend_queryset(self, queryset):
        """
        a method for annotate and order data in queryset

        :param queryset: queryset is a data set that get from model

        :return: quertset after annotate and order
        """
        return queryset.values('time', 'pcode', ) \
            .annotate(total_prices=Sum('amt'), total_qty=Sum('qty')) \
            .order_by('time', 'pcode', )

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have date is a key and sub-key is product code

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for x in queryset:
            dt = x['time'].strftime('%Y-%m-%d')
            pcode = x['pcode']
            if pool.get(dt) is None:
                pool[dt] = {}
            pool[dt][pcode] = {'total_prices': float(x['total_prices']), 'total_qty': float(x['total_qty'])}
        return pool

    @property
    def total_item(self):
        """
        a method to process data and reform to dictionary that have product code is a key.
        this dictionary data combine amount and quantity between individual sales and promotion sales

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        product_id = []
        for x in queryset:
            product_id.append(x['pcode'])
        products = {x.pcode: x for x in Product.objects.filter(pcode__in=product_id)}
        promotions = {x.pcode: x for x in Promotion.objects.filter(pcode__in=product_id).prefetch_related('items')}
        for x in queryset:
            pcode = x['pcode']
            if pcode in products:
                total_item = int(x['total_qty'])
                if pcode not in pool:
                    pool[pcode] = {
                        'code': pcode,
                        'description': products[pcode].pdesc,
                        "qty": total_item
                    }
                else:
                    pool[pcode]['qty'] += total_item

            elif pcode in promotions:
                promotion = promotions[pcode]
                for pitem in promotion.items.all():
                    total_item = int(x['total_qty']) * int(pitem.qty)
                    if pitem.pcode not in pool:
                        pool[pitem.pcode] = {
                            'code': pcode,
                            'description': pitem.pdesc,
                            "qty": total_item
                        }
                    else:
                        pool[pitem.pcode]['qty'] += total_item
        return pool

    @property
    def summary(self):
        """
        a method to process data and reform to dictionary that have product code is a key.

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        product_id = []
        for x in queryset:
            product_id.append(x['pcode'])

        if self.select_group == 'CCI':
            products = {x.pcode: x for x in Product.objects.filter(pcode__in=product_id)}
        else:
            products = {x.pcode: x for x in Promotion.objects.filter(pcode__in=product_id)}

        for x in queryset:
            pcode = x['pcode']
            if pcode in products:
                total_item = int(x['total_qty'])
                if pcode not in pool:
                    pool[pcode] = {
                        'code': pcode,
                        'description': products[pcode].pdesc,
                        "qty": total_item
                    }
                else:
                    pool[pcode]['qty'] += total_item
        return pool
