from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import BranchStock


@admin.register(BranchStock)
class BranchStockAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('inv_code', 'pcode', 'qty', )
    list_filter = ('inv_code', 'pcode',)
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('pcode', )



