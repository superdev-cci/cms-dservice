from django.db.models import Count

from commission.models import PvTransfer, WeekCommission, WeakStrongSummary
from member.models import Member


def link_statement():
    allInv = PvTransfer.objects.values('mcode').annotate(memberid=Count('mcode')).order_by('-memberid')
    pool = [i['mcode'] for i in allInv]
    member = {x.mcode: x.id for x in Member.objects.filter(mcode__in=pool)}
    for k, v in member.items():
        print('Update : {}'.format(k))
        PvTransfer.objects.filter(mcode=k).update(member_id=v)
    return


def week_commission_statement():
    allInv = WeekCommission.objects.values('mcode').annotate(memberid=Count('mcode')).order_by('-memberid')
    pool = [i['mcode'] for i in allInv]
    member = {x.mcode: x.id for x in Member.objects.filter(mcode__in=pool)}
    for k, v in member.items():
        print('Update : {}'.format(k))
        WeekCommission.objects.filter(mcode=k).update(member_id=v)
    return


def weak_strong_statement():
    allInv = WeakStrongSummary.objects.values('mcode').annotate(memberid=Count('mcode')).order_by('-memberid')
    pool = [i['mcode'] for i in allInv]
    member = {x.mcode: x.id for x in Member.objects.filter(mcode__in=pool)}
    for k, v in member.items():
        print('Update : {}'.format(k))
        WeakStrongSummary.objects.filter(mcode=k).update(member_id=v)
    return


def main():
    link_statement()
    week_commission_statement()
    weak_strong_statement()