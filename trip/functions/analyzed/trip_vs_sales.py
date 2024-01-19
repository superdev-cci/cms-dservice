from trip.models import TripApplication
from trip.models import Trip


def main(code):
    trip = Trip.objects.get(code=code)
    total_sales_value = 0
    seat = 0
    count = 0
    for x in TripApplication.objects.filter(trip=trip).select_related('member'):
        print('{} : {}'.format(x.member.code, x.balance_use))
        sales_value = (x.balance_use / 0.7) * 11
        print('Make sales_value -> {:,.2f}'.format(sales_value))
        total_sales_value += sales_value
        seat += x.seat
        count += 1

    print('Result Total Duration {} days'.format(trip.duration))
    print('Total Sales volume -> {:,.2f}'.format(total_sales_value))
    print('Average per day -> {:,.2f}'.format(total_sales_value / trip.duration))
    print('Total seat {}'.format(seat))
    print('Total Member {}'.format(count))
