from dateutil.relativedelta import relativedelta
from django.db.models import Q

from commission.models import WeekCommission
from trip.models import Trip, TripApplication


class TripCalculatorMixin:

    def is_head(self, trip, ref_trip):
        if ref_trip.end < trip.end:
            return True
        return False

    def get_head_trip(self, ref_trip, trip):
        if ref_trip.end < trip.end:
            return trip, ref_trip
        return ref_trip, trip

    def calculate_consuming(self, trip, balance, member=None):
        if member is None:
            member = self.member
        consuming, flag = self.get_overlap_application(trip, member)
        total_consuming = balance['tail_use'] + consuming
        if flag is True:
            if balance['tail'] - total_consuming >= 0:
                remaining = balance['head']
            else:
                remaining = (balance['tail'] - total_consuming) + \
                            balance['head']
        else:
            if balance == 0:
                remaining = 0
            else:
                remaining = int(balance['head'])
        return remaining, consuming

    def solve_overlap_trip(self, trip, depth=0):
        overlap_trip = self.get_overlap_trip(trip)
        trip_balance = self.get_cumulative(trip.start, trip.end)
        balance = {
            'non_overlap': trip_balance,
            'overlap': 0,
            'total': trip_balance,
            'tail_use': 0,
            'tail': 0,
            'head': 0,
            'is_exist': False
        }

        if overlap_trip is not None:
            balance = self.determine_overlap_balance(trip, overlap_trip)
            if depth < 1 and overlap_trip.remaining_days < 0:
                previous_balance = self.solve_overlap_trip(overlap_trip, depth + 1)[0]
                remaining, consuming = self.calculate_consuming(overlap_trip, previous_balance)
                # Adjust remaining
                # if remaining != 0 and consuming != 0:
                self.adjust_balance(balance, remaining)

        # print(trip_balance, balance)
        return balance, overlap_trip

    def get_cumulative(self, start, end, member=None):
        if member is None:
            cumulative = WeekCommission.get_cumulative_ws(start, end, self.member.code)
        else:
            cumulative = WeekCommission.get_cumulative_ws(start, end, member)
        balance = cumulative['total_balance']
        if balance is None:
            balance = 0
        return float(balance)

    def get_inside_trip(self, trip):
        trips = Trip.objects.filter(end__range=(trip.start, trip.end), start__gt=trip.start).filter(
            ~Q(code=trip.code))
        return trips

    def get_overlap_trip(self, trip):
        overlap_trip = Trip.objects.filter(end__range=(trip.start, trip.end), start__lt=trip.start).filter(
            ~Q(code=trip.code))
        return overlap_trip

    def get_overlap_application(self, trip, member=None):
        if member is None:
            overlap_trip = TripApplication.objects.filter(trip__end__range=(trip.start, trip.end),
                                                          member=self.member).filter(~Q(trip__code=trip.code))
        else:
            overlap_trip = TripApplication.objects.filter(trip__end__range=(trip.start, trip.end),
                                                          member__mcode=member).filter(~Q(trip__code=trip.code))
        total_overlap_use = 0
        is_exist = False
        for x in overlap_trip:
            total_overlap_use += x.balance_use
            is_exist = True
        return total_overlap_use, is_exist

    def determine_overlap_balance(self, head, tail, member=None):
        last_day_last_month = head.start - relativedelta(days=1)
        start_tail_balance = self.get_cumulative(tail.start, last_day_last_month, member)
        end_tail_balance = self.get_cumulative(head.start, tail.end, member)
        tail_application_trip, is_exist = self.get_overlap_application(tail, member)
        head_balance = self.get_cumulative(head.start, head.end, member)

        balance = {
            'non_overlap': int(start_tail_balance),
            'overlap': int(end_tail_balance),
            'total': int(start_tail_balance + end_tail_balance),
            'tail_use': int(tail_application_trip),
            'tail': int(start_tail_balance),
            'head': int(head_balance),
            'is_exist': is_exist
        }

        return balance

    def determine_overlap_balance_by_date(self, head, tail, member=None):
        last_day_last_month = head['start'] - relativedelta(days=1)
        start_tail_balance = self.get_cumulative(tail['start'], last_day_last_month, member)
        end_tail_balance = self.get_cumulative(head['start'], tail['end'], member)
        # tail_application_trip, is_exist = self.get_overlap_application(tail, member)
        head_balance = self.get_cumulative(head['start'], head['end'], member)

        balance = {
            'non_overlap': start_tail_balance,
            'overlap': end_tail_balance,
            'total': start_tail_balance + end_tail_balance,
            'tail': start_tail_balance,
            'head': head_balance,
        }

        return balance

    def get_trip_balance(self, trip):
        balance = self.solve_overlap_trip(trip)
        balance_pool = balance[0]
        remaining, consuming = self.calculate_consuming(trip, balance_pool)

        balance_pool['remaining'] = remaining
        balance_pool['consuming'] = consuming
        return balance_pool

    # Pre define test only
    def solve_overlap_remaining(self, re_trip, trip, member):
        overlap_trip = self.get_overlap_trip(trip)
        trip_balance = self.get_cumulative(trip.start, trip.end, member)
        balance = {
            'non_overlap': trip_balance,
            'overlap': 0,
            'total': trip_balance,
            'tail_use': 0,
            'tail': 0,
            'head': 0,
            'is_exist': False
        }
        if overlap_trip is not None:
            previous_trip = overlap_trip.first()
            balance = self.determine_overlap_balance(trip, previous_trip, member)
            remaining, consuming = self.calculate_consuming(trip, balance, member)
            if remaining != balance['head']:
                balance['consume_from_previous'] = balance['head'] - remaining
            balance['remaining'] = remaining
            balance['consuming'] = consuming

        return balance

    def adjust_balance(self, balance, remaining):
        # Adjust remaining
        if remaining <= balance['total']:
            diff = balance['total'] - remaining
            balance['consume_from_previous'] = diff
            balance['total'] = balance['total'] - diff
            balance['tail'] = balance['tail'] - diff
            if balance['tail'] < 0:
                balance['head'] = balance['head'] + balance['tail']
                balance['tail'] = 0
            balance['tail_use'] = 0
        return balance

    def get_overlap_summary(self, member, select_trip, limit_date=None):
        trip_enroll = TripApplication.objects.filter(trip=select_trip, member=member)

        if len(trip_enroll):
            enroll_instance = trip_enroll.first()
            total_consume = enroll_instance.previous_use + enroll_instance.balance_use

            if limit_date is not None:
                tail_end_date = limit_date - relativedelta(days=1)
                trip_balance_tail = self.get_cumulative(select_trip.start, tail_end_date)

                if trip_balance_tail >= total_consume:
                    return False, 0

                consume = total_consume - trip_balance_tail
                return True, consume

        return False, 0

    def get_inside_summary(self, member, select_trip):
        total = 0
        for x in self.get_inside_trip(select_trip):
            instance = TripApplication.objects.filter(trip=x, member=member).first()
            if instance:
                total += instance.balance_use

        return total

    def get_trip_summary(self, member, select_trip):
        overlap_trip = self.get_overlap_trip(select_trip)
        trip_balance = self.get_cumulative(select_trip.start, select_trip.end)

        if overlap_trip is not None:
            is_consume, consume = self.get_overlap_summary(member, overlap_trip, select_trip.start)
            if is_consume:
                trip_balance -= consume
        else:
            consume = 0

        inside_use_balance = self.get_inside_summary(member, select_trip)
        trip_balance = trip_balance - inside_use_balance

        return trip_balance, consume + inside_use_balance, consume
