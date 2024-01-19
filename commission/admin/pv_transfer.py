from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.urls import reverse
from ..models import PvTransfer
from jet.filters import DateRangeFilter


@admin.register(PvTransfer)
class PvTransferAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('member', 'bill_number')
    list_per_page = 50
    list_display = ('hono', 'sadate', 'mcode', 'name_t', 'bill_type', 'pv', 'create_user', 'is_cancel', 'remark', 'remote_ip', 'menu_actions')
    list_select_related = ('member', 'create_user')
    list_filter = ('sa_type', ('sadate', DateRangeFilter))
    raw_id_fields = ('member', 'create_user')
    search_fields = ('member__mcode', 'member__name_t')

    def bill_type(self, obj):
        annotate = {
            'A': 'Normal',
            'Y': 'Transfer',
            'AM': 'Sale Maintain',
            'AE': 'Expired'
        }
        if obj.sa_type in annotate:
            return annotate[obj.sa_type]
        return '-'

    def pv(self, obj):
        return obj.tot_pv

    def is_cancel(self, obj):
        return int(obj.cancel) > 0

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<statement_id>.+)/proc_ae/$',
                self.admin_site.admin_view(self.process_ae_action),
                name='commission-fix-ae',
            ),
        ]
        return custom_urls + urls

    def menu_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Fix Expired</a>',
            reverse('admin:commission-fix-ae', args=[obj.pk]),
        )

    def process_ae_action(self, request, statement_id, *args, **kwargs):
        try:
            obj = PvTransfer.objects.get(hono=statement_id)
            if obj.sa_type == 'AE':
                obj.sa_type = 'A'
                obj.save()
        except Exception as e:
            pass
        return redirect('/admin/commission/pvtransfer/')
