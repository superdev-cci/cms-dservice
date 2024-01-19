from datetime import date, datetime

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from core.authentication.legacy import BasicAuthDefault
from core.filters.branch_old import BranchStatementFilter
from core.filters.statement import StatementDateTime
from core.report.pdf import InvoiceNormalPdf, InvoicePdfBlankTemplate
from ecommerce.functions import CheckDiscountQualified
from ecommerce.functions.analyze import SalePeriodTree
from ecommerce.report.sale import SaleItemSummaryReport, SaleSummaryReport, SummarySaleByMemberReport
from ecommerce.functions.calculate_shiping_box import calculate_box
from ..filter import BillTypeBackendFilter, BillStateBackendFilter, SendBackendFilter, BillGroupBackendFilter
from ..models import SaleInvoice
from ..report import SoldDailySummary, SoldMonthlySummary, SaleInvoiceForAccountingReport
from ..serializers import SaleInvoiceSerializer, ShippingBoxSerializer


class SalesSummaryView(viewsets.ModelViewSet):
    queryset = SaleInvoice.objects.all()
    serializer_class = SaleInvoiceSerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (
        SearchFilter, StatementDateTime, BranchStatementFilter, BillTypeBackendFilter, BillStateBackendFilter,
        SendBackendFilter, BillGroupBackendFilter)
    date_range_fields = ('sadate',)
    branch_field = 'inv_code'
    search_fields = ('sano', 'sadate', 'inv_code', 'mcode', 'name_t')
    group_field = 'online'

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

    @action(detail=False, methods=['GET'])
    def get_sales(self, request, *args, **kwargs):
        date = request.query_params.get('date', None)
        daily_sale = SoldDailySummary()
        month_sale = SoldMonthlySummary()
        return Response({
            'daily': daily_sale.daily_summary(date),
            'month': month_sale.monthly_summary
        }, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_sales_items(self, request, *args, **kwargs):
        dt = request.query_params.get('date', date.today().strftime('%Y-%m-%d'))
        instance = SaleItemSummaryReport(start=dt, end=dt, get_type='daily')
        return Response(instance.total_item, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], )
    def sales_report(self, request, *args, **kwargs):
        data = request.query_params
        period = data.get('period', 'daily')
        dt = data.get('date', date.today().strftime('%Y-%m-%d'))
        dt = datetime.strptime(dt, '%Y-%m-%d').date()
        if period == 'daily':
            start, end = SaleItemSummaryReport.get_month_range(dt)
            instance = SaleSummaryReport(start=start, end=end, get_type='daily')
        elif period in ('monthly', 'quarter'):
            start, end = SaleItemSummaryReport.get_year_range(dt)
            instance = SaleSummaryReport(start=start, end=end, get_type='monthly')
        else:
            Response(status.HTTP_400_BAD_REQUEST)
        result = instance.total
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def sales_items_report(self, request, *args, **kwargs):
        result = {}
        data = request.query_params
        period = data.get('period', None)
        dt = data.get('date', date.today().strftime('%Y-%m-%d'))
        dt = datetime.strptime(dt, '%Y-%m-%d').date()

        if 'start' in data and 'end' in data:
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

    @action(detail=False, methods=['GET'], permission_classes=(AllowAny,))
    def check_discount(self, request, *args, **kwargs):
        result = {}
        data = request.query_params
        mem_code = data.get('member', None)
        if mem_code is not None:
            result[mem_code] = CheckDiscountQualified(mem_code)
        else:
            result['message'] = 'bad request'
        return Response(result, status.HTTP_200_OK)

    @action(detail=True, methods=['GET'], permission_classes=(AllowAny,))
    def print(self, request, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(instance.bill_number)
        pdf = InvoicePdfBlankTemplate(instance.bill_number, data=instance)
        # pdf = InvoiceNormalPdf(instance.bill_number, data=instance)
        pdf.create_pdf(response=response)
        return response

    @action(detail=True, methods=['GET'], permission_classes=(AllowAny,))
    def preview(self, request, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(instance.bill_number)
        pdf = InvoiceNormalPdf(instance.bill_number, data=instance)
        pdf.create_pdf(response=response)
        return response

    @action(detail=False, methods=['GET'], )
    def get_sale_tree(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        member = request.query_params.get('m', None)
        depth = request.query_params.get('depth', 3)
        instance = SalePeriodTree(member=member, start=start, end=end)
        data = instance.process(int(depth))
        return Response(data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_summary_items_report(self, request, *args, **kwargs):
        dt = request.query_params.get('date', date.today().strftime('%Y-%m-%d'))
        sg = request.query_params.get('select_group', 'CCI')
        start, end = SaleItemSummaryReport.get_week_range(dt)
        instance = SaleItemSummaryReport(start=start, end=end, get_type='monthly', select_group=sg)
        return Response(instance.summary, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], )
    def summary_sales_by_member_report(self, request, *args, **kwargs):
        data = request.query_params
        dt = data.get('date', date.today().strftime('%Y-%m-%d'))
        dt = datetime.strptime(dt, '%Y-%m-%d').date()
        start, end = SaleItemSummaryReport.get_month_range(dt)
        instance = SummarySaleByMemberReport(start=start, end=end, get_type='monthly')
        result = instance.total
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel(self, request, *args, **kwargs):
        data = request.query_params
        dt = datetime.strptime(data.get('date', date.today().strftime('%Y-%m-%d')), '%Y-%m-%d').date()
        start, end = SaleItemSummaryReport.get_month_range(dt)
        branch = data.get('branch', None)
        excel = SaleInvoiceForAccountingReport(start=start, end=end, branch=branch)
        excel.process_data()
        response = HttpResponse(excel.response_file, content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['POST'], permission_classes=(AllowAny, ))
    def get_shipping_box(self, request, *args, **kwargs):
        data = request.data
        result, volume, weight = calculate_box(data)
        if result is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ShippingBoxSerializer(result)
        week_day = datetime.today().weekday()
        return Response(
            {
                "box": serializer.data,
                'volume': volume,
                'weight': weight,
                'week_day': week_day
            }
        )


