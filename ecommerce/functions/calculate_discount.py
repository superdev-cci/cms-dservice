import datetime, decimal
from member.models import Member
from commission.models import PvTransfer
from ecommerce.models import SaleInvoice, MemberDiscount
from django.db.models import Q, Avg, Count, Min, Sum


def calculateDiscountPV(month, year):
    agdict, mfdict, fsdict = {}, {}, {}
    asi = SaleInvoice.objects.filter(tot_pv__gte=1000, sadate__month=month, sadate__year=year)
    ag = asi.filter(tot_pv__gte=3000)
    for i in ag.values('mcode').annotate(tot_pv=Sum('tot_pv')):
        if i['mcode'] in agdict:
            agdict[i['mcode']] += i['tot_pv']
        else:
            agdict[i['mcode']] = i['tot_pv']

    apt = PvTransfer.objects.filter(tot_pv__gte=1000, sadate__month=month, sadate__year=year)
    agpt = apt.filter(tot_pv__gte=3000)
    for i in agpt.values('mcode').annotate(tot_pv=Sum('tot_pv')):
        if i['mcode'] in agdict:
            agdict[i['mcode']] += i['tot_pv']
        else:
            agdict[i['mcode']] = i['tot_pv']

    asi2 = asi.exclude(tot_pv__gte=3000)
    apt2 = apt.exclude(tot_pv__gte=3000)
    mobml = Member.objects.filter(Q(name_t__icontains='โมบาย') | Q(name_t__icontains='mobile')).values_list('mcode',
                                                                                                            flat=True)
    mf = asi2.filter(mcode__in=mobml)
    for i in mf.values('mcode').annotate(tot_pv=Sum('tot_pv')):
        if i['mcode'] in mfdict:
            mfdict[i['mcode']] += i['tot_pv']
        else:
            mfdict[i['mcode']] = i['tot_pv']

    mfpt = apt2.filter(mcode__in=mobml)
    for i in mfpt.values('mcode').annotate(tot_pv=Sum('tot_pv')):
        if i['mcode'] in mfdict:
            mfdict[i['mcode']] += i['tot_pv']
        else:
            mfdict[i['mcode']] = i['tot_pv']

    fs = asi2.exclude(mcode__in=mobml)
    for i in fs.values('mcode').annotate(tot_pv=Sum('tot_pv')):
        if i['mcode'] in fsdict:
            fsdict[i['mcode']] += i['tot_pv']
        else:
            fsdict[i['mcode']] = i['tot_pv']

    fspt = apt2.exclude(mcode__in=mobml)
    for i in fspt.values('mcode').annotate(tot_pv=Sum('tot_pv')):
        if i['mcode'] in fsdict:
            fsdict[i['mcode']] += i['tot_pv']
        else:
            fsdict[i['mcode']] = i['tot_pv']

    for mcode in agdict:
        try:
            ob = MemberDiscount.objects.create(member=Member.objects.get(mcode=mcode),
                                               value=agdict[mcode] * decimal.Decimal(0.3))
            ob.save()
        except:
            print(mcode)

    for mcode in fsdict:
        try:
            ob = MemberDiscount.objects.create(member=Member.objects.get(mcode=mcode),
                                               value=fsdict[mcode] * decimal.Decimal(0.15))
            ob.save()
        except:
            print(mcode)

    for mcode in mfdict:
        try:
            ob = MemberDiscount.objects.create(member=Member.objects.get(mcode=mcode),
                                               value=mfdict[mcode] * decimal.Decimal(0.1))
            ob.save()
        except:
            print(mcode)
