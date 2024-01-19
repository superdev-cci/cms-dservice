from django.db.models import Sum
from commission.models import WeakStrongCurrentRoundStack
from member.models import Member
from datetime import date


def get_round_date():
    cd = date.today()
    if 1 <= cd.day <= 7:
        return cd.replace(day=1)
    elif 8 <= cd.day <= 14:
        return cd.replace(day=8)
    elif 15 <= cd.day <= 21:
        return cd.replace(day=15)
    return cd.replace(day=22)


class StampPvRound(object):
    def __init__(self, mcode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.member = mcode
        self.queryset = WeakStrongCurrentRoundStack.objects.filter(upa_code=self.member, fdate__gte=get_round_date())
        return

    @property
    def all_pv(self):
        qs = self.queryset.values('lr').annotate(total=Sum('pv')).order_by('lr')
        tmp = {'left': 0, 'right': 0}
        for i in qs:
            if i['lr'] == 1:
                tmp['left'] = i['total']
            else:
                tmp['right'] = i['total']
        return tmp

    @property
    def left_detail(self):
        return self.queryset.filter(lr=1)

    @property
    def right_detail(self):
        return self.queryset.filter(lr=2)

    @staticmethod
    def create_stamp_pv(bill_number, mcode, pv):
        member = Member.objects.get(mcode=mcode)
        stack = []
        trg = member
        count = 0
        while trg.upa_code != '':
            count += 1
            stack.append(WeakStrongCurrentRoundStack(
                rcode=0,
                sano=bill_number,
                mcode=mcode,
                member=member,
                upa_code=trg.upa_code,
                lr=trg.lr,
                level=count,
                pv=pv,
                bv=0,
                fdate=date.today(),
                tdate=date.today(),
            ))
            trg = Member.objects.get(mcode=trg.upa_code)
        return WeakStrongCurrentRoundStack.objects.bulk_create(stack)

    @staticmethod
    def delete_stamp_pv(bill_number):
        WeakStrongCurrentRoundStack.objects.filter(sano=bill_number).delete()
        return
