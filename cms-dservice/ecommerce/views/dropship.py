from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import ProductSerializer
from ..models import Product
from ecommerce.functions import dropship as dropship_function
from member.models import Member
from member.serializers import MemberShortSerializer


class DropShipProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['post'])
    def calprices(self, request, *args, **kwargs):
        data = dropship_function.recal_prices(request.data)
        return Response(data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_ag(self, request, *args, **kwargs):
        data = request.query_params
        assert 'member' in data, 'Member code not defined'
        try:
            member = Member.objects.get(mcode=data['member'])
            serializer = MemberShortSerializer(member.agency_ref)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def ag_list(self, request, *args, **kwargs):
        data = request.query_params
        assert 'member' in data, 'Member code not defined'
        try:
            member = Member.objects.get(mcode=data['member'])
            if member.member_type == 'MB':
                queryset = Member.objects.filter(sponsor_lft__lt=member.sponsor_lft, sponsor_rgt__gt=member.sponsor_rgt,
                                                 sponsor_depth__lt=member.sponsor_depth, mtype1__in=[1, 2]).order_by(
                    '-sponsor_depth')
                serializer = MemberShortSerializer(queryset, many=True)
            else:
                return Response([], status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def add_ag(self, request, *args, **kwargs):
        data = request.data
        assert 'member' in data, 'Member code not defined'
        assert 'ag' in data, 'Agency code not defined'
        try:
            member = Member.objects.get(mcode=data['member'])
            queryset = Member.objects.filter(sponsor_lft__lt=member.sponsor_lft, sponsor_rgt__gt=member.sponsor_rgt,
                                             sponsor_depth__lt=member.sponsor_depth, mtype1__in=[1, 2]).order_by(
                '-sponsor_depth')
            all_code = [x.mcode for x in queryset]
            assert data['ag'] in all_code, 'Not Found'
            agency = Member.objects.get(mcode=data['ag'])
            member.agency_ref = agency
            member.save()
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def unset_ag(self, request, *args, **kwargs):
        data = request.data
        assert 'member' in data, 'Member code not defined'
        try:
            member = Member.objects.get(mcode=data['member'])
            member.agency_ref = None
            member.save()
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)
