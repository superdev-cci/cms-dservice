from datetime import date
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.mixin import MonthMixIn
from ..models import MonthCommission
from ..report import SummaryMonthCommission, ExcelSummaryMonthCommission
from ..serializers import MonthCommissionSerializer


class CommissionBReportView(viewsets.ModelViewSet):
    queryset = MonthCommission.objects.all()
    serializer_class = MonthCommissionSerializer

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
    def get_json(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        instance = SummaryMonthCommission(start=start, end=end, get_type=period, mcode=mem_code)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelSummaryMonthCommission(start=start, end=end, get_type=period, mcode=mem_code)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response