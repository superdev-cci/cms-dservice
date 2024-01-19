from datetime import date, datetime

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from commission.functions.analyze import TransferPvPeriodTree
from commission.functions.analyze.weak_team_commission import WeakTeamTree
from member.report.analyst.sponsor_tree_analyst import PvTransferInSponsorTree
from commission.report import SummaryPVTransferByMemberReport
from commission.report.pv_transfer_analyst.excel_analyst import ExcelSummaryPvTransferInOutAnalyst, \
    ExcelPvTransferInnerOuterAnalyst, ExcelSummaryPvTransferAnalyst
from core.authentication.legacy import BasicAuthDefault
from ecommerce.report.sale import SaleItemSummaryReport
from ..models import PvTransfer
from ..serializers import PvTransferSerializer


class OrgScanPvView(viewsets.ModelViewSet):
    queryset = PvTransfer.objects.all()
    serializer_class = PvTransferSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthDefault,)

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

    @action(detail=False, methods=['GET'],)
    def get_transfer_tree(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        member = request.query_params.get('m', None)
        depth = request.query_params.get('depth', 5)
        instance = TransferPvPeriodTree(member=member, start=start, end=end)
        data = instance.process(int(depth))
        return Response(data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_ws_tree(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        member = request.query_params.get('m', None)
        depth = request.query_params.get('depth', 5)
        instance = WeakTeamTree(member=member, start=start, end=end)
        data = instance.process(int(depth))
        return Response(data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], )
    def summary_pvtransfer_by_member_report(self, request, *args, **kwargs):
        data = request.query_params
        dt = data.get('date', date.today().strftime('%Y-%m-%d'))
        dt = datetime.strptime(dt, '%Y-%m-%d').date()
        start, end = SaleItemSummaryReport.get_month_range(dt)
        instance = SummaryPVTransferByMemberReport(start=start, end=end, get_type='monthly')
        result = instance.total
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel_summary_in_out_pv_transfer_analyst(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelSummaryPvTransferInOutAnalyst(start=start, end=end, get_type=period)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_excel_in_out_pv_transfer_analyst(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelPvTransferInnerOuterAnalyst(start=start, end=end, get_type=period)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_excel_pv_transfer_analyst(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelSummaryPvTransferAnalyst(start=start, end=end, get_type=period)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_pv_transfer_sponsor_tree(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        member = request.query_params.get('m', None)
        depth = request.query_params.get('depth', 3)
        instance = PvTransferInSponsorTree(member=member, start=start, end=end)
        data = instance.process(int(depth))
        return Response(data, status.HTTP_200_OK)

