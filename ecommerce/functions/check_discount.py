from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from commission.report.holdpv_activity import PvActivityReport
from member.models import Member
from ecommerce.models import SaleInvoice
from django.db.models import Sum


def CheckDiscountQualified(mem_code):
    dt = date.today() - relativedelta(months=1)
    start, end = PvActivityReport.get_month_range(dt)
    member = Member.objects.select_related('group').get(mcode=mem_code)
    tmp = PvActivityReport(start=start, end=end, get_type='monthly', mem_code=mem_code).result

    # AG Child check (Disable this function)
    child_sale = SaleInvoice.objects.filter(sadate__range=(start, end), cancel=0, sa_type='H',
                                            member__agency_ref=member, inv_code='BKK02') \
        .aggregate(total=Sum('tot_pv'))

    child_sale_total = child_sale['total']

    if child_sale_total is None:
        child_sale_total = 0
    else:
        child_sale_total = float(child_sale_total)

    result = {
        'total': child_sale_total,
        'qualify': False,
        'group': member.group.code
    }

    for k, v in tmp.items():
        total = v['in'] + v['transfer'] + child_sale_total

        result = {
            'total': total,
            'qualify': total >= member.group.status_qualified,
            'group': member.group.code
        }
        if member.group.code == 'MB':
            result['qualify'] = False
    return result
