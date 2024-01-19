from commission.models import PvTransfer, MonthQualified
from member.models import Member


def update_code(start, end):
    statement = PvTransfer.objects.filter(sadate__range=(start, end), sa_type='AM', cancel=0)
    count = 1
    for x in statement:
        print(x, count)
        count += 1
        qualify = MonthQualified.objects.filter(mcode=x.mcode, month_pv='201902')
        if len(qualify) == 1:
            print(x.mcode, 'is exit', len(qualify))
        elif len(qualify) == 2:
            print(x.mcode, 'is dobule', len(qualify))
        else:
            print(x.mcode, 'is create')
    return


def verify(start, end):
    qualify = MonthQualified.objects.filter(month_pv='201902')
    statement = PvTransfer.objects.filter(sadate__range=(start, end), sa_type='AM', cancel=0)
    q_member = [x.mcode for x in qualify]
    s_member = [x.mcode for x in statement]
    result = list(set(q_member) - set(s_member))
    print(result)
