from django.db.models import Sum
from member.models import Member
from trip.models import TravelPointUseStatement, TripApplication
import pandas as pd


def check_report_pt(trip):
    t = trip
    rp = TravelPointUseStatement.objects.filter(trip=t) \
        .values('member__mcode', 'member__name_t') \
        .annotate(total_gold=Sum('gold_coin'),
                  total_silver=Sum('silver_coin')) \
        .filter(total_gold__gte=20, total_silver__gte=30) \
        .order_by('member')

    data = {}

    for x in rp:
        m = Member.objects.get(mcode=x.get('member__mcode'))
        sp = Member.objects.filter(sp_code=m.mcode, level='VIP', distributor_date__range=['2020-12-01', '2021-02-28'])
        ta = TripApplication.objects.filter(member=m, trip__trip_type='OS')

        left = 0
        right = 0
        cmeta = m.child_tree_meta
        new_member = "YES"

        for y in sp:
            if y.line_lft >= cmeta['R']['lft'] and y.line_rgt <= cmeta['R']['rgt']:
                right += 1
            elif y.line_lft >= cmeta['L']['lft'] and y.line_rgt <= cmeta['L']['rgt']:
                left += 1
        if ta.count() > 0:
            new_member = "NO"

        discount = True if new_member == "YES" else False

        if discount:
            gold_mod = int(x['total_gold'] / (t.required_gold - 20))
            silver_mod = int(x['total_silver'] / (t.required_silver - 10))
        else:
            gold_mod = int(x['total_gold'] / t.required_gold)
            silver_mod = int(x['total_silver'] / t.required_silver)

        data[x['member__mcode']] = {
            "name": x['member__name_t'],
            "new_member": new_member,
            "total_gold": x['total_gold'],
            "total_silver": x['total_silver'],
            "gold_mod": gold_mod,
            "silver_mod": silver_mod,
            "sponsor_right": right,
            "sponsor_left": left,
        }

    df = pd.DataFrame.from_dict(data, orient="index")
    sorted_row = df.sort_index(axis=0)
    # sorted_row.to_excel("./trip_pt_2021.xlsx", na_rep=0, encoding="utf-8")
    return sorted_row
