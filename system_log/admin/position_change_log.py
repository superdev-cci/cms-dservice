from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import PositionChangeLog


@admin.register(PositionChangeLog)
class PositionChangeLogAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_per_page = 20
    list_display = ('uid', 'mcode', 'pos_before', 'pos_after', 'date_change',)
    list_filter = ('mcode', 'pos_before', 'pos_after')
    search_fields = ('mcode', 'pos_before', 'pos_after')
