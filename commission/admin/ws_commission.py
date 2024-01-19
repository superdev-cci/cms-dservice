from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.urls import reverse
from ..models import WeakStrongSummary
from jet.filters import DateRangeFilter


@admin.register(WeakStrongSummary)
class WeakStrongSummaryAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('member', 'bill_number')
    list_per_page = 50
    list_display = ('rcode', 'date_issue', 'member', 'member_name', 'current_pos', 'current_left', 'current_right', 'previous_left',
                    'previous_right', 'total_left', 'total_right', 'remaining_left', 'remaining_right',
                    'balance', 'total')
    list_select_related = ('member', )
    list_filter = ('rcode', ('date_issue', DateRangeFilter))
    raw_id_fields = ('member',)
    search_fields = ('member__mcode', 'member__name_t')
