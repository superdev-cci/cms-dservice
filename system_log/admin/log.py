from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('sys_id', 'subject', 'detail', 'ip', 'logdate',)
    list_filter = ('sys_id', )
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('subject', 'detail', 'ip')
