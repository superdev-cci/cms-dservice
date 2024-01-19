from django.conf.urls import url
from django.contrib import admin, messages
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.html import format_html

from ..models import TravelPointUseStatement
from trip.functions.travel_point_stack import TravelPointStackOperator

@admin.register(TravelPointUseStatement)
class TravelPointUseStatementAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    list_display_links = ('id', 'get_member_code')
    list_per_page = 50
    list_display = (
        'id', 'bill_number', 'get_member_code', 'get_member_name', 'trip', 'issue_date', 'state', 'gold_coin', 'silver_coin',
        'cancel_actions')
    list_filter = ('trip', )
    list_select_related = ('member', 'trip')
    raw_id_fields = ('member', 'trip')

    search_fields = ('member__mcode', 'member__name_t')

    def get_member_code(self, obj):
        return obj.member.code

    get_member_code.short_description = 'Member code'

    def get_member_name(self, obj):
        return obj.member.full_name

    get_member_name.short_description = 'Member name'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<pk>.+)/cancel/$',
                self.admin_site.admin_view(self.process_cancel_action),
                name='travel_point_cancel',
            ),
        ]
        return custom_urls + urls

    def cancel_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Cancel</a>',
            reverse('admin:travel_point_cancel', args=[obj.pk]),
        )

    def process_cancel_action(self, request, pk, *args, **kwargs):
        try:
            obj = TravelPointUseStatement.objects.get(pk=pk)
            if obj.state == "CM":
                stack = TravelPointStackOperator(member=obj.member)
                if obj.gold_coin > 0:
                    stack.push_gold_stack(obj.gold_coin)
                if obj.silver_coin > 0:
                    stack.push_silver_stack(obj.silver_coin)
                obj.state = "CA"
                obj.save()
                self.message_user(request, 'Complete', level=messages.SUCCESS)
            else:
                self.message_user(request, 'Not change', level=messages.WARNING)
        except Exception as e:
            print(e.__str__())
        return redirect('/admin/trip/travelpointusestatement/')
