from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import SaleInvoice, SaleItem


@admin.register(SaleInvoice)
class SaleInvoiceAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('id', 'sano', 'sadate', 'sctime', 'inv_code', 'mcode', 'name_t', 'sa_type', 'total', 'tot_pv')
    list_filter = ('inv_code', 'sa_type', 'cancel')
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('sano', 'mcode', 'name_t')


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('id', 'sano', 'pcode', 'price', 'pv', 'amt', 'qty', )
    list_filter = ('pcode', 'inv_code',)
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    # search_fields = ('sano', 'mcode', 'name_t')
