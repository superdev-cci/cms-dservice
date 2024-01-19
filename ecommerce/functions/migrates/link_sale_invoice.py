from django.db.models import Count
from ecommerce.models import SaleInvoice
from member.models import Member


def main():
    allInv = SaleInvoice.objects.filter(member__isnull=True)
    pool = [i.mcode for i in allInv]
    member = {x.mcode: x.id for x in Member.objects.filter(mcode__in=pool)}
    for k, v in member.items():
        print('Update : {}'.format(k))
        SaleInvoice.objects.filter(member__isnull=True, mcode=k).update(member_id=v)
