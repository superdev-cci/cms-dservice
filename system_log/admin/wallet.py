from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import LogWallet


@admin.register(LogWallet)
class LogWalletAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('rcode', 'fdate', 'mcode', 'ewallet', 'evoucher', 'eautoship',)
    list_filter = ('rcode', )
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('mcode',)
