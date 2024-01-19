from base64 import b64encode, b64decode
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from oauth2_provider.backends import OAuth2Backend
from rest_framework.authentication import get_authorization_header, BasicAuthentication
from member.models import Member
from rest_framework import exceptions


class ChangePasswordModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)
        try:
            case_insensitive_username_field = '{}'.format(user_model.USERNAME_FIELD)
            user = user_model._default_manager.get(**{case_insensitive_username_field: username})
            if not user.check_password(password):
                try:
                    m_obj = Member.objects.get(mcode=username.upper(), sv_code=password, level__in=["VIP", "DIS", "PRO"])
                    user.useraccount.set_password(m_obj.sv_code)
                    return user
                except Member.DoesNotExist:
                    # raise exceptions.AuthenticationFailed('Invalid Password')
                    pass
        except user_model.DoesNotExist:
            # raise exceptions.AuthenticationFailed('Invalid Username')
            pass
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user




