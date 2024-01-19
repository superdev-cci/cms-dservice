from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import TravelPointStack


@admin.register(TravelPointStack)
class TravelPointStackAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('id', 'get_member_code')
    list_per_page = 50
    list_display = (
        'id', 'get_member_code', 'get_member_name', 'stamp_date', 'gold_point',
        'remaining_gold_point', 'silver_point', 'remaining_silver_point')
    list_filter = ('stamp_date',)
    list_select_related = ('member',)
    raw_id_fields = ('member',)
    search_fields = ('member__mcode', 'member__name_t')

    def get_member_code(self, obj):
        return obj.member.code

    get_member_code.short_description = 'Member code'

    def get_member_name(self, obj):
        return obj.member.full_name

    get_member_name.short_description = 'Member name'
