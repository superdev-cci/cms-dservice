from django.db.models import Q

from member.models import Member
from system_log.models import PositionChangeLog


def update_distributor_date():
    apply_count = 0
    member_skip = {x.mcode: x for x in Member.objects.filter(distributor_date=None)}
    target_log = PositionChangeLog.objects.filter(pos_before="MB").values_list("mcode", "date_change")
    for l in target_log:
        if l[0] in member_skip:
            continue
        try:
            m = Member.objects.get(mcode=l[0])
            if not m.distributor_date:
                m.distributor_date = l[1]
                m.save()
                apply_count += 1
        except:
            pass

    for member in Member.objects.filter(~Q(level='MB'), distributor_date=None):
        last_change = PositionChangeLog.objects.filter(mcode=member.code).order_by('date_change').first()
        if last_change:
            member.distributor_date = last_change.date_change
        else:
            member.distributor_date = member.mdate
        member.save()
        apply_count += 1

    print('Finish apply record : {}'.format(apply_count))
