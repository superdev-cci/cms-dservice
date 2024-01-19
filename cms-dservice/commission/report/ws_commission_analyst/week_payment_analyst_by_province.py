from django.db.models import Count, Q
from commission.models import WeekPayment, MonthPayment
from member.models import Member


def find_month_paid_population(month_focus='2019-12-31'):
    primary = MonthPayment.objects.filter(date_issue=month_focus)
    result = primary.values("member__cprovinceid").annotate(pop=Count("mcode")).order_by("-pop")
    for i in result:
        print(i)


def find_week_paid_population(start_date='2019-12-22', end_date='2019-12-31'):
    primary = WeekPayment.objects.filter(date_issue__range=(start_date, end_date), paid_state=1)
    result1 = primary.values("member__provinceid").annotate(pop=Count("mcode")).order_by("-pop")
    result2 = primary.values("member__cprovinceid").annotate(pop=Count("mcode")).order_by("-pop")
    result = {}
    for i in result1:
        if i["member__provinceid"] not in result:
            result[i["member__provinceid"]] = {
                "pop_province": i["pop"],
                "pop_send_province": 0
            }
        else:
            result[i["member__provinceid"]]["pop_province"] += i["pop"]
    for i in result2:
        if i["member__cprovinceid"] not in result:
            result[i["member__cprovinceid"]] = {
                "pop_province": 0,
                "pop_send_province": i["pop"]
            }
        else:
            result[i["member__cprovinceid"]]["pop_send_province"] += i["pop"]
    for k, v in result.items():
        print(k, v)


def member_honor_by_province():
    primary = Member.objects.filter(~Q(honor=""), Q(status_terminate=0), Q(status_suspend=0))
    result = {}
    for i in primary.values("cprovinceid", "honor").annotate(pop=Count("mcode")).order_by("-pop"):
        if i["cprovinceid"] not in result:
            result[i["cprovinceid"]] = {}
            if i["honor"] not in result[i["cprovinceid"]]:
                result[i["cprovinceid"]][i["honor"]] = i["pop"]
            else:
                print("case1", i)
        else:
            if i["honor"] not in result[i["cprovinceid"]]:
                result[i["cprovinceid"]][i["honor"]] = i["pop"]
            else:
                print("case2", i)
    for k, v in result.items():
        print(k, v)
