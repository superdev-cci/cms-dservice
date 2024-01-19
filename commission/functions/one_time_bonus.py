from collections import OrderedDict

from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1

from commission.models import AllSaleBonus, HonorChangeLog
from member.models import Member
from core.mixin import MonthMixIn
from core.report.excel import ExcelTemplateReport
from datetime import date


class OneTimeBonusCalculator(ExcelTemplateReport, MonthMixIn):
    level_ref = {
        'PE': 1,
        'SE': 2,
        'EE': 3,
        'DE': 4,
        'CE': 5
    }

    bonus = {
        'PE': 3000,
        'SE': 8000,
        'EE': 30000,
        'DE': 62000,
        'CE': 150000
    }

    template_file = './templates/report/commission/one_time_bonus.xlsx'

    class Meta:
        title = 'One time bonus report'
        sheet_name = 'One time bonus'
        file_name = 'one_time_bonus'
        head_file = 'One time bonus'
        head_start_col = 4
        head_start_row = 7
        content_start_col = 1
        content_start_row = 9

    def __init__(self, start, end, *args, **kwargs):
        super(OneTimeBonusCalculator, self).__init__(*args, **kwargs)
        self.start = start
        self.end = end
        self.qualified = {
            'PE': 0,
            'SE': 0,
            'EE': 0,
            'DE': 0,
            'CE': 0
        }
        self.month_range = self._calculate_month_range(self.start, self.end)

    def add_to_pool(self, pool, instance):
        if pool.get(instance.mcode):
            last_level = self.level_ref.get(pool[instance.mcode]['last'])
            current = self.level_ref.get(instance.qualified_position)
            if current > last_level:
                pool[instance.mcode][instance.fdate.strftime('%b')] = {
                    'level': instance.qualified_position,
                    'bonus': self.bonus.get(instance.qualified_position)
                }
                self.qualified[instance.qualified_position] += 1
            else:
                pool[instance.mcode][instance.fdate.strftime('%b')] = {
                    'level': instance.qualified_position,
                    'bonus': 0
                }
        else:
            pool[instance.mcode] = {}
            pool[instance.mcode][instance.fdate.strftime('%b')] = {
                'level': instance.qualified_position,
                'bonus': self.bonus.get(instance.qualified_position)
            }
            self.qualified[instance.qualified_position] += 1

        pool[instance.mcode]['last'] = instance.qualified_position
        pool[instance.mcode]['name'] = instance.member_name

    def calculate(self):
        pool = {}
        for d in self.month_range:
            start_date, end_date = self._calculate_period(d)
            honor_log = {x.mcode: x for x in HonorChangeLog.objects.filter(date_change__range=(start_date, end_date))}
            current_round = AllSaleBonus.objects.filter(fdate__range=(start_date, end_date))
            for x in current_round:
                h_log = honor_log.get(x.mcode)
                if h_log:
                    if h_log.first_honor:
                        continue

                if x.is_qualified:
                    self.add_to_pool(pool, x)
        return pool

    def create_head(self):
        current = self.Meta.head_start_col
        current_row = self.Meta.head_start_row

        cell = self.get_cell(current, current_row + 1)
        cell.value = 'Last Level'
        cell.border = self.style['full_border']
        cell.alignment = self.style['align_center']
        current += 1

        for d in self.month_range:
            cell_range = self.get_string_cell_range(current, current_row, current + 1, current_row)
            self.work_sheet.merge_cells(cell_range)
            self.style_range(self.work_sheet, cell_range, self.style['full_border'], self.style['align_center'])
            cell = self.get_cell(current, current_row)
            cell.value = d.strftime('%b')
            cell = self.get_cell(current, current_row + 1)
            cell.value = 'Level'
            cell.alignment = self.style['align_center']
            cell.border = self.style['full_border']
            cell = self.next_cell(cell, 1, 0)
            cell.value = 'Bonus'
            cell.alignment = self.style['align_center']
            cell.border = self.style['full_border']
            current += 2

        self.work_sheet['C3'] = '{}'.format(self.Meta.head_file)
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')
        return

    def create_summary(self, current_row):
        return

    def create_report(self):
        current_row = self.Meta.content_start_row
        self.create_head()
        pool = self.calculate()
        count = 1
        members = {x.mcode: x for x in Member.objects.filter(mcode__in=list(pool.keys()))}
        honor_log = {x.mcode: x for x in HonorChangeLog.objects.filter(mcode__in=pool.keys(), pos_before='')}
        for k, v in pool.items():
            v['honor_date'] = honor_log[k].date_change
            v['honor_first'] = honor_log[k].pos_after

            self.fill_row(count, k, v, row=current_row)
            count += 1
            current_row += 1

        self.create_summary(current_row)
        print(self.qualified)
        self.save_file()
        return

    def build_row_meta(self, count, member_code, data, **kwargs):
        row = kwargs.get('row')
        month_range = self._calculate_month_range(self.start, self.end)
        row_meta = [
            ('no', {'data': count, 'alignment': self.style['align_center']}),
            ('mcode', {'data': member_code, 'alignment': self.style['align_center']}),
            ('person', {'data': data['name']}),
            ('last', {'data': data['last'], 'alignment': self.style['align_center']}),
        ]
        cell_string = []
        cell_index = self.Meta.content_start_col + 5
        for x in month_range:
            current_month = x.strftime('%b')
            bonus = 0
            level = '-'
            if data.get(current_month):
                bonus = data[current_month]['bonus']
                level = data[current_month]['level']
            cell_string.append(self.get_string_cell(cell_index, row))
            cell_index += 2
            row_meta.append((current_month + '_level', {
                'data': level,
                'alignment': self.style['align_center']
            }))
            row_meta.append((current_month + '_bonus', {
                'data': bonus,
                'number_format': FORMAT_NUMBER_COMMA_SEPARATED1,
                'alignment': self.style['align_right']
            }))

        row_meta.append(('sum', {
            'data': '=SUM({})'.format(','.join(cell_string)),
            'number_format': FORMAT_NUMBER_COMMA_SEPARATED1,
            'alignment': self.style['align_right']
        }))

        row_meta.append(('honor_date', {
            'data': data['honor_date'],
        }))

        row_meta.append(('honor_first', {
            'data': data['honor_first'],
        }))

        return OrderedDict(row_meta)

    @property
    def file_name(self):
        name = '{}'.format(self.Meta.file_name)
        return '{}.xlsx'.format(name)
