from datetime import datetime
from django.db.models import Q, Count, Sum
from member.models import Member
from ..models import Trip

level_discount = {
    "VIP": 2000,
    "PRO": 800,
    "DIS": 400
}


def trip_sponsor_discount(trip_code="2020HHN"):
    trip = Trip.objects.get(code=trip_code)
    queryset = Member.objects.filter(Q(status_terminate=0), Q(distributor_date__range=(trip.start, trip.end)))
    data_list = queryset.annotate(count=Count('mcode')).values('sp_code', 'level', 'count').order_by('sp_code')
    pool = {}
    for i in data_list:
        if i['sp_code'] not in pool:
            pool[i['sp_code']] = i['count'] * level_discount.get(i['level'], 0)
        else:
            pool[i['sp_code']] += i['count'] * level_discount.get(i['level'], 0)
    return pool
