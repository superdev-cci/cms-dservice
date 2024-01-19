from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import AliUser


@admin.register(AliUser)
class StaffUserAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('usercode',)
    list_per_page = 25
    list_display = ('usercode', 'username', 'usertype', 'inv_ref', 'accessright', )
    list_filter = ('usertype', 'inv_ref')
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('usercode', 'username',)
