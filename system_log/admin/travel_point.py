from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import LogTravelPoint


@admin.register(LogTravelPoint)
class LogTravelPointAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_per_page = 50
    list_display = (
        'id', 'date_issue', 'member', 'statement', 'silver_in', 'silver_out', 'gold_in', 'gold_out', 'total', 'remark',)
    list_select_related = ('member',)
    raw_id_fields = ('member',)

    search_fields = ('member__mcode', 'member__name_t')
