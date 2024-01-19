from abc import ABC
from collections import OrderedDict
from datetime import date
from django.db.models import Min, Max, Count

from member.models import Member
from core.report.excel import ExcelTemplateReport


class MemberWithHonorSponsorDepth(ExcelTemplateReport, ABC):
    template_file = './templates/report/member/sponsor.xlsx'

    class Meta:
        title = 'Member sponsor depth'
        sheet_name = 'Summary'
        file_name = 'member_sponsor'
        head_file = 'Member sponsor depth'
        head_start_col = 4
        head_start_row = 6
        content_start_col = 1
        content_start_row = 8

    def __init__(self, *args, **kwargs):
        super(MemberWithHonorSponsorDepth, self).__init__(**kwargs)
        self.honor = kwargs.get('honor', '')
        assert self.honor != '', 'Invalid honor type'
        return

    def create_head(self):
        self.work_sheet['C3'] = self.Meta.title
        self.work_sheet['D4'] = date.today().strftime('%d/%b/%Y')
        return

    def get_queryset(self):
        queryset = Member.objects.filter(honor=self.honor, status_terminate=0)
        return queryset

    def get_data(self, queryset):
        pool = {}
        for x in queryset:
            child = x.sponsor_child
            data = child.filter(status_terminate=0, level__in=('DIS', 'PRO', 'VIP')).aggregate(
                max_depth=Max('sponsor_depth'),
                min_depth=Min('sponsor_depth'), total_child=Count('mcode'))
            pool[x.code] = {
                'max': data['max_depth'],
                'min': data['min_depth'],
                'count': data['total_child'],
                'name': x.full_name,
                'honor': x.honor,
                'start': x.sponsor_depth,
            }
            if data['max_depth'] is None:
                pool[x.code]['depth'] = 0
            else:
                pool[x.code]['depth'] = data['max_depth'] - x.sponsor_depth
        return pool

    def build_row_meta(self, count, member_code, data, **kwargs):
        row_meta = [
            ('no', {'data': count, 'alignment': self.style['align_center']}),
            ('mcode', {'data': member_code, 'alignment': self.style['align_center']}),
            ('name', {'data': data['name']}),
            ('honor', {'data': data['honor']}),
            ('depth', {'data': data['depth']}),
            ('min', {'data': data['min']}),
            ('max', {'data': data['max']}),
            ('count', {'data': data['count']}),
        ]
        return OrderedDict(row_meta)

    def process_data(self):
        count = 1
        current_row = self.Meta.content_start_row
        self.create_head()
        queryset = self.get_queryset()

        for k, v in self.get_data(queryset).items():
            self.fill_row(count, k, v, row=current_row)
            count += 1
            current_row += 1
        return

    @property
    def file_name(self):
        name = '{}_{}'.format(self.Meta.file_name, self.honor)
        return '{}.xlsx'.format(name)
