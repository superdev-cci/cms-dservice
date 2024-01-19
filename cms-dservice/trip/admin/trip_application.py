from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import TripApplication


@admin.register(TripApplication)
class TripApplicationAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('sano',)
    list_per_page = 50
    list_display = (
    'id', 'get_member_code', 'get_member_name', 'trip', 'register_date', 'confirm_count', 'balance_use', 'previous_use')
    list_filter = ('trip',)
    list_select_related = ('member', 'trip')
    raw_id_fields = ('member', 'trip')

    search_fields = ('member__mcode', 'member__name_t')

    def get_member_code(self, obj):
        return obj.member.code

    get_member_code.short_description = 'Member code'

    def get_member_name(self, obj):
        return obj.member.full_name

    get_member_name.short_description = 'Member name'
