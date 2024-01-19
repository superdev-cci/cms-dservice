from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.html import format_html

from ..models import Product, ProductCategory, ProductClass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('pcode',)
    list_per_page = 50
    list_display = (
        'pcode', 'pdesc', 'group_id', 'product_class', 'price', 'get_member_price',
        'get_resale_price', 'pv', 'product_img', 'activated', 'product_actions')
    list_filter = ('group_id', 'activated', 'product_class')
    list_select_related = ('product_class',)
    # raw_id_fields = ('member',)

    search_fields = ('pcode', 'pdesc',)

    def get_member_price(self, obj):
        return obj.customer_price

    get_member_price.short_description = 'Member Prices'

    def get_resale_price(self, obj):
        return obj.personel_price

    get_resale_price.short_description = 'Resale Prices'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<product_id>.+)/active/$',
                self.admin_site.admin_view(self.process_product_action),
                name='product-active',
            ),
        ]
        return custom_urls + urls

    def product_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Active</a>',
            reverse('admin:product-active', args=[obj.pk]),
        )

    def process_product_action(self, request, product_id, *args, **kwargs):
        try:
            obj = Product.objects.get(pcode=product_id)
            if obj.activated:
                obj.activated = False
            else:
                obj.activated = True
            obj.save()
        except Exception as e:
            pass
        return redirect('/admin/ecommerce/product/')

    product_actions.short_description = 'Actions'
    product_actions.allow_tags = True


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('pcode',)
    list_per_page = 50
    list_display = ('groupname',)
    # list_filter = ('group_id', )
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('groupname',)


@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('pcode',)
    list_per_page = 50
    list_display = ('name', 'description')
    # list_filter = ('group_id', )
    # list_select_related = ('member',)
    # raw_id_fields = ('member',)

    search_fields = ('name',)
