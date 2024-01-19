import datetime
from dateutil import relativedelta
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication import MemberTokenAuthentication
from core.pagination import AdaptivePagination
from ..serializers import AchievementSerializer, OnlineCertAchievementSerializer
from ..models import Achievement, Member
from django.db.models import Q


class AchievementView(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    authentication_classes = (OAuth2Authentication, MemberTokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination
    ordering_fields = ('stamp_date', 'name', 'code')
    search_fields = ('name', 'code', 'stamp_date', 'status')

    # def list(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    # def retrieve(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    # def create(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    # def update(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    # def destroy(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def get_detail(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('mcode', None)
        try:
            queryset = Achievement.objects.get(member__mcode=mem_code)
            result = AchievementSerializer(queryset).data
        except Achievement.DoesNotExist:
            result = {}
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def create_online_cert(self, request, *args, **kwargs):
        user = request.user.useraccount
        try:
            instance = Achievement.objects.create(member=user.member, code='OC', note="OC")
            member = user.member
            Member.objects.filter(mcode=member.code).update(ocert=1)
            result = OnlineCertAchievementSerializer(instance=instance).data
        except Achievement.DoesNotExist:
            result = {}
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def get_online_cert(self, request, *args, **kwargs):
        if hasattr(request, 'member'):
            member = request.member
        else:
            user = request.user.useraccount
            member = user.member
        try:
            queryset = Achievement.objects.filter(member__mcode=member.code, code='OC').last()
            result = OnlineCertAchievementSerializer(queryset).data
        except Achievement.DoesNotExist:
            result = {}
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def check_info(self, request, *args, **kwargs):
        user = request.user.useraccount
        member = user.member
        if member.line_id == '' and member.mobile == '':
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)

    @action(detail=False, methods=['PUT', ])
    def update_member_info(self, request, *args, **kwargs):
        user = request.user.useraccount
        member = user.member
        data = request.data
        try:
            queryset = Member.objects.filter(mobile=data['mobile'], status_terminate=0).filter(~Q(mcode=member.code))
            assert len(queryset) is 0, 'CODE0'
            queryset = Member.objects.filter(line_id=data['line'], status_terminate=0).filter(~Q(mcode=member.code))
            assert len(queryset) is 0, 'CODE1'
            # queryset = Member.objects.filter(facebook_name=data['facebook']).filter(~Q(mcode=member.code))
            # assert len(queryset) is 0, 'CODE2'
            Member.objects.filter(mcode=member.code).update(mobile=data['mobile'], line_id=data['line'],
                                                            facebook_name=data['facebook'])
        except Exception as e:
            return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
