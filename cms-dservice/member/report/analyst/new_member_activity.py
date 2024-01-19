from django.db.models import Count, Max, Min, Avg, Q, Sum
from member.models import Member
from ecommerce.models import SaleInvoice
from commission.models import PvTransfer
from core.report.summary import PeriodSummaryBase
from datetime import datetime


class NewMemberPvTransferActivity(PeriodSummaryBase):
    """
    a class for present a Pv Transfer activity of member in distributor role
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        new_member_list (:obj:`list`): list of member code in distributor role
    """
    class Meta:
        model = PvTransfer
        date_fields = 'sadate'
        filter = {
            "cancel": 0,
            "tot_pv__gt": 0,
            "sa_type": "A"
        }
        exclude = {"remark": "แจงสมัคร"}

    def __init__(self, *args, **kwargs):
        super(NewMemberPvTransferActivity, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.new_member_list = Member.objects.filter(
            distributor_date__range=(kwargs.get("mstart", "2020-01-01"), kwargs.get("mend", "2020-02-29")),
            status_terminate=0,
            status_suspend=0
        ).values_list("mcode", flat=True).order_by("mcode").distinct()

    def get_extend_queryset(self, queryset):
        """
        a method that overwrite from class PeriodSummaryBase to extend filter query and group data by time period

        :param queryset: queryset is a data set that get from model

        :return: queryset after annotate and group by value
        """
        return queryset.filter(mcode__in=self.new_member_list).values("time", "mcode").annotate(
            sum_pv=Sum("tot_pv"),
            bill_qty=Count("id")
        ).values("time", "mcode", "bill_qty", "sum_pv").order_by("time", "mcode")

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have member code is a key and sub-key is time period

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for i in queryset:
            if i["mcode"] not in pool:
                pool[i["mcode"]] = {
                    datetime.strftime(i["time"], "%b-%Y"): {
                        "sum_pv": i["sum_pv"],
                        "bill_qty": i["bill_qty"]
                    }
                }
            else:
                if datetime.strftime(i["time"], "%b-%Y") not in pool[i["mcode"]]:
                    pool[i["mcode"]][datetime.strftime(i["time"], "%b-%Y")] = {
                        "sum_pv": i["sum_pv"],
                        "bill_qty": i["bill_qty"]
                    }
                else:
                    pool[i["mcode"]][datetime.strftime(i["time"], "%b-%Y")]["sum_pv"] += i["sum_pv"]
                    pool[i["mcode"]][datetime.strftime(i["time"], "%b-%Y")]["bill_qty"] += i["bill_qty"]
        return pool


class NewMemberSaleInvoiceActivity(PeriodSummaryBase):
    """
    a class for present a Sale Invoice activity of member in distributor role
    This class inherit class `PeriodSummaryBase` also you can use a method in PeriodSummaryBase or overwrite method
    and receive attribute from `PeriodSummaryBase`

    Attributes:
        start (:obj:`date`): a start date of interested data.
        end (:obj:`date`): a end date of interested data.
        get_type (str): time period option [daily, monthly, quarter, yearly]
        new_member_list (:obj:`list`): list of member code in distributor role
    """
    class Meta:
        model = SaleInvoice
        date_fields = 'sadate'
        filter = {
            "cancel": 0,
            "total__gt": 0,
            "sa_type__in": ["A","H"]
        }

    def __init__(self, *args, **kwargs):
        super(NewMemberSaleInvoiceActivity, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")
        self.new_member_list = Member.objects.filter(
            distributor_date__range=(kwargs.get("mstart", "2020-01-01"), kwargs.get("mend", "2020-02-29")),
            status_terminate=0,
            status_suspend=0
        ).values_list("mcode", flat=True).order_by("mcode").distinct()

    def get_extend_queryset(self, queryset):
        """
        a method that overwrite from class PeriodSummaryBase to extend filter query and group data by time period

        :param queryset: queryset is a data set that get from model

        :return: queryset after annotate and group by value
        """
        return queryset.filter(mcode__in=self.new_member_list).values("time", "mcode").annotate(
            sum_total=Sum("total"),
            sum_pv=Sum("tot_pv"),
            bill_qty=Count("id")
        ).values("time", "mcode", "bill_qty", "sum_pv", "sum_total").order_by("time", "mcode")

    @property
    def total(self):
        """
        a method to process data and reform to dictionary that have member code is a key and sub-key is time period

        :return: (:obj:`dictionary`)
        """
        pool = {}
        queryset = self.get_query_set(self.start, self.end, self.get_type)
        for i in queryset:
            if i["mcode"] not in pool:
                pool[i["mcode"]] = {
                    datetime.strftime(i["time"], "%b-%Y"): {
                        "sum_total": i["sum_total"],
                        "sum_pv": i["sum_pv"],
                        "bill_qty": i["bill_qty"]
                    }
                }
            else:
                if datetime.strftime(i["time"], "%b-%Y") not in pool[i["mcode"]]:
                    pool[i["mcode"]][datetime.strftime(i["time"], "%b-%Y")] = {
                        "sum_pv": i["sum_pv"],
                        "sum_total": i["sum_total"],
                        "bill_qty": i["bill_qty"]
                    }
                else:
                    pool[i["mcode"]][datetime.strftime(i["time"], "%b-%Y")]["sum_pv"] += i["sum_pv"]
                    pool[i["mcode"]][datetime.strftime(i["time"], "%b-%Y")]["sum_total"] += i["sum_total"]
                    pool[i["mcode"]][datetime.strftime(i["time"], "%b-%Y")]["bill_qty"] += i["bill_qty"]
        return pool
