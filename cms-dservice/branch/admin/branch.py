from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = ('inv_code', 'inv_desc', 'inv_type', 'bill_ref')
    list_filter = ('inv_code', 'inv_type',)
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('inv_code', )



