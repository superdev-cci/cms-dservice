from django.utils.deprecation import MiddlewareMixin
from member.models import Member


class UserMemberMiddleware(MiddlewareMixin):
    def process_request(self, request, *args):
        ref_member = request.GET.get('ref')

        if ref_member is not None:
            member = Member.objects.get(mcode=ref_member)
            setattr(request, 'member', member)
            return
