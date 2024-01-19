from django.db.models import Sum

from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleItem, Product, Promotion


class SaleItemAnalyst(PeriodSummaryBase):
    """
    a class for present total product sales in interesting time period.
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        product_code (str): product code that interested (Optional)
    """
    class Meta:
        model = SaleItem
        date_fields = "sano_link__sadate"
        filter = {
            "sano_link__isnull": False,
            "sano_link__sa_type__in": ["A", "H", "L", "B", "CF"]
        }
        exclude = {
            "sano_link__cancel": 1
        }

    def __init__(self, *args, **kwargs):
        super(SaleItemAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "daily")
        self.product_code = kwargs.get("pcode", None)
        if self.product_code is not None:
            self.product_code = self.product_code.split(',')

    def get_extend_queryset(self, queryset):
        """
        a method that overwrite from class PeriodSummaryBase to extend filter query

        :param queryset: queryset is a data set that get from model

        :return: filtered queryset
        """
        if self.product_code:
            return queryset.filter(pcode__in=self.product_code)
        return queryset

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have product code is a key and sub-key is time period

        :return: (:obj:`dictionary`)
        """
        pool = {}
        instance = self.get_query_set(self.start, self.end, self.get_type)
        data_dict = instance.values("time", "pcode").annotate(sum_qty=Sum("qty")).order_by("time", "pcode")
        product_id = instance.values_list("pcode", flat=True).distinct()
        products = {x.pcode: x for x in Product.objects.filter(pcode__in=product_id)}
        promotions = {x.pcode: x for x in Promotion.objects.filter(pcode__in=product_id).prefetch_related('items')}
        for x in data_dict:
            if x["pcode"] in products:
                if x["pcode"] not in pool:
                    pool[x["pcode"]] = {
                        x["time"]: {
                            "qty_single_unit": int(x["sum_qty"]),
                            "qty_from_promotion": 0
                        }
                    }
                else:
                    if x["time"] not in pool[x["pcode"]]:
                        pool[x["pcode"]][x["time"]] = {
                            "qty_single_unit": int(x["sum_qty"]),
                            "qty_from_promotion": 0
                        }
                    else:
                        pool[x["pcode"]][x["time"]]["qty_single_unit"] += int(x["sum_qty"])
            elif x["pcode"] in promotions:
                prom_instance = promotions[x["pcode"]].items.all()
                for pitem in prom_instance:
                    if pitem.pcode not in pool:
                        pool[pitem.pcode] = {
                            x["time"]: {
                                "qty_single_unit": 0,
                                "qty_from_promotion": int(x["sum_qty"]) * int(pitem.qty)
                            }
                        }
                    else:
                        if x["time"] not in pool[pitem.pcode]:
                            pool[pitem.pcode][x["time"]] = {
                                "qty_single_unit": 0,
                                "qty_from_promotion": int(x["sum_qty"]) * int(pitem.qty)
                            }
                        else:
                            pool[pitem.pcode][x["time"]]["qty_from_promotion"] += int(x["sum_qty"]) * int(pitem.qty)
        return pool

