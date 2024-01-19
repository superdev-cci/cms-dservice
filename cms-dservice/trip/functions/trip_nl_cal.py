from django.db.models import Sum

from commission.models import MonthCommission
from member.models import Member
from trip.models import TravelPointUseStatement, TripApplication
import pandas as pd


def check_report_nl(trip):
    t = trip
    rp = TravelPointUseStatement.objects.filter(trip=trip) \
        .values('member__mcode', 'member__name_t') \
        .annotate(total_gold=Sum('gold_coin'),
                  total_silver=Sum('silver_coin')) \
        .filter(total_silver__gte=100) \
        .order_by('member')

    data = {}

    for x in rp:
        m = Member.objects.get(mcode=x.get('member__mcode'))
        matching_count = MonthCommission.objects.filter(fdate__range=(trip.start, trip.end),
                                                        mcode=m.code, dmbonus__gte=0)
        gold_mod = int(x['total_gold'] / t.required_gold)
        silver_mod = int(x['total_silver'] / t.required_silver)

        data[x['member__mcode']] = {
            "name": x['member__name_t'],
            "matching_count": matching_count.count(),
            "total_gold": x['total_gold'],
            "total_silver": x['total_silver'],
            "gold_mod": gold_mod,
            "silver_mod": silver_mod,
        }

    df = pd.DataFrame.from_dict(data, orient="index")
    sorted_row = df.sort_index(axis=0)
    # sorted_row.to_excel("./trip_pt_2021.xlsx", na_rep=0, encoding="utf-8")
    return sorted_row
