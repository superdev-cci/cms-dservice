from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Q, Window, F
from django.db.models.functions import RowNumber
from datetime import datetime, timedelta, date

from core.authentication import MemberTokenAuthentication
from core.pagination import StandardResultsSetPagination, AdaptivePagination
from member.serializers import MemberSerializer
from ..serializers import MemberShortSerializer, MemberStatusSerializer
from ..models import Member, MemberActive
from core.filters.member import MemberGroupFilter


class MemberMatrixView(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.none()
    serializer_class = MemberShortSerializer
    authentication_classes = (MemberTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination
    ordering_fields = ('mcode', 'name_t', 'mdate', 'mobile', 'level', 'honor', 'hpv')

    def list(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def active(self, request, *args, **kwargs):
        try:
            member = request.member
            last_active, add_new = MemberActive.objects.update_or_create(member=member.code, defaults={
                "member": member.code
            })
            if add_new is False:
                last_active.last_seen = datetime.now()
                last_active.save()
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_400_BAD_REQUEST)

        return Response({
            "status": 'OK'
        }, status.HTTP_200_OK)
