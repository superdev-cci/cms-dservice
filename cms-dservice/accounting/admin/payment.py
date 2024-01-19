from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import PaymentType


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_per_page = 50
    list_display = ('name', 'code')
    search_fields = ('name', 'code')