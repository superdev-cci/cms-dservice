from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleItem
from django.db.models import Sum
import pandas as pd


class SaleItemPerMonth(PeriodSummaryBase):
    class Meta:
        model = SaleItem
        date_fields = "sano_link__sadate"
        filter = {"sano_link__cancel": 0}

    def __init__(self, *args, **kwargs):
        super(SaleItemPerMonth, self).__init__(*args, **kwargs)
        self.get_type = "monthly"
        self.pcode = kwargs.get("pcode", [])

    def get_extend_queryset(self, queryset):
        if self.pcode:
            queryset = queryset.filter(pcode__in=self.pcode)
        queryset = queryset.values("time", "pcode").annotate(sum_qty=Sum("qty")).values(
            "time", "pcode", "pdesc", "sum_qty").order_by("time")
        return queryset

    @property
    def total(self):
        pool = {}
        instance = self.get_query_set(self.start, self.end, self.get_type)
        for i in instance:
            if i["time"].strftime("%Y-%b") not in pool:
                pool[i["time"].strftime("%Y-%b")] = {(i["pcode"], i["pdesc"]): float(i["sum_qty"])}
            else:
                pool[i["time"].strftime("%Y-%b")][(i["pcode"], i["pdesc"])] = float(i["sum_qty"])
        return pool


def get_monthly_product_sku(start="2019-07-01", end="2020-02-29", pcode=["CCI002", "CCI004", "CCI006"]):
    data_dict = SaleItemPerMonth(start=start, end=end, pcode=pcode).total
    df = pd.DataFrame.from_dict(data_dict)
    sorted_row = df.sort_index(axis=0)
    sorted_row.to_excel("./excel_sale_monthly_product_quantity.xlsx", na_rep=0, encoding="utf-8")