from django.conf.urls import url
from django.contrib import admin
from member.models import MemberActive, MemberDocumentCheckup


@admin.register(MemberActive)
class MemberActiveAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('member',)
    list_per_page = 50
    list_display = ('member', 'last_seen')

    search_fields = ('member',)


@admin.register(MemberDocumentCheckup)
class MemberDocumentCheckupAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_per_page = 50
    list_display = ('date_issue', 'suspend', 'terminate')
