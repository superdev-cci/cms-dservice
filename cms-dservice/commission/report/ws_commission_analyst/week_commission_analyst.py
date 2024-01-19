from django.db.models import Max, Min, Avg, Sum

from commission.models import WeekCommission
from core.report.summary import PeriodSummaryBase


class WeekCommissionAnalyst(PeriodSummaryBase):
    class Meta:
        model = WeekCommission
        date_fields = 'fdate'
        exclude = {"ws_bonus": 0}

    def __init__(self, *args, **kwargs):
        super(WeekCommissionAnalyst, self).__init__(*args, **kwargs)
        self.get_type = kwargs.get("get_type", "monthly")

    def get_extend_queryset(self, queryset):
        return queryset.values("time", "mcode").annotate(
            min=Min("ws_bonus"),
            avg=Avg("ws_bonus"),
            max=Max("ws_bonus"),
            sum=Sum("ws_bonus")
        ).values(
            "time",
            "mcode",
            "name_t",
            "min",
            "max",
            "avg",
            "sum",
            "member__distributor_date"
        ).order_by("time", "mcode")

    @property
    def total(self):
        pool = {}
        query_data = self.get_query_set(self.start, self.end, self.get_type)
        for x in query_data:
            if x["mcode"] not in pool:
                pool[x["mcode"]] = {
                    "name": x["name_t"],
                    "distributor_date": x["member__distributor_date"],
                    "data_record": {
                        x["time"]: {"min": x["min"], "max": x["max"], "sum": x["sum"], "avg": x["avg"]}
                    }
                }
            else:
                pool[x["mcode"]]["data_record"][x["time"]] = {
                    "min": x["min"], "max": x["max"], "sum": x["sum"], "avg": x["avg"]
                }
        return pool

