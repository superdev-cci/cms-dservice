from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import LogTravelCredit


@admin.register(LogTravelCredit)
class LogTravelCreditAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('sano', 'mcode', 'sadate', 'value_in', 'value_out', 'value_option', 'sa_type',)
    list_filter = ('sa_type', )
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('sano', 'mcode',)
