from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from ..models import Promotion, PromotionItem
from ..models import DropShipPromotionType, DropShipPromotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('pcode',)
    list_per_page = 50
    list_display = ('pcode', 'pdesc', 'price', 'pv',)
    # list_filter = ('group_id',)
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('pcode', 'pdesc',)


@admin.register(PromotionItem)
class PromotionItemAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('package',)
    list_per_page = 50
    list_display = ('package', 'pcode', 'pdesc', 'qty')
    list_filter = ('pcode',)
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('package', 'pdesc')


@admin.register(DropShipPromotionType)
class DropShipPromotionTypeAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('name',)
    list_per_page = 50
    list_display = ('name', 'meta', )
    # list_filter = ('group_id',)
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('name',)


@admin.register(DropShipPromotion)
class DropShipPromotionAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('name',)
    list_per_page = 50
    list_display = ('name', 'formula', 'priority')
    # list_filter = ('group_id',)
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('name', )
