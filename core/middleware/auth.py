from django.utils.deprecation import MiddlewareMixin
from Crypto.Cipher import AES
import base64
from member.models import Member


class MemberAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # do something only if request contains a Bearer token
        if request.META.get("HTTP_AUTHORIZATION", "").startswith("Bearer"):
            token = request.META.get("HTTP_AUTHORIZATION", "").split(' ')[1]
            entry = AES.new('uyth5vm2s9qtfkyv', AES.MODE_CFB, 'rfvtgbyhnujmikug')
            raw_pwd = base64.b64decode(token)[16:]
            passwd = entry.decrypt(raw_pwd)
            password = passwd.decode('utf-8')
            member_id, member_code, member_pass = password.split(':')
            print(member_id, member_code, member_pass)
            member = Member.objects.filter(id=member_id, mcode=member_code, sv_code=member_pass)
            if len(member):
                setattr(request, 'member', member.first())
                return
        return
1