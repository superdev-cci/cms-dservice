from member.models import Member, MemberGroup
from django.db.models import Q


def update_member_group():
    mfl = list(Member.objects.filter(Q(name_t__icontains='โมบาย') |
                                     Q(name_t__icontains='mobile')).values_list('id', flat=True))
    Member.objects.filter(mtype1=1, id__in=mfl).update(group=3)
    Member.objects.filter(mtype1=1).exclude(id__in=mfl).update(group=2)
    agtl = list(Member.objects.filter(mtype1=2, name_t__icontains='มัดจำ').values_list('id', flat=True))
    Member.objects.filter(mtype1=2, id__in=agtl).update(group=5)
    Member.objects.filter(mtype1=2).exclude(id__in=agtl).update(group=4)
    Member.objects.filter(mtype1=0).update(group=1)
