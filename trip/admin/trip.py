from django.conf.urls import url
from django.contrib import admin, messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.html import format_html
from io import BytesIO
from trip.report.trip_enroll import TripEnrollReport
from trip.functions.trip_pt_cal import check_report_pt
from trip.functions.trip_nl_cal import check_report_nl
import pandas as pd
from openpyxl.writer.excel import save_virtual_workbook
from ..models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('name',)
    list_per_page = 50
    list_display = (
        'id', 'name', 'code', 'start', 'end', 'required_gold', 'required_silver', 'minimum_matching', 'max_seat',
        'report_actions')
    list_filter = ('start', 'end', 'active')

    # list_select_related = ('member',)

    # search_fields = ('pcode', )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<pk>.+)/enrol/$',
                self.admin_site.admin_view(self.process_trip_report_action),
                name='trip-tripreport',
            ),
        ]
        return custom_urls + urls

    def report_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Enroll</a>',
            reverse('admin:trip-tripreport', args=[obj.pk]),
        )

    def process_tripenroll_action(self, request, pk, *args, **kwargs):
        try:
            obj = Trip.objects.get(id=pk)
            report = TripEnrollReport(obj.code)
            report.create_report()
            response = HttpResponse(report.response_file,
                                    content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename={}'.format(report.file_name)
            self.message_user(request, 'Complete', level=messages.SUCCESS)
            return response
        except Exception as e:
            print(e.__str__())
        return

    def process_trip_report_action(self, request, pk, *args, **kwargs):
        try:
            obj = Trip.objects.get(id=pk)
            bio = BytesIO()
            if obj.code == "PT2021":
                df = check_report_pt(obj)
                excel_file = pd.ExcelWriter(bio, engine='openpyxl')
                df.to_excel(excel_file, header=True, encoding="utf-8", na_rep=0)
                response = HttpResponse(save_virtual_workbook(excel_file.book),
                                        content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename={}'.format("2021_pt_trip.xlsx")
            elif obj.code == "2020NR":
                df = check_report_nl(obj)
                excel_file = pd.ExcelWriter(bio, engine='openpyxl')
                df.to_excel(excel_file, header=True, encoding="utf-8", na_rep=0)
                response = HttpResponse(save_virtual_workbook(excel_file.book),
                                        content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename={}'.format("2021_nl_trip.xlsx")
            else:
                report = TripEnrollReport(obj.code)
                report.create_report()
                response = HttpResponse(report.response_file,
                                        content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename={}'.format(report.file_name)
            self.message_user(request, 'Complete', level=messages.SUCCESS)
            return response
        except Exception as e:
            print(e.__str__())
        return
