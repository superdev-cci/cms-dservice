from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from datetime import date, datetime

from commission.report.pv_activity_group_honor import PvActivityHonorGroupReport
from core.authentication.legacy import BasicAuthDefault
from ecommerce.functions.analyze import SalePeriodTree
from ecommerce.report import SoldItemMonthlySummary, SoldMonthlySummary, SoldMonthlyPaymentSummary
from ecommerce.report.excel.sale_item import MemberBoughtItemCodeSummaryExcel
from ecommerce.report.sale import AgFrBoughtSummaryReport, SaleItemSummaryReport
from ecommerce.report.summary import MemberBoughtItemSummary
from ecommerce.report.analyst.excel_analyst import ExcelSaleInvoiceAnalyst, ExcelSaleItemAnalyst
from ..serializers import SaleInvoiceSerializer, SaleItemSerializer
from ..models import SaleInvoice, SaleItem
from core.filters.branch_old import BranchStatementFilter
from core.filters.statement import StatementDateTime


class SalesAnalyzedView(viewsets.ModelViewSet):
    queryset = SaleInvoice.objects.all()
    serializer_class = SaleInvoiceSerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (StatementDateTime, BranchStatementFilter,)
    date_range_fields = ('sadate',)
    branch_field = 'inv_code'

    def retrieve(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['GET'], )
    def monthly_sales_item_report(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = SoldItemMonthlySummary(start=start, end=end)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'], )
    def sales_report(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = SoldMonthlySummary(start=start, end=end)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'], )
    def payment_report(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = SoldMonthlyPaymentSummary(start=start, end=end)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    # @action(detail=False, methods=['GET'], )
    # def agfr_report(self, request, *args, **kwargs):
    #     start = request.query_params.get('start', None)
    #     end = request.query_params.get('end', None)
    #     report = AgFrBoughtSummaryReport(start=start, end=end)
    #     return Response(report.total, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def sales_items_report(self, request, *args, **kwargs):
        result = {}
        data = request.query_params
        period = data.get('period', None)
        dt = data.get('date', date.today().strftime('%Y-%m-%d'))
        dt = datetime.strptime(dt, '%Y-%m-%d').date()
        if 'start' in data and 'end' in data:
            # start = data.get('start')
            # end = data.get('end')
            instance = SaleItemSummaryReport(get_type='monthly', **data.dict())
            result = instance.total
        elif period == 'daily':
            instance = SaleItemSummaryReport(start=dt, end=dt, get_type='daily')
            result = instance.total
        elif period == 'monthly':
            start, end = SaleItemSummaryReport.get_year_range(dt)
            instance = SaleItemSummaryReport(start=start, end=end, get_type='monthly')
            result = instance.total
        else:
            result['message'] = 'bad request'
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], )
    def get_sale_tree(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        member = request.query_params.get('m', None)
        depth = request.query_params.get('depth', 3)
        instance = SalePeriodTree(member=member, start=start, end=end)
        data = instance.process(int(depth))
        return Response(data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], )
    def sales_item_member(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        items = request.query_params.getlist('items')
        report_type = request.query_params.get('type', 'sale')
        if report_type == 'sale':
            report = MemberBoughtItemSummary(start=start, end=end, items=items, get_type='monthly')
            data, header, code = report.total
            return Response(data, status.HTTP_200_OK)
        else:
            report = MemberBoughtItemCodeSummaryExcel(start=start, end=end, items=items)
            report.process()
            response = HttpResponse(report.response_file,
                                    content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename={}'.format(report.file_name)
            return response

    @action(detail=False, methods=['GET'], )
    def pv_member(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        group = request.query_params.get('group')
        report = PvActivityHonorGroupReport(start=start, end=end, group=group, get_type='monthly')
        report.process()
        response = HttpResponse(report.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(report.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_excel_sale_invoice_analyst(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelSaleInvoiceAnalyst(start=start, end=end)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_excel_sale_item_analyst(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelSaleItemAnalyst(start=start, end=end)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response
