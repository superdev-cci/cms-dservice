import datetime
from collections import OrderedDict

from django.db.models import Sum, Q
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1, BUILTIN_FORMATS
from commission.models import WeekCommission, MonthQualified
from core.mixin.trip_calculator_mixin import TripCalculatorMixin
from core.report.excel import ExcelTemplateReport
from core.utility import dict_transfrom
from member.models import Member
from trip.models import TripApplication, Trip
from ..functions.trip_calculator import TripCalculator
from ..functions.trip_sponsor_discount import trip_sponsor_discount


class TripEnrollReport(TripCalculatorMixin, ExcelTemplateReport):
    # template_file = './templates/report/trip/trip.xlsx'
    template_file = './templates/report/trip/trip2.xlsx'

    class Meta:
        title = 'Trip report'
        sheet_name = 'Trip'
        file_name = 'trip'
        head_file = 'Trap'
        head_start_col = 4
        head_start_row = 7
        content_start_col = 1
        content_start_row = 9

    def __init__(self, trip, *args, **kwargs):
        super(TripEnrollReport, self).__init__(*args, **kwargs)
        if isinstance(trip, Trip):
            self.trip = trip
        else:
            self.trip = Trip.objects.get(code=trip)
        self.discount_pv = self.cal_discount()

    def cal_discount(self):
        return trip_sponsor_discount(self.trip.code)

    def create_head(self):
        self.work_sheet['C3'] = 'Trip : {}'.format(self.trip.name)
        self.work_sheet['D4'] = datetime.date.today().strftime('%d/%b/%Y')
        return

    def build_row_meta(self, count, member_code, data, **kwargs):
        row = kwargs.get('row')
        row_meta = [
            ('no', {'data': count, 'alignment': self.style['align_center']}),
            ('mcode', {'data': member_code, 'alignment': self.style['align_center']}),
            ('person', {'data': data['name']}),
            ('level', {'data': data['level']}),
            ('balance', {
                'data': data['balance'],
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1,
                'alignment': self.style['align_right']
            }),
            ('right', {
                'data': data['right'],
                'alignment': self.style['align_center']
            }),
            ('use_other_trip', {
                'data': data['use_other_trip'],
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1,
                'alignment': self.style['align_center']
            }),
            ('use_overlap_trip', {
                'data': data['overlap_trip'],
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1,
                'alignment': self.style['align_center']
            }),
            ('status', {'data': data['status'], 'alignment': self.style['align_center']}),
            ('new', {'data': data['new_entry'], 'alignment': self.style['align_center']}),
            ('sponsor_pv', {
                'data': data.get('sponsor_pv', 0),
                'number_format': BUILTIN_FORMATS[3],
                'alignment': self.style['align_right']
            }),
            ('use_balance', {
                'data': data.get('use_balance', 0),
                'number_format': BUILTIN_FORMATS[3],
                'alignment': self.style['align_right']
            }),
            ('right_dc', {
                'data': data.get('right_dc', 0),
                'alignment': self.style['align_center']
            }),
        ]
        return OrderedDict(row_meta)

    def get_overlap_enroll(self, trips):
        query = TripApplication.objects.filter(trip__in=trips).values('member__mcode').annotate(
            total=Sum('balance_use')).order_by('total')
        return {x['member__mcode']: x['total'] for x in query}

    def calculate(self):
        if self.trip.code == "2020HHN":
            trip_cumulative = WeekCommission.get_cumulative_ws(self.trip.start, self.trip.end)
            sponsor_pv_dict = self.discount_pv
            pool = {}
            for x in trip_cumulative:
                total_balance = int(x['total_balance'])
                if total_balance < (self.trip.balance / 4):
                    continue
                mcode = x['mcode']
                calculator = TripCalculator(mcode)
                member = calculator.member
                new_balance, consume_with_previous, consume_with_overlap = calculator.get_trip_summary(member,
                                                                                                       self.trip)
                if new_balance < (self.trip.balance / 4):
                    continue
                out_bound_trip = TripApplication.objects.filter(member__mcode=mcode)
                new_entry = True
                if out_bound_trip.count() > 0:
                    right = new_balance // self.trip.balance
                    new_entry = False
                else:
                    right = new_balance // (self.trip.balance - self.trip.balance_discount)
                if right > self.trip.max_seat:
                    right = self.trip.max_seat

                if mcode not in sponsor_pv_dict.keys():
                    sponsor_pv = 0
                else:
                    sponsor_pv = sponsor_pv_dict[mcode]

                if 6000 <= sponsor_pv < 8000:
                    use_balance = self.trip.balance - 2000
                elif 8000 <= sponsor_pv < 10000:
                    use_balance = self.trip.balance - 4000
                elif 10000 <= sponsor_pv:
                    use_balance = 0
                else:
                    use_balance = self.trip.balance
                right_dc = 1 if new_balance >= use_balance and sponsor_pv >= 4000 else 0

                pool[mcode] = {
                    'right': right,
                    'balance': new_balance,
                    'use_other_trip': consume_with_previous,
                    'overlap_trip': consume_with_overlap,
                    'new_entry': new_entry,
                    'sponsor_pv': sponsor_pv,
                    'use_balance': use_balance,
                    'right_dc': right_dc
                }

            # for mc in sponsor_pv_dict.keys():
            #     if mc not in pool.keys():
            #         calculator = TripCalculator(mc)
            #         member = calculator.member
            #         new_balance, consume_with_previous, consume_with_overlap = calculator.get_trip_summary(member,
            #                                                                                                self.trip)
            #         if new_balance < (self.trip.balance / 4):
            #             continue
            #         out_bound_trip = TripApplication.objects.filter(member__mcode=mc, trip__trip_type='OS')
            #         new_entry = True
            #         if out_bound_trip.count() > 0:
            #             right = new_balance // self.trip.balance
            #             new_entry = False
            #         else:
            #             right = new_balance // (self.trip.balance - self.trip.balance_discount)
            #         if right > self.trip.max_seat:
            #             right = self.trip.max_seat
            #
            #         sponsor_pv = sponsor_pv_dict[mc]
            #         if 4000 <= sponsor_pv < 6000:
            #             use_balance = self.trip.balance
            #         elif 6000 <= sponsor_pv < 8000:
            #             use_balance = self.trip.balance - 2000
            #         elif 8000 <= sponsor_pv < 10000:
            #             use_balance = self.trip.balance - 4000
            #         elif 10000 <= sponsor_pv:
            #             use_balance = 0
            #         else:
            #             use_balance = self.trip.balance
            #         right_dc = 1 if new_balance >= use_balance and sponsor_pv >= 4000 else 0
            #
            #         pool[mc] = {
            #             'right': right,
            #             'balance': new_balance,
            #             'use_other_trip': consume_with_previous,
            #             'overlap_trip': consume_with_overlap,
            #             'new_entry': new_entry,
            #             'sponsor_pv': sponsor_pv,
            #             'use_balance': use_balance,
            #             'right_dc': right_dc
            #         }

            members = Member.objects.filter(mcode__in=pool.keys())
            for x in members:
                pool[x.mcode]['name'] = x.full_name
                pool[x.mcode]['level'] = x.level
                pool[x.mcode]['status'] = x.status

            list_pool = dict_transfrom.dict_to_list(pool)
            list_pool = sorted(list_pool, key=lambda x: x['balance'], reverse=True)
        else:
            trip_cumulative = WeekCommission.get_cumulative_ws(self.trip.start, self.trip.end)
            pool = {}
            for x in trip_cumulative:
                total_balance = int(x['total_balance'])
                if total_balance < (self.trip.balance / 4):
                    continue
                mcode = x['mcode']
                calculator = TripCalculator(mcode)
                member = calculator.member
                new_balance, consume_with_previous, consume_with_overlap = calculator.get_trip_summary(member,
                                                                                                       self.trip)
                if new_balance < (self.trip.balance / 4):
                    continue
                out_bound_trip = TripApplication.objects.filter(member__mcode=mcode, trip__trip_type='OS')
                new_entry = True
                if out_bound_trip.count() > 0:
                    right = new_balance // self.trip.balance
                    new_entry = False
                else:
                    right = new_balance // (self.trip.balance - self.trip.balance_discount)
                if right > self.trip.max_seat:
                    right = self.trip.max_seat
                pool[mcode] = {
                    'right': right,
                    'balance': new_balance,
                    'use_other_trip': consume_with_previous,
                    'overlap_trip': consume_with_overlap,
                    'new_entry': new_entry
                }

            members = Member.objects.filter(mcode__in=pool.keys())
            for x in members:
                pool[x.mcode]['name'] = x.full_name
                pool[x.mcode]['level'] = x.level
                pool[x.mcode]['status'] = x.status

            list_pool = dict_transfrom.dict_to_list(pool)
            list_pool = sorted(list_pool, key=lambda x: x['balance'], reverse=True)
        return dict_transfrom.list_to_dict(list_pool, 'key')

    def create_report(self):
        current_row = self.Meta.content_start_row
        self.create_head()
        pool = self.calculate()
        count = 1

        for k, v in pool.items():
            if v['status'] == 'Normal':
                self.fill_row(count, k, v, row=current_row)
                count += 1
                current_row += 1
            else:
                continue
        return

    @property
    def file_name(self):
        name = '{}_{}_{}'.format(self.Meta.file_name, self.trip.code, datetime.date.today())
        return '{}.xlsx'.format(name)
