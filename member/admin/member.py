from django.conf.urls import url
from django.contrib import admin, messages
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.urls import reverse

from ..forms.hold_pv import MemberHoldPvActionForm
from ..models import Member, MemberGroup, ClientVatType


class IsOcertFilter(admin.SimpleListFilter):
    title = 'Online Cert'
    parameter_name = 'online_cert'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(ocert=1)
        elif value == 'No':
            return queryset.filter(ocert=0)
        return queryset


@admin.register(MemberGroup)
class MemberGroupAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('mcode',)
    list_per_page = 50
    list_display = ('id', 'name', 'code',)
    # list_select_related = ('member',)
    # list_filter = ('mtype1', 'level', 'honor', IsOcertFilter)
    # raw_id_fields = ('member',)

    # search_fields = ('mcode', 'name_t',)


@admin.register(ClientVatType)
class ClientVatTypeAdmin(admin.ModelAdmin):
    empty_value_display = '--None--'
    # list_display_links = ('mcode',)
    list_per_page = 50
    list_display = ('id', 'name', 'code',)
    # list_select_related = ('member',)
    # list_filter = ('mtype1', 'level', 'honor', IsOcertFilter)
    # raw_id_fields = ('member',)

    # search_fields = ('mcode', 'name_t',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    change_list_template = 'admin/members/member/change_list.html'
    empty_value_display = '--None--'
    list_display_links = ('mcode',)
    list_per_page = 50
    list_display = ('mcode', 'name_t', 'mdate', 'level', 'honor', 'sv_code', 'online_cert', 'hpv', 'member_actions')
    # list_select_related = ('member',)
    list_filter = ('mtype1', 'level', 'honor', IsOcertFilter)
    exclude = ('favorite', )
    raw_id_fields = ('agency_ref', )
    search_fields = ('mcode', 'name_t',)

    def online_cert(self, obj):
        return obj.ocert > 0

    online_cert.boolean = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<member_id>.+)/active/$',
                self.admin_site.admin_view(self.process_ocert_action),
                name='member-setcert',
            ),
            url(r'^change_hpv/$', self.admin_site.admin_view(self.sync_member), name='member-change-hpv', ),
        ]
        return custom_urls + urls

    def member_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Set OCert</a>',
            reverse('admin:member-setcert', args=[obj.pk]),
        )

    def process_ocert_action(self, request, member_id, *args, **kwargs):
        try:
            obj = Member.objects.get(id=member_id)
            if obj.ocert:
                obj.ocert = False
            else:
                obj.ocert = True
            obj.save()
        except Exception as e:
            pass
        return redirect('/admin/member/member/')

    def sync_member(self, request, *args, **kwargs):
        if request.method != 'POST':
            form = MemberHoldPvActionForm()
        else:
            form = MemberHoldPvActionForm(request.POST)
            if form.is_valid():
                try:
                    member = Member.objects.get(mcode=form.cleaned_data['member'])
                    member.hpv = int(form.cleaned_data['hpv'])
                    member.save()
                except Member.DoesNotExist as e:
                    pass
                self.message_user(request, "SUCCESS", level=messages.SUCCESS)
                return redirect('/admin/member/member/')

        context = self.admin_site.each_context(request)
        context['form'] = form
        context['title'] = 'Change hpv'
        return TemplateResponse(
            request,
            'change_hpv.html',
            context,
        )