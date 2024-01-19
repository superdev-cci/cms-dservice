from django.test import TestCase
from member.report import MemberWithHonorSponsorDepth


# Create your tests here.
from member.report.analyst.excel_child_report import ExcelChildActivityAnalyst


def create_sponsor_depth():
    for x in ('CE', 'DE', 'EE', 'SE', 'PE', 'SI', 'GL'):
        print('Process : {}'.format(x))
        x = MemberWithHonorSponsorDepth(honor=x)
        x.process_data()
        x.save_file()

def generate_report_relax():
    members = [
        # 'TH1200000',
        # 'TH3085327',
        # 'TH5423583',
        # 'TH8881115',
        # 'TH9895961',
        # 'TH1855599',
        # 'TH3393675',
        # 'TH2500151',
        # 'TH6071264',
        # 'TH3080139',
        # 'TH1792329',
        # 'TH6368103',
        # 'TH5124835',
        # 'TH7161560',
        # 'TH3398461',
        # 'TH3865009',
        # 'TH6599889',
        # 'TH8401480',
        # 'TH8000001',
        # 'TH9656584',
        # 'TH4356994',
        # 'TH4926452',
        # 'TH5445861',
        # 'TH9921899',
        # 'TH3114372',
        # 'TH2222299',
        # 'TH0016699',
        # 'TH9903699',
        # 'TH9243256',
        # 'TH1809387',
        # 'TH4036421',
        # 'TH9555899',
        # 'TH4982222',
        # 'TH9913999',
        # 'TH1682895',
        # 'TH8745294',
        # 'TH9999979',
        # 'TH9845154',
        # 'TH7599929',
        # 'TH0236641',
        # 'TH1687898',
        # 'TH2222290',
        # 'TH8895379',
        # 'TH9556810',
        # 'TH3725891',
        # 'TH6678999',
        # 'TH9921699',
        # 'TH1682894',
        # 'TH3910532',
        # 'TH3266456',
        # 'TH6666772',
        # 'TH1259899',
        # 'TH9329621',
        # 'TH7446062',
        # 'TH2040498',
        # 'TH9776622',
        # 'TH4563981',
        # 'TH7354399',
        # 'TH1168477',
        # 'TH9199989',
        # 'TH4275512',
        # 'TH9090989',
        # 'TH2667348',
        # 'TH2057379',
        # 'TH4234203',
        # 'TH1981808',
        # 'TH6118604',
        # 'TH5816960',
        # 'TH2222463',
        # 'TH8116059',
        # 'TH4703014',
        # 'TH2222263',
        # 'TH7716263',
        # 'TH6540775',
        # 'TH6344372',
        # 'TH7896456',
        # 'TH3296789'
    ]
    start_date = '2018-01-01'
    end_date = '2018-12-31'
    for x in members:
        report = ExcelChildActivityAnalyst(start=start_date, end=end_date, mcode=x)
        report.process_data()
        report.save_file()


# import pandas as pd
# from commission.report.summary.summary_week_commission import SummaryWeekCommission
# report = SummaryWeekCommission(start="2020-01-01", end="2020-02-29", get_type="monthly")
# pool_data = report.direct_data
# df = pd.DataFrame.from_dict(pool_data, orient="index")
# df.fillna(0)
# df.to_excel("/home/jew/Desktop/test_to_excel.xlsx", header=True, encoding="utf-8", na_rep=0)


