import datetime
from django.db import models
from dateutil import relativedelta
from core.utility.month_dict import th_months
from core.utility import dict_transfrom


class TripApplication(models.Model):
    member = models.ForeignKey('member.Member', related_name='trip_enter', blank=True, on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', related_name='attendee', blank=True, on_delete=models.CASCADE)
    register_date = models.DateField(auto_now_add=True)
    confirm_count = models.IntegerField(default=0)
    balance_use = models.IntegerField(default=0)
    seat = models.IntegerField(default=0)
    previous_use = models.IntegerField(default=0)

    class Meta:
        ordering = ('-trip__start',)

    def __str__(self):
        return '{}:{} : {}/{}'.format(self.trip.code, self.member.mcode, self.balance_use, self.seat)


class Trip(models.Model):
    TRIP_TYPE_CHOICE = (
        ('IN', 'InBound'),
        ('OS', 'Oversea'),
    )

    code = models.CharField(max_length=8, blank=True)
    name = models.CharField(max_length=128)
    start = models.DateField()
    end = models.DateField()
    register_period = models.DateField()
    balance = models.IntegerField(default=0, blank=True)
    month_qualified = models.IntegerField(default=0, blank=True)
    condition = models.TextField(blank=True)
    max_seat = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    trip_type = models.CharField(max_length=2, choices=TRIP_TYPE_CHOICE, blank=True, null=True)
    balance_discount = models.IntegerField(default=0)
    # sponsor_discount = models.IntegerField(default=0)
    # sponsor_require = models.IntegerField(default=0)
    required_gold = models.IntegerField(default=0)
    required_silver = models.IntegerField(default=0)
    minimum_matching = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Travel Event'

    def __str__(self):
        return '{} : {}'.format(self.code, self.name)

    @property
    def duration(self):
        return (self.end - self.start).days

    @property
    def total_month(self):
        r = relativedelta.relativedelta(self.end, self.start)
        return r.months + (12 * r.years)

    @property
    def remaining_days(self):
        current_date = datetime.date.today()
        remaining_day = (self.end - current_date).days
        return remaining_day

    @property
    def on_going_days(self):
        current_date = datetime.date.today()
        on_going = (current_date - self.start).days
        return on_going

    def process(self, balance, month_qualified, member, balance_discount=0):
        result = {}
        right = 0
        condition = {}

        use_balance = self.balance - balance_discount
        # Add on new function
        if use_balance < 0:
            use_balance = 0

        out_bound_trip = TripApplication.objects.filter(member=member, trip__trip_type='OS')
        if len(out_bound_trip) == 0:
            use_balance = use_balance - self.balance_discount

        if use_balance == 0:
            right = 1
        else:
            right = balance // use_balance

        max_balance = self.max_seat * use_balance
        if right == 0:
            current_process = balance
            to_target = use_balance - balance
        else:
            current_process = right * use_balance
            if current_process >= max_balance:
                current_process = max_balance
                right = self.max_seat
                to_target = 0
            else:
                to_target = int(use_balance - (balance % use_balance))
                current_process = int(balance % use_balance)

        right_count = 0
        right_process = []
        remaining = int(balance)
        for i in range(0, self.max_seat):
            if remaining >= use_balance:
                remaining -= use_balance
                right_count += 1
                right_process.append({
                    'current': '{:,}/{:,}'.format(use_balance, use_balance),
                    'percent': 100,
                    'use_balance': use_balance
                })
                if right_count >= self.max_seat:
                    break
            else:
                right_process.append({
                    'current': '{:,}/{:,}'.format(remaining, use_balance),
                    'percent': int(remaining / use_balance * 100),
                    'use_balance': use_balance
                })
                remaining = 0
                break

        # Use balance must grater than 0
        if use_balance != 0:
            percent = int(current_process / use_balance * 100) % 100
        else:
            percent = 100

        if to_target == 0:
            percent = 100

        condition['balance'] = {
            'text': 'รายได้ทีมอ่อน {:,} บาท'.format(use_balance),
            'current': '{:,}/{:,}'.format(int(balance), use_balance),
            'percent': percent,
            'pass': True if right > 0 else False,
            'target': '{:,}'.format(to_target)
        }

        # This process will discontinue
        if self.month_qualified > 0:
            diff = relativedelta.relativedelta(self.end, self.start)
            months = {}
            current_month = self.start
            for x in range(0, diff.months + 1):
                months[(current_month.strftime('%b'))] = '-'
                current_month = current_month.replace(month=(current_month.month + 1) % 12)
            qualified_count = month_qualified.count()
            for x in month_qualified:
                months[x.sdate.strftime('%b')] = th_months[x.sdate.strftime('%b')]
            # current_process = month_qualified if month_qualified > self.month_qualified else month_qualified
            percent = int(qualified_count / self.month_qualified * 100)
            condition['qualified'] = {
                'text': 'รักษายอด {} เดือน'.format(self.month_qualified),
                'current': '{:,}/{:,}'.format(qualified_count, self.month_qualified),
                'percent': percent,
                'pass': True if qualified_count >= self.month_qualified else False,
                'detail': [v for k, v in months.items()]
            }

        qualified = True
        for x in condition.values():
            if x['pass'] is False:
                qualified = False

        result['right'] = right
        if qualified is False:
            result['right'] = 0

        result['condition'] = condition
        result['right'] = {
            'right': int(right),
            'process': right_process,
            'current': '{:,}/{:,}'.format(right, self.max_seat),
            'percent': int(right / self.max_seat * 100),
        }

        return result, remaining

    def get_time_remaining(self, current):
        on_going = (current - self.start).days
        remaining_day = (self.end - current).days
        return {
            'current': '{} - {}'.format(self.start.strftime('%d-%m-%Y'), self.end.strftime('%d-%m-%Y')),
            'percent': int(on_going / self.duration * 100),
            'remaining': remaining_day
        }
