from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from ..models import StockStatement
from jet.filters import DateRangeFilter


@admin.register(StockStatement)
class StockStatementAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = (
        'branch_name', 'bill_number', 'date_issue', 'pcode', 'pdesc', 'incoming', 'outgoing', 'bring_forward', 'balance')
    list_filter = ('branch_name', 'pcode', ('date_issue', DateRangeFilter))
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('pcode', 'bill_number', 'client_code',)

    def incoming(self, obj):
        return obj.in_qty

    def outgoing(self, obj):
        return obj.out_qty
