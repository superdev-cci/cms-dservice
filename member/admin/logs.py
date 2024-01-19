from django.conf.urls import url
from django.contrib import admin
from member.models import MemberLogs


@admin.register(MemberLogs)
class MemberLogsAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('id', 'member',)
    list_per_page = 50
    list_display = ('id', 'member', 'topic', 'change')
    list_select_related = ('member',)
    # list_filter = ('mtype1', 'level', 'honor', IsOcertFilter)
    raw_id_fields = ('member',)

    search_fields = ('member__mcode', 'member__name_t',)
