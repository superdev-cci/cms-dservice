from datetime import datetime, timedelta, date

from django.db.models import Sum
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.authentication.legacy import BasicAuthDefault
from ..models import HonorChangeLog
from ..serializers import HonorChangeLogSerializer
# from ..report import SummaryFastCommission


class HonorChangeLogView(viewsets.ModelViewSet):
    queryset = HonorChangeLog.objects.all()
    serializer_class = HonorChangeLogSerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)

    # def list(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    # @action(detail=False, methods=['GET'])
    # def get_summary(self, request, *args, **kwargs):
    #     period = request.query_params.get('period', 'monthly')
    #     mem_code = request.query_params.get('mcode', None)
    #     start = request.query_params.get('start', None)
    #     end = request.query_params.get('end', None)
    #     instance = SummaryFastCommission(start=start, end=end, get_type=period, mcode=mem_code)
    #     return Response(instance.total, status.HTTP_200_OK)