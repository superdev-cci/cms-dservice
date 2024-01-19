from django.contrib import admin
from ..models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'location')
    search_fields = ('name',)

