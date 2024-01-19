from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from ..models import BranchGoodsImportStatement, BranchGoodsImportItem
from jet.filters import DateRangeFilter


@admin.register(BranchGoodsImportStatement)
class BranchGoodsImportStatementAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = (
        'branch', 'from_branch', 'bill_number', 'date_issue', 'statement_type', 'statement_state', 'remark')
    list_filter = ('branch', 'statement_type', 'statement_state', 'from_branch', ('date_issue', DateRangeFilter))
    list_select_related = ('branch', 'statement_type', 'statement_state', 'from_branch')
    # raw_id_fields = ('member',)

    search_fields = ('branch__inv_code', 'bill_number',)


@admin.register(BranchGoodsImportItem)
class BranchGoodsImportItemAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('statement', 'product', 'price', 'qty', 'amount')
    list_filter = ('statement', 'product')
    list_select_related = ('statement', 'product')
    # raw_id_fields = ('member',)
    search_fields = ('statement__bill_number', 'product__pcode',)
