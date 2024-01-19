from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.urls import reverse
from ..models import HonorChangeLog
from jet.filters import DateRangeFilter


@admin.register(HonorChangeLog)
class HonorChangeLogAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('member', 'bill_number')
    list_per_page = 50
    list_display = ('rcode', 'mcode', 'pos_before', 'pos_after', 'date_change', 'date_update', 'type', 'is_moving_up')
    list_filter = ('rcode', ('date_change', DateRangeFilter),)
    search_fields = ('mcode', 'name_t')