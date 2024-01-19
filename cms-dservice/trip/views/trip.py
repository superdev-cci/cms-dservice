from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import datetime

from core.authentication import MemberTokenAuthentication
from core.authentication.legacy import BasicAuthDefault
from core.pagination import AdaptivePagination
from member.models import Member
from trip.functions.analyzed import TripEnrollAnalyzed
from ..serializers import TripSerializer, TripApplicationSerializer, TravelPointUseStatementSerializer, TravelPointUseStatementCreateSerializer
from ..models import Trip, TripApplication, TravelPointStack
from trip.functions import TripCalculator


class TripView(viewsets.ReadOnlyModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    pagination_class = AdaptivePagination
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['GET'])
    def get_enroll(self, request, *args, **kwargs):
        data = request.query_params
        trip_code = data.get('code', '')
        try:
            trip = TripApplication.objects.filter(trip__code=trip_code).select_related('member', 'trip')
            serializer = TripApplicationSerializer(trip, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response([], status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], authentication_classes=(MemberTokenAuthentication,))
    def get_available(self, request, *args, **kwargs):
        current_date = datetime.date.today()
        member = request.member
        calculator = TripCalculator(member, request=request)
        # result = calculator.find_current_trip(current_date)
        result = calculator.find_all_trip(current_date)
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], authentication_classes=(BasicAuthDefault,),
            permission_classes=(IsAuthenticated,))
    def analyzed(self, request, *args, **kwargs):
        data = request.query_params
        member = data.get('m')
        trip = data.get('trip')
        type = data.get('type', None)
        if type == '':
            type = None
        try:
            func = TripEnrollAnalyzed(member, trip, filter=type)
            response = func.create_tree()
        except Exception as e:
            return Response({'reason': e}, status.HTTP_400_BAD_REQUEST)

        return Response(response, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], authentication_classes=(BasicAuthDefault,),
            permission_classes=(IsAuthenticated,))
    def get_active_trip(self, request, *args, **kwargs):
        current_date = datetime.date.today()
        trip_query = Trip.objects.filter(start__lte=current_date, register_period__gte=current_date)
        serializer = TripSerializer(trip_query, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], authentication_classes=(BasicAuthDefault,),
            permission_classes=(IsAuthenticated,))
    def get_trip_enroll(self, request, *args, **kwargs):
        data = request.query_params
        ref_member = data.get('ref')
        member = data.get('m')
        trip = data.get('trip')
        try:
            top_member = Member.objects.get(mcode=ref_member)
            target_member = Member.objects.get(mcode=member)
            if top_member.is_child_or_self(target_member):
                func = TripEnrollAnalyzed(member, trip)
                return Response(func.calculate(), status.HTTP_200_OK)
            else:
                return Response({
                    'reason': 'Invalid reference'
                }, status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'], authentication_classes=(BasicAuthDefault,),
            permission_classes=(IsAuthenticated,))
    def get_trip_enroll_tree(self, request, *args, **kwargs):
        data = request.query_params
        ref_member = data.get('ref')
        member = data.get('m')
        trip = data.get('trip')
        depth = int(data.get('depth', 3))
        try:
            top_member = Member.objects.get(mcode=ref_member)
            target_member = Member.objects.get(mcode=member)
            if top_member.is_child_or_self(target_member):
                func = TripEnrollAnalyzed(member, trip, depth=depth)
                return Response(func.create_tree(), status.HTTP_200_OK)
            else:
                return Response({
                    'reason': 'Invalid reference'
                }, status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'], authentication_classes=(MemberTokenAuthentication,))
    def get_all_coin(self, request, *args, **kwargs):
        try:
            member = request.member
            data = {
                'gold': TravelPointStack.get_gold_coin(member),
                'silver': TravelPointStack.get_silver_coin(member),
            }
            return Response(data, status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "reason": "HTTP_401_UNAUTHORIZED",
                'message': str(e)
            }, status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['POST'], authentication_classes=(MemberTokenAuthentication,))
    def create_statement(self, request, *args, **kwargs):
        try:
            member = request.member
            if member is None:
                return Response({
                    "reason": "HTTP_401_UNAUTHORIZED",
                    'message': "Member not found"
                }, status.HTTP_401_UNAUTHORIZED)
            data = request.data
            new_instance = {
                "member": member.id,
                "trip": data['trip'],
                'state': 'CM',
                "gold_coin": data.get('gold', 0),
                "silver_coin": data.get('silver', 0)
            }
            serializer = TravelPointUseStatementCreateSerializer(data=new_instance)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                serializer = TravelPointUseStatementSerializer(instance)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "reason": "HTTP_401_UNAUTHORIZED",
                'message': str(e)
            }, status.HTTP_401_UNAUTHORIZED)