# from member.models import Member
# from commission.models import HonorChangeLog
# from django.db.models import Count, Sum
# import pandas as pd
#
# new_distributor = Member.objects.filter(
#     distributor_date__gte="2019-09-01", status_terminate=0, status_suspend=0
# ).values("sp_code").annotate(count=Count("id")).values("sp_code", "sp_name", "count").order_by("-count")
#
# df = pd.DataFrame(new_distributor[0:20])
# df.to_excel("/home/jew/Desktop/member_sponsor_new_member.xlsx", header=True, encoding="utf-8")
#
# mhonor_list = HonorChangeLog.objects.filter(date_change__gte="2019-09-01").values_list("mcode", flat=True).distinct()
# new_honor = Member.objects.filter(
#     mcode__in=mhonor_list, status_terminate=0, status_suspend=0
# ).values("sp_code").annotate(count=Count("id")).values("sp_code", "sp_name", "count").order_by("-count")
#
# from ecommerce.models import SaleInvoice
# from django.db.models.functions import TruncMonth
# de_list = Member.objects.filter(status_terminate=0, status_suspend=0, honor="DE").values_list("mcode", flat=True)
# de_bill = SaleInvoice.objects.filter(
#     cancel=0, total__gt=10, mcode__in=de_list, sadate__gte="2019-09-01"
# ).annotate(time=TruncMonth("sadate")).values("mcode", "time").annotate(sum_total=Sum("total")).values(
#     "mcode", "time", "sum_total"
# ).order_by("mcode")
# result = {}
# for bill in de_bill:
#     if bill["mcode"] not in result:
#         result[bill["mcode"]] = {bill["time"]: float(bill["sum_total"])}
#     else:
#         result[bill["mcode"]][bill["time"]] = float(bill["sum_total"])


# import pandas as pd
# from commission.models import WeekCommission
# from django.db.models import Avg
#
# mlist = ["TH1000000","TH2282462","TH2644665","TH2222236","TH3910532","TH7249578","TH6600064",
#          "TH7699929","TH2465691","TH4152712","TH7463684","TH8599965","TH3907211","TH8633686",
#          "TH8401480","TH3585510","TH2160524","TH9796855","TH7599929","TH4741516","TH2222259",
#          "TH6269830","TH6926269","TH6539589","TH4311523","TH4744005","TH0704657","TH3085327",
#          "TH2456491","TH3282554","TH1200000","TH4586486","TH9287429","TH9329621","TH8398997",
#          "TH3114372","TH5500001","TH2445691","TH9986499","TH2163147","TH7495998","TH6443065",
#          "TH4153984","TH4456691","TH5029699","TH2569323","TH7720509","TH7078928","TH4995595",
#          "TH6294452","TH8933276","TH0202223","TH7254203","LA1727252","TH9921699","TH9886093",
#          "TH5656888","LA1692176","TH2992001","TH8180780","TH9913999","TH9499889","TH9299979",
#          "TH9903699","TH2458168","TH9999979","TH4000000","TH5573734","TH5433959","TH9929658",
#          "TH8935244","TH6245915","TH9555899","TH5316802","TH8507160"]
#
# wc = WeekCommission.objects.filter(rcode__gte=149, mcode__in=mlist).order_by("mcode")
# result = {}
# for i in wc:
#     if i.mcode not in result:
#         result[i.mcode] = {}
#         result[i.mcode][i.fdate] = float(i.ws_bonus)
#     else:
#         result[i.mcode][i.fdate] = float(i.ws_bonus)

# import pandas as pd
# from commission.models import WeekCommission
# from member.models import Member
# from django.db.models.functions import TruncMonth
# from django.db.models import Sum
#
# queryset = WeekCommission.objects.filter(rcode__gte=61, ws_bonus__gt=0)
# all_commission = queryset.annotate(time=TruncMonth("fdate"))\
#     .values("mcode", "time").annotate(sum_ws=Sum("ws_bonus")).values("mcode", "time", "sum_ws").order_by("time")
#
# all_member = Member.objects.filter(
#     mcode__in=queryset.values_list("mcode", flat=True).distinct(),
#     status_terminate=0,
#     status_suspend=0
# ).values("mcode", "name_t", "distributor_date")
#
# result = {}
# for com in all_commission:
#     if com["mcode"] not in result:
#         result[com["mcode"]] = {com["time"].strftime("%Y-%b"): float(com["sum_ws"])}
#     else:
#         result[com["mcode"]][com["time"].strftime("%Y-%b")] = float(com["sum_ws"])
#
#
# df = pd.DataFrame.from_dict(result, orient="index")
# sorted_col = df.sort_index(axis=1)
# sorted_row = sorted_col.sort_index(axis=0)
# sorted_row.to_excel("/home/jew/Desktop/2year_commission.xlsx", header=True, encoding="utf-8", na_rep=0)

