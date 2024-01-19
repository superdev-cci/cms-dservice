from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import ShippingBox


@admin.register(ShippingBox)
class ShippingBoxAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('name',)
    list_per_page = 50
    list_display = ('id', 'name', 'height', 'length', 'width', 'max_weight')
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('name', )

