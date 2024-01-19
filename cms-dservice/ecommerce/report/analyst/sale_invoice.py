from core.report.summary import PeriodSummaryBase
from ecommerce.models import SaleInvoice


class SaleInvoiceAnalyst(PeriodSummaryBase):
    """
    a class for represent member's `Chance of repeat purchases`
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        member_code (str): member code that interested (Optional)
    """
    class Meta:
        model = SaleInvoice
        date_fields = "sadate"
        filter = {"sa_type__in": ["A", "H", "L"], "total__gt": 10}
        exclude = {"cancel": 1}

    def __init__(self, *args, **kwargs):
        super(SaleInvoiceAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "daily")
        self.member_code = kwargs.get("mcode", None)

    def get_extend_queryset(self, queryset):
        """
        a method that overwrite from class PeriodSummaryBase to extend filter query and group data by member code

        :param queryset: queryset is a data set that get from model

        :return: queryset after reform
        """
        pool = {}
        if self.member_code:
            pool[self.member_code] = queryset.filter(mcode=self.member_code).order_by("-sadate")
        else:
            mcode_list = queryset.values_list("mcode", flat=True).distinct()
            for mc in mcode_list:
                pool[mc] = queryset.filter(mcode=mc).order_by("-sadate")
        return pool

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have member code is a key and sub-key is date delta

        :return: (:obj:`dictionary`)
        """
        pool = {}
        instance = self.get_query_set(self.start, self.end, self.get_type)
        for mcode, query_set in instance.items():
            pool[mcode] = {}
            temp_list = []
            for i in range(query_set.count()):
                if i+1 == query_set.count():
                    break
                delta = query_set[i].sadate - query_set[i + 1].sadate
                temp_list.append(delta.days)
            for day_diff in list(set(temp_list)):
                pool[mcode][str(day_diff)] = temp_list.count(day_diff)
        return pool
