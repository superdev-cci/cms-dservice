from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication.legacy import BasicAuthDefault
from core.pagination import StandardResultsSetPagination, AdaptivePagination
from member.serializers import MemberSerializer
from ..serializers import MemberShortSerializer
from ..models import Member
from core.filters.member import MemberGroupFilter


class MemberFavorite(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberShortSerializer
    filter_backends = (MemberGroupFilter, OrderingFilter)
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination
    ordering_fields = ('mcode', 'name_t', 'mdate', 'mobile', 'level', 'honor')
    group_field = 'group'

    def list(self, request, *args, **kwargs):
        data = request.query_params
        ref_member = data.get('ref', None)
        search_key = data.get('q', '')
        try:
            top_member = Member.objects.get(mcode=ref_member)
            if search_key != '':
                favorite_queryset = top_member.favorite.filter(
                    Q(name_t__icontains=search_key) |
                    Q(mcode__icontains=search_key) |
                    Q(mobile__icontains=search_key),
                    Q(status_terminate=0))
            else:
                favorite_queryset = top_member.favorite.all()
            queryset = OrderingFilter().filter_queryset(self.request, favorite_queryset, self)
            page = self.paginate_queryset(queryset)
            if page is not None:
                favorite = [x.mcode for x in request.member.favorite.all()]
                context = self.get_serializer_context()
                context['favorite'] = favorite
                serializer = MemberSerializer(page, many=True, context=context)
                return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        data = request.data
        ref_member = data.get('ref', None)
        target = data.get('member', None)
        try:
            top_member = Member.objects.get(mcode=ref_member)
            target_member = Member.objects.get(mcode=target)
            query = top_member.favorite.filter(mcode=target_member)
            if len(query):
                return Response({
                    'reason': 'Already in list'
                }, status.HTTP_409_CONFLICT)

            if top_member.is_child(target_member):
                top_member.favorite.add(target_member)
                return Response({
                    'status': 'OK'
                }, status.HTTP_200_OK)
            else:
                return Response({
                    'reason': 'Invalid reference'
                }, status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['DELETE'])
    def remove_favourite(self, request, *args, **kwargs):
        data = request.query_params
        ref_member = data.get('ref', None)
        target = data.get('member', None)
        try:
            top_member = Member.objects.get(mcode=ref_member)
            target_member = Member.objects.get(mcode=target)
            target = top_member.favorite.get(mcode=target_member)
            top_member.favorite.remove(target)
            return Response({
                'status': 'OK'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'])
    def is_favourite(self, request, *args, **kwargs):
        data = request.query_params
        ref_member = data.get('ref', None)
        target = data.get('member', None)
        try:
            top_member = Member.objects.get(mcode=ref_member)
            target_member = Member.objects.get(mcode=target)
            if target_member.is_terminate:
                raise AttributeError('Member is terminate')
            query = top_member.favorite.filter(mcode=target_member)
            if len(query):
                return Response({
                    'status': True
                }, status.HTTP_200_OK)
            else:
                return Response({
                    'status': False
                }, status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_403_FORBIDDEN)
