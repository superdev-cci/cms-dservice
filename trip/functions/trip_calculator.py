import datetime
from django.db.models import Q
from commission.models import MonthQualified, MonthCommission
from core.mixin.trip_calculator_mixin import TripCalculatorMixin
from member.models import Member
from event.models import Attendee
from trip.models import TripApplication, Trip, TravelPointUseStatement
from trip.serializers import TripSerializer

from dateutil.relativedelta import relativedelta


class TripCalculator(TripCalculatorMixin):

    def __init__(self, member, *args, **kwargs):
        self.member = Member.objects.get(mcode=member)
        self.context = kwargs
        self.trips = []
        return

    def calculate_trip_result(self, current_date, trip, trip_pool, priority='MAIN', consuming=0, previous_remaining=0):
        # Collect total balance for select trip
        balance, balance_use, consume_with_overlap = self.get_trip_summary(self.member, trip)
        qualified = MonthQualified.objects.filter(mdate__range=(trip.start, trip.end),
                                                  mcode=self.member.code)

        # Determine total remaining balance
        if priority == 'SEC':
            # Main trip had been calculated
            if previous_remaining != 0 and consuming == 0:
                if previous_remaining > balance:
                    total = balance
                else:
                    total = previous_remaining
            elif previous_remaining == 0 and consuming == 0:
                total = balance
            elif previous_remaining == 0 and consuming != 0:
                total = previous_remaining
            else:
                # Dummy result
                total = 0
        else:
            # Secondary trip had been calculated
            total = int(balance - consuming)

        if total < 0:
            total = 0

        if trip.code == '2020HHN':
            sponsor, discount = self.calculate_huahin_sponsor(trip)
            result, remaining_all = trip.process(int(total), qualified, self.member, discount)
            trip_serializer = TripSerializer(trip)
            event_count = self.get_attendee_event(trip)
            result = self.recalcuate_huahin(result, sponsor, discount, event_count)
            trip_pool.append({
                **trip_serializer.data,
                'priority': priority,
                'cumulative': total,
                'result': result,
                'date': trip.get_time_remaining(current_date),
                'extend': '*นักธุรกิจยต้องยันตัวตนโดยแสดงบัตร ปชช. และสแกน QR Code'
            })
        else:
            result, remaining_all = trip.process(int(total), qualified, self.member)
            trip_serializer = TripSerializer(trip)
            trip_pool.append({
                **trip_serializer.data,
                'priority': priority,
                'cumulative': total,
                'result': result,
                'date': trip.get_time_remaining(current_date)
            })

        return trip_pool, total - remaining_all, balance

    def find_active_trip(self, select_date=None):
        sel_trip = self.context['request'].query_params.get('trip', 'SEC')
        trip_sel = self.context['request'].query_params.get('check', None)
        trip_pool = []

        if select_date is not None:
            current_date = select_date
        else:
            current_date = datetime.date.today()

        # Determine current trip on process
        trip_query = Trip.objects.filter(start__lte=current_date, end__gte=current_date, active=True)
        self.trips = [x for x in trip_query]
        self.trips = sorted(self.trips, key=lambda x: x.duration, reverse=True)
        if len(self.trips):
            main_trip = self.trips[0]
            if len(self.trips) > 1:
                secondary_trip = self.trips[1]
                if sel_trip == 'MAIN':
                    trip_pool, consuming, main_balance_result = self.calculate_trip_result(current_date, main_trip,
                                                                                           trip_pool, 'MAIN')
                    if main_balance_result > consuming:
                        # Calculate with remaining result but not over on secondary trip periods
                        trip_pool, consuming, sec_balance_result = self.calculate_trip_result(current_date,
                                                                                              secondary_trip,
                                                                                              trip_pool, 'SEC',
                                                                                              0,
                                                                                              main_balance_result - consuming)
                    else:
                        # Force secondary trip to 0 balance
                        trip_pool, consuming, sec_balance_result = self.calculate_trip_result(current_date,
                                                                                              secondary_trip,
                                                                                              trip_pool, 'SEC',
                                                                                              consuming,
                                                                                              0)
                else:
                    trip_pool, consuming, sec_balance_result = self.calculate_trip_result(current_date, secondary_trip,
                                                                                          trip_pool, 'SEC')
                    # Calculate main trip with secondary consuming
                    trip_pool, consuming, sec_balance_result = self.calculate_trip_result(current_date, main_trip,
                                                                                          trip_pool, 'MAIN', consuming)

            else:
                self.calculate_trip_result(current_date, main_trip, trip_pool)

            return sorted(trip_pool, key=lambda x: x['balance'], reverse=True)

    def get_overlap_trip(self, trip):
        queryset = super().get_overlap_trip(trip)
        return queryset.first()

    def get_attendee_event(self, trip):
        event_attendant = Attendee.objects.filter(event__date__range=(trip.start, trip.end),
                                                  members__mcode=self.member.code)
        return event_attendant.count()

    def get_sponsor_discount(self, trip):
        member_query = Member.objects.filter(sp_code=self.member.code,
                                             distributor_date__range=(trip.start, trip.end),
                                             status_terminate=0)

        sponsor_pool = [x.code for x in member_query]
        event_attendant = Attendee.objects.filter(event__date__range=(trip.start, trip.end),
                                                  members__mcode__in=sponsor_pool) \
            .select_related('members') \
            .values_list('members__mcode', flat=True) \
            .distinct()
        return len(event_attendant)

    def calculate_huahin_sponsor(self, trip):

        level_score = {
            "VIP": 2000,
            "PRO": 800,
            "DIS": 400
        }
        total = 0
        new_sponsor = Member.objects.filter(sp_code=self.member.code,
                                            distributor_date__range=(trip.start, trip.end),
                                            status_terminate=0)
        for x in new_sponsor:
            total += level_score[x.level]

        if total < 6000:
            discount = 0
        elif 6000 <= total < 8000:
            discount = 2000
        elif 8000 <= total < 10000:
            discount = 4000
        else:
            discount = 5000

        return total, discount

    def recalcuate_huahin(self, result, sponsor, discount, event_count):
        percent = 100

        previous_app = TripApplication.objects.filter(member=self.member)
        pass_factor = 4000
        if len(previous_app) == 0:
            pass_factor = 2000

        if sponsor < 10000:
            percent = (sponsor / pass_factor) * 100

        sponsor_condition = {
            'text': 'แนะนำตรงสมาชิกใหม่รวม {:,} PV'.format(pass_factor),
            'current': '{:,}/{:,} PV'.format(int(sponsor), pass_factor),
            'percent': percent if percent <= 100 else 100,
            'pass': True if sponsor >= pass_factor else False,
            'target': '{:,}'.format(0 if discount >= 5000 else 5000 - discount)
        }

        event_condition = {
            'text': 'ยืนยันตัวตนในงานบริษัท',
            'pass': True if event_count > 0 else False,
        }

        result['condition']['sponsor'] = sponsor_condition
        result['condition']['event'] = event_condition
        qualified = True
        for x in result['condition'].values():
            if x['pass'] is False:
                qualified = False

        if qualified is False:
            adjust_right = {
                **result['right'],
                'right': 0,
                'current': '{:,}/{:,}'.format(0, 1),
                'percent': 0,
            }
            result['right'] = adjust_right
        return result

    def find_all_trip(self, select_date=None):
        trip_pool = []

        if select_date is not None:
            current_date = select_date
        else:
            current_date = datetime.date.today()
        trip_query = Trip.objects.filter(start__lte=current_date, register_period__gte=current_date, active=True)
        self.trips = [x for x in trip_query]
        self.trips = sorted(self.trips, key=lambda x: x.duration, reverse=True)

        for x in self.trips:
            trip_pool.append(self.get_trip_description(x))

        return trip_pool

    def get_trip_description(self, trip):
        meta = TripSerializer(trip).data
        total_coin = TravelPointUseStatement.get_total_coin(trip, self.member)
        if trip.code == 'PT2021':
            oversea_trip = TripApplication.objects.filter(trip__trip_type='OS', member=self.member).count()
            if oversea_trip == 0:
                meta['required_gold'] = trip.required_gold - 20
                meta['required_silver'] = trip.required_silver - 10

        gold_coin = total_coin.get('total_gold', 0)
        silver_coin = total_coin.get('total_silver', 0)
        meta['current'] = {
            'gold': gold_coin if gold_coin is not None else 0,
            'silver': silver_coin if silver_coin is not None else 0
        }

        matching_count = MonthCommission.objects.filter(fdate__range=(trip.start, trip.end),
                                                        mcode=self.member.code, dmbonus__gte=0)
        meta['current']['matchingCount'] = matching_count.count()
        meta['pass_count'] = self.calculate_right(trip, meta['current'])

        if trip.code == 'PT2021':
            cmeta = self.member.child_tree_meta
            sp = Member.objects.filter(sp_code=self.member.mcode, level='VIP',
                                       distributor_date__range=['2020-12-01', '2021-02-28'])
            left = 0
            right = 0
            for y in sp:
                if y.line_lft >= cmeta['R']['lft'] and y.line_rgt <= cmeta['R']['rgt']:
                    right += 1
                elif y.line_lft >= cmeta['L']['lft'] and y.line_rgt <= cmeta['L']['rgt']:
                    left += 1

            sponsor_condition = min([right, left])
            if meta['pass_count'] >= sponsor_condition:
                meta['pass_count'] = sponsor_condition if not sponsor_condition >= trip.max_seat else trip.max_seat
            meta['sponsor'] = {
                "left": left,
                "right": right,
                "max": 2
            }

        return meta

    def calculate_right(self, trip, data):
        gold_coin = int(data['gold'])
        silver_coin = int(data['silver'])
        pass_count = 0
        required_gold = trip.required_gold
        required_silver = trip.required_silver

        if trip.code == 'PT2021':
            oversea_trip = TripApplication.objects.filter(trip__trip_type='OS', member=self.member).count()
            if oversea_trip == 0:
                required_gold = trip.required_gold - 20
                required_silver = trip.required_silver - 10

        for x in range(trip.max_seat):
            gold_count = int(gold_coin / required_gold)
            silver_count = int(silver_coin / required_silver)

            if gold_coin != 0:
                if gold_count > 0 and silver_count > 0:
                    gold_coin -= required_gold
                    silver_coin -= required_silver
                    pass_count += 1
                else:
                    silver_count = int(silver_coin / (required_silver * 2))
                    if silver_count > 0:
                        pass_count += 1
                        silver_coin -= required_silver * 2
            else:
                silver_count = int(silver_coin / (required_silver * 2))
                if silver_count > 0:
                    pass_count += 1
                    silver_coin -= required_silver * 2
        return pass_count
