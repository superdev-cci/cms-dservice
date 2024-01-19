from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from ..models import BranchGoodsSnapRemainingStatement, BranchGoodsSnapRemainingItem
from jet.filters import DateRangeFilter


class BranchGoodsSnapRemainingItemInlineAdmin(admin.TabularInline):
    model = BranchGoodsSnapRemainingItem
    raw_id_fields = ('statement', 'product')


@admin.register(BranchGoodsSnapRemainingStatement)
class BranchGoodsSnapRemainingStatementAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = (
        'branch', 'bill_number', 'date_issue', 'remark')
    list_filter = ('branch', 'statement_type', 'statement_state', ('date_issue', DateRangeFilter))
    list_select_related = ('branch', 'statement_type', 'statement_state',)
    # raw_id_fields = ('member',)

    search_fields = ('branch__inv_code', 'bill_number',)
    inlines = [BranchGoodsSnapRemainingItemInlineAdmin, ]
