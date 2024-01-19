from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import LineAgent


@admin.register(LineAgent)
class LineAgentAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display = ('id', 'agent', 'token')
    list_display_links = ('agent',)
    list_per_page = 25
