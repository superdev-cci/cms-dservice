from django.conf.urls import url
from django.contrib import admin
from member.models import MemberStatusStack


@admin.register(MemberStatusStack)
class MemberStatusStackAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('id', 'member',)
    list_per_page = 50
    list_display = ('id', 'member', 'issue_date', 'stack_type')
    list_select_related = ('member',)
    list_filter = ('stack_type',)
    raw_id_fields = ('member',)

    search_fields = ('member__mcode', 'member__name_t',)
