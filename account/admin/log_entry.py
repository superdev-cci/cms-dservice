from django.contrib import admin
from django.contrib.admin.models import LogEntry


@admin.register(LogEntry)
class AdminLogEntryAdmin(admin.ModelAdmin):
    model = LogEntry
    list_per_page = 50
    list_display = ('action_time', 'user', 'object_repr', 'action_flag', 'change_message')
    list_select_related = ('user',)
