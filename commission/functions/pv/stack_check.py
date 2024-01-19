from django.db.models import Sum, Q, F
from commission.models import HoldPvStack


def check_stack_pv():
    message = ""
    all_stack = HoldPvStack.objects.exclude(remaining=0).values('member__mcode', 'member__name_t', 'member__hpv') \
        .annotate(stack=Sum('remaining')).filter(~Q(stack=F('member__hpv'))).order_by('member__mcode')
    total = all_stack.count()
    if all_stack.count():
        message = "พบความผิดปกติในระบบคะแนน\n"
        message += "รายชื่อสมาชิก\n"
        for x in all_stack:
            message += '{} {} คะแนน {} : Stack {}\n'.format(x['member__mcode'], x['member__name_t'], x['member__hpv'],
                                                            x['stack'])

    return total, message
