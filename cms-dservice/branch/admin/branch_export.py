from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from ..models import BranchGoodsExportStatement, BranchGoodsExportItem
from jet.filters import DateRangeFilter


@admin.register(BranchGoodsExportStatement)
class BranchGoodsExportStatementAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = (
        'branch', 'to_branch', 'bill_number', 'date_issue', 'statement_type', 'statement_state', 'remark')
    list_filter = ('branch', 'statement_type', 'statement_state', 'to_branch', ('date_issue', DateRangeFilter))
    list_select_related = ('branch', 'statement_type', 'statement_state', 'to_branch')
    # raw_id_fields = ('member',)

    search_fields = ('branch__inv_code', 'bill_number',)


@admin.register(BranchGoodsExportItem)
class BranchGoodsExportItemAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('statement', 'product', 'price', 'qty', 'amount')
    list_filter = ('statement', 'product')
    list_select_related = ('statement', 'product')
    # raw_id_fields = ('member',)
    search_fields = ('statement__bill_number', 'product__pcode',)


