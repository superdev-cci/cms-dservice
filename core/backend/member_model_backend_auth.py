from base64 import b64encode, b64decode
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from oauth2_provider.backends import OAuth2Backend
from rest_framework.authentication import get_authorization_header, BasicAuthentication
from member.models import Member
from account.models import UserAccount
from rest_framework import exceptions
from member.functions.reformat_data import format_name


class CreateMemberModelBackend(ModelBackend):

    def user_can_authenticate(self, user):
        result = super(CreateMemberModelBackend, self).user_can_authenticate(user)
        if result and user.useraccount.member:
            if user.useraccount.member.status == 'Normal':
                return True
        return False

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)
        try:
            case_insensitive_username_field = '{}__iexact'.format(user_model.USERNAME_FIELD)
            user = user_model._default_manager.get(**{case_insensitive_username_field: username})
        except user_model.DoesNotExist:
            try:
                m_obj = Member.objects.get(mcode=username.upper(), sv_code=password, level__in=["VIP", "DIS", "PRO"])
                name_dict = format_name({}, m_obj.name_t)
                first_name = name_dict['name']
                last_name = name_dict.get('surname', "")
                uac = UserAccount(member=m_obj)
                user = uac.create_member_account(username.upper(), password, first_name, last_name)
                return user
            except Member.DoesNotExist:
                # raise exceptions.AuthenticationFailed('Invalid User')
                pass
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
