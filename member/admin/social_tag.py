from django.conf.urls import url
from django.contrib import admin
from member.models import MemberSocialTagConfig


@admin.register(MemberSocialTagConfig)
class MemberSocialTagConfigAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('id', 'member',)
    list_per_page = 50
    list_display = ('id', 'member', 'pixel_id', 'line_tag_id', 'google_tag_id')
    list_select_related = ('member',)
    raw_id_fields = ('member',)

    search_fields = ('member__mcode', 'member__name_t',)
