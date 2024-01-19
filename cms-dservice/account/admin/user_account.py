from django.contrib import admin
from ..models import UserAccount
from oauth2_provider.admin import AccessTokenAdmin
from oauth2_provider.models import AccessToken

admin.site.unregister(AccessToken)


@admin.register(AccessToken)
class SystemAccessTokenAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ("token", "user", "application", "expires")
    list_select_related = ('user', 'application')
    list_filter = ('user__groups', )
    raw_id_fields = ("user",)
    search_fields = ('user__username', )
    model = AccessToken


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    model = UserAccount
    list_per_page = 50
    list_display = ('id', 'get_user', 'get_user_name', 'is_staff')
    list_select_related = ('member', 'user')
    raw_id_fields = ('member', 'user')
    search_fields = ('member__mcode', 'user__username')

    def get_user(self, obj):
        return obj.user.username

    get_user.short_description = 'User'

    def get_user_name(self, obj):
        return obj.user.get_full_name()

    get_user_name.short_description = 'Name'

    def is_staff(self, obj):
        return obj.user.is_staff

    is_staff.short_description = 'Staff'


