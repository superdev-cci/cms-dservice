from Crypto.Cipher import AES
from django.contrib.auth import get_user_model
from rest_framework import HTTP_HEADER_ENCODING, exceptions
import base64
from rest_framework.authentication import get_authorization_header, TokenAuthentication
from member.models import Member


class MemberTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

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
