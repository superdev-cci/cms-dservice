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
from ..models import Member
from core.filters.member import MemberGroupFilter


class MemberStatusView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberShortSerializer
    filter_backends = (MemberGroupFilter, OrderingFilter)
    authentication_classes = (MemberTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination
    ordering_fields = ('mcode', 'name_t', 'mdate', 'mobile', 'level', 'honor', 'hpv')
    group_field = 'group'

    def list(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def get_status(self, request, *args, **kwargs):
        try:
            member = request.member
            context = self.get_serializer_context()
            serializer = MemberStatusSerializer(member, context=context)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_400_BAD_REQUEST)

