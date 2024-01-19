from django.conf.urls import url
from django.contrib import admin
from member.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('id', 'member',)
    list_per_page = 50
    list_display = ('id', 'member', 'code', 'stamp_date', 'note', 'status')
    list_select_related = ('member',)
    raw_id_fields = ('member',)

    search_fields = ('member__mcode', 'member__name_t',)
