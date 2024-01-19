from datetime import datetime, timedelta, date

from django.db.models import Sum
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.authentication.legacy import BasicAuthDefault
from ..functions import HoldExpirePvStack
from ..models import HoldPvStack
from ..report import PvActivityReport, SummaryCommission, ExcelSummaryCommission, SummaryWeekCommission, \
    ExcelSummaryWeekCommission, SummaryMonthCommission, ExcelSummaryMonthCommission, SummaryWeakStrong, \
    ExcelSummaryWeakStrong, GroupCommission, GroupPvTransfer
from ..serializers import HoldPvStackSerializer
from commission.report.ws_commission_analyst.excel_analyst import ExcelWSBonusAnalyst


class CommissionReportView(viewsets.ModelViewSet):
    queryset = HoldPvStack.objects.all()
    serializer_class = HoldPvStackSerializer
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
    def holdpv(self, request, *args, **kwargs):
        result = {}
        tmp = HoldPvStack.objects.all().aggregate(Sum('remaining'))
        result['hold_pv'] = tmp['remaining__sum']
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def holdpv_activity(self, request, *args, **kwargs):
        data = request.query_params
        period = data.get('period', 'daily')
        mem_code = data.get('mcode', None)
        end = data.get('end', date.today().strftime('%Y-%m-%d'))
        end = datetime.strptime(end, '%Y-%m-%d').date()
        start = data.get('start', None)

        if start:
            start = datetime.strptime(start, '%Y-%m-%d').date()
            if period == 'daily':
                instance = PvActivityReport(start=start, end=end, get_type='daily', mem_code=mem_code)
            elif period in ('monthly', 'quarter'):
                instance = PvActivityReport(start=start, end=end, get_type='monthly', mem_code=mem_code)
            else:
                Response(status.HTTP_400_BAD_REQUEST)
        else:
            if period == 'daily':
                start = end - timedelta(6)
                instance = PvActivityReport(start=start, end=end, get_type='daily', mem_code=mem_code)
            elif period in ('monthly', 'quarter'):
                start, end = PvActivityReport.get_year_range(end)
                instance = PvActivityReport(start=start, end=end, get_type='monthly', mem_code=mem_code)
            else:
                Response(status.HTTP_400_BAD_REQUEST)

        result = instance.result
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_hold_pv_member(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('mcode', None)
        result = {}
        tmp = HoldPvStack.objects.filter(member__mcode=mem_code).aggregate(Sum('remaining'))
        result['hold_pv'] = tmp['remaining__sum']
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_member_stack(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('mcode', None)
        stack = HoldExpirePvStack(mem_code)
        qs = stack.display_available_pv()
        result = HoldPvStackSerializer(qs, many=True).data
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_summary(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        instance = SummaryCommission(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel_summary(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        excel = ExcelSummaryCommission(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_summary_commission_a(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        instance = SummaryWeekCommission(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel_commission_a(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        excel = ExcelSummaryWeekCommission(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_summary_commission_b(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        instance = SummaryMonthCommission(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel_commission_b(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        excel = ExcelSummaryMonthCommission(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_summary_weak_strong(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        instance = SummaryWeakStrong(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel_summary_weak_strong(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        honor = request.query_params.getlist('honor', [])
        excel = ExcelSummaryWeakStrong(start=start, end=end, get_type=period, mcode=mem_code, honor=honor)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'])
    def get_group_commission_report(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'daily')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        instance = GroupCommission(start=start, end=end, get_type=period, mcode=mem_code)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_group_pv_transfer_report(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'daily')
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        instance = GroupPvTransfer(start=start, end=end, get_type=period, mcode=mem_code)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_excel_ws_bonus_analyst(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelWSBonusAnalyst(start=start, end=end, get_type=period)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response
