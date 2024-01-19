from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import StatementType, StatementState


@admin.register(StatementType)
class StatementTypeAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_per_page = 50
    list_display = ('name', 'code', 'use_app')
    search_fields = ('name', 'code')


@admin.register(StatementState)
class StatementStateAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_per_page = 50
    list_display = ('name', 'code', 'use_app')
    search_fields = ('name', 'code')
