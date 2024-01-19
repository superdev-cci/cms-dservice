from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.urls import reverse
from ..models import WeekCommission
from jet.filters import DateRangeFilter


@admin.register(WeekCommission)
class WeekCommissionAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('member', 'bill_number')
    list_per_page = 50
    list_display = ('rcode', 'date_issue', 'member', 'name_t', 'fast_bonus', 'ws_bonus', 'resale', 'total_commission', 'sano_ewallet',)
    list_select_related = ('member', )
    list_filter = ('rcode', ('fdate', DateRangeFilter))
    raw_id_fields = ('member',)
    search_fields = ('member__mcode', 'member__name_t')
