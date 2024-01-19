from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import HoldPvStack


@admin.register(HoldPvStack)
class HoldPvStackAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('member', 'bill_number')
    list_per_page = 50
    list_display = ('member', 'stamp_date', 'pv', 'remaining', 'stack_type')
    list_select_related = ('member',)
    raw_id_fields = ('member',)
    search_fields = ('member__mcode','member__name_t')
