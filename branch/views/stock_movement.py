from django.db.models import Prefetch, Q
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication.legacy import BasicAuthDefault
from core.pagination import StandardResultsSetPagination
from core.report.pdf.stock_adjust import StockAdjustPdf
from core.filters import StatementDateTime, BranchStatementFilter, ProductFilter
from core.mixin import MonthMixIn
from ..serializers import StockMovementSerializer
from ..models import StockStatement
from ..report import ExcelStockMovement, ExcelSummaryStockMovement
from ecommerce.functions import dropship as dropship_function
from datetime import date


class StockMovementView(viewsets.ModelViewSet):
    queryset = StockStatement.objects.filter(~Q(pcode__in=('D001',))).all()
    serializer_class = StockMovementSerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter, StatementDateTime, BranchStatementFilter, ProductFilter)
    date_range_fields = ('date_issue',)
    branch_field = 'to_branch'
    product_field = 'pcode'
    search_fields = ('client_code', 'client_name', 'bill_number')

    @action(detail=False, methods=['GET'])
    def get_pdf(self, request, *args, **kwargs):
        bill_number = request.query_params['bill_number']
        instance = self.filter_queryset(self.get_queryset()).get(bill_number=bill_number)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(instance.bill_number)
        pdf = StockAdjustPdf(instance.bill_number, data=instance)
        pdf.create_pdf(response=response)
        return response

    @action(detail=True, methods=['GET'])
    def print(self, request, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(instance.bill_number)
        pdf = StockAdjustPdf(instance.bill_number, data=instance)
        pdf.create_pdf(response=response)
        return response

    @action(detail=False, methods=['GET'])
    def get_excel(self, request, *args, **kwargs):
        end = request.query_params.get('end', None)
        start = request.query_params.get('start', None)
        product = request.query_params.get('product', None)
        branch = request.query_params.get('branch', None)
        excel = ExcelStockMovement(end=end, start=start, product=product, branch=branch)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_summary_stock_movement_excel(self, request, *args, **kwargs):
        idate = request.query_params.get('date', date.today())
        start, end = MonthMixIn.get_month_range(idate)
        branch = request.query_params.get('branch', None)
        excel = ExcelSummaryStockMovement(end=end, start=start, branch=branch)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response
