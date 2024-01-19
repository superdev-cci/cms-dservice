from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Q
from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter
from datetime import datetime, timedelta, date

from core.authentication.legacy import BasicAuthDefault
from ..serializers import WeakStrongCurrentRoundStackSerializer
from ..models import WeakStrongCurrentRoundStack
from ..functions import StampPvRound


class WeakStrongCurrentRoundView(viewsets.ModelViewSet):
    queryset = WeakStrongCurrentRoundStack.objects.all()
    serializer_class = WeakStrongCurrentRoundStackSerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)

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
    def get_round_pv_member(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('mcode', None)
        obj = StampPvRound(mem_code)
        result = {
            'all_pv': obj.all_pv,
            'left': WeakStrongCurrentRoundStackSerializer(obj.left_detail, many=True).data,
            'right': WeakStrongCurrentRoundStackSerializer(obj.right_detail, many=True).data,
        }
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def create_stamp_pv_round(self, request, *args, **kwargs):
        query_params = request.data
        qs = StampPvRound.create_stamp_pv(query_params['bill_number'], query_params['mcode'], query_params['pv'])
        result = WeakStrongCurrentRoundStackSerializer(qs, many=True).data
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['DELETE'])
    def delete_stamp_pv_round(self, request, *args, **kwargs):
        StampPvRound.delete_stamp_pv(request.data['bill_number'])
        return Response("Delete Successful", status.HTTP_200_OK)