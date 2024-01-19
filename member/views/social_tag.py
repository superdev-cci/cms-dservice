from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication import MemberTokenAuthentication
from core.authentication.legacy import BasicAuthDefault
from core.pagination import AdaptivePagination
from ..models import MemberSocialTagConfig, Member
from ..serializers import MemberSocialTagConfigSerializer


class MemberSocialTagConfigView(viewsets.ModelViewSet):
    queryset = MemberSocialTagConfig.objects.all()
    serializer_class = MemberSocialTagConfigSerializer
    filter_backends = (SearchFilter,)
    authentication_classes = (MemberTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'], )
    def get_info(self, request, *args, **kwargs):
        try:
            member = request.member
            if hasattr(member, "membersocialtagconfig") is False:
                instance = MemberSocialTagConfig.objects.create(member=member)
            else:
                instance = member.membersocialtagconfig
            serializer = MemberSocialTagConfigSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            result = {}
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'], authentication_classes=(BasicAuthDefault,))
    def get_tag(self, request, *args, **kwargs):
        try:
            mem_code = request.query_params.get('mcode', None)
            if mem_code is not None:
                mem_code = mem_code.upper()
            member = Member.objects.get(mcode=mem_code)
            if hasattr(member, "membersocialtagconfig") is False:
                instance = MemberSocialTagConfig.objects.create(member=member)
            else:
                instance = member.membersocialtagconfig
            serializer = MemberSocialTagConfigSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            result = {}
        return Response(status=status.HTTP_404_NOT_FOUND)
