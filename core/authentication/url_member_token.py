import datetime
from django.contrib.auth import get_user_model
from Crypto.Cipher import AES
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from django.utils.translation import gettext as _
import base64
from member.models import Member


class URLTokenMemberAuthentication(BaseAuthentication):

    def authenticate(self, request):
        query_params = request.query_params
        if 'token' in query_params:
            token = query_params['token']
            user, member = self.authenticate_credentials(token)
            if user is not None:
                setattr(request, 'member', member)
            return user, token

    def authenticate_credentials(self, key):
        user_model = get_user_model()
        entry = AES.new('uyth5vm2s9qtfkyv', AES.MODE_CFB, 'rfvtgbyhnujmikug')
        raw_pwd = base64.b64decode(key)[16:]
        passwd = entry.decrypt(raw_pwd)
        password = passwd.decode('utf-8')
        member_id, member_code, member_pass = password.split(':')
        user = None
        member = None
        try:
            member = Member.objects.get(id=member_id, mcode=member_code, sv_code=member_pass)
            user = user_model(username=member.code)
        except Member.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return user, member
