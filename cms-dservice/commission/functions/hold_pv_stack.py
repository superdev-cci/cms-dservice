from django.db.models import Sum
from datetime import date, timedelta
from commission.models import HoldPvStack
from commission.serializers import HoldPvStackSerializer
from member.models import Member


class HoldExpirePvStack(object):

    def __init__(self, member):
        if isinstance(member, Member):
            self.member = member
        else:
            self.member = Member.objects.get(mcode=member)
        self.stack_queryset = self.member.holdpvstack_set.all()

    @property
    def remaining_pv(self):
        return self.stack_queryset.filter(remaining__gt=0).aggregate(Sum("remaining"))["remaining__sum"]

    def add_pv(self, idate, pv):
        obj, created = HoldPvStack.objects.get_or_create(
            member=self.member,
            stamp_date=idate,
            defaults={
                'member': self.member,
                'stamp_date': idate,
                'pv': pv,
                'remaining': pv,
            }
        )
        if not created:
            obj.pv += pv
            obj.remaining += pv
            obj.save()

    def cancel_pv(self, pvcancel, idate=None):
        try:
            target = self.stack_queryset.get(stamp_date=idate)
        except:
            target = self.stack_queryset.filter(remaining__gt=0).order_by("-stamp_date")[0]

        if target.remaining >= pvcancel:
            target.remaining -= pvcancel
            target.pv -= pvcancel
            if target.pv <= 0:
                target.delete()
            else:
                target.save()
        else:
            over_cancel = pvcancel - target.remaining
            target.pv -= target.remaining
            target.remaining = 0
            if target.pv <= 0:
                target.delete()
            else:
                target.save()
            self.cancel_pv(over_cancel)
        return True

    def use_pv(self, pvuse):
        available_pv = self.stack_queryset.filter(remaining__gt=0).order_by("stamp_date")
        if pvuse <= available_pv[0].remaining:
            available_pv[0].remaining -= pvuse
            available_pv[0].save()
        else:
            overuse = pvuse - available_pv[0].remaining
            available_pv[0].remaining = 0
            available_pv[0].save()
            self.use_pv(overuse)

    def revert_pv(self, pvrevert, anotherstack, idate=None):
        # revert self to another
        durationDict = {'MB': 30, 'FR': 60, 'AG': 90}
        if self.remaining_pv < pvrevert:
            return "Not enough points to revert"
        else:
            if idate:
                self.cancel_pv(pvrevert, idate)
            else:
                idate = date.today()
                self.cancel_pv(pvrevert, idate)
            expire_date = date.today() - timedelta(durationDict[anotherstack.member.member_type])
            received = anotherstack.stack_queryset.filter(stamp_date__gte=expire_date).order_by("stamp_date")
            if received[0].stamp_date >= expire_date + timedelta(7):
                received[0].remaining += pvrevert
                received[0].save()
            else:
                trg = received.filter(stamp_date__lte=(expire_date + timedelta(7)))[-1]
                trg.remaining += pvrevert
                trg.save()

    def display_available_pv(self):
        available_pv = self.stack_queryset.filter(remaining__gt=0).order_by("stamp_date")
        # return HoldPvStackSerializer(available_pv, many=True).data
        return available_pv
