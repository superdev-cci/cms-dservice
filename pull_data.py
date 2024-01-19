from commission.models import WeekPayment, MonthPayment
from member.models import Member
from django.db.models import Sum


def main():
    startdate = '2019-01-01'
    enddate = '2019-12-31'
    result1 = WeekPayment.objects.filter(date_issue__range=('2018-12-22', enddate), paid_state=1).aggregate(
        sum_week_total=Sum('total'))
    result2 = MonthPayment.objects.filter(date_issue__range=('2018-12-31', enddate), paid_state=1).aggregate(
        sum_month_total=Sum('total'))
    result3 = WeekPayment.objects.filter(date_issue='2019-11-14', paid_state=0).aggregate(
        sum_week_total=Sum('total'))
    result4 = MonthPayment.objects.filter(date_issue='2019-10-31', paid_state=0).aggregate(
        sum_month_total=Sum('total'))
    print('{:,}'.format(result1['sum_week_total']), '{:,}'.format(result2['sum_month_total']))
    print('{:,}'.format(result1['sum_week_total'] + result2['sum_month_total']))
    print('{:,}'.format(result3['sum_week_total']), '{:,}'.format(result4['sum_month_total']))


def check_member_com():
    queryset = WeekPayment.objects.filter(week_round=152, cumulative_paid__range=(100000, 150000))
    for x in queryset:
        member_pay = WeekPayment.objects.filter(week_round=152, mcode=x.mcode).count()
        if member_pay <= 24:
            member = Member.objects.get(mcode=x.mcode)
            if member.distributor_date.month > 6 and member.distributor_date.year == 2019:
                print('{} {} -> {} // {}  -> {}'.format(x.mcode, x.name_t, x.cumulative_paid, member.distributor_date, member.sponsor_child.count()))
