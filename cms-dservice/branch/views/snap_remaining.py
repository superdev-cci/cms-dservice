from datetime import date

from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from core.mixin import MonthMixIn
from ..models import BranchGoodsSnapRemainingStatement, BranchGoodsSnapRemainingItem
from ..report import SnapRemainingPdf, ExcelSnapRemaining
from ..serializers import BranchGoodsSnapRemainingStatementSerializer


class SnapRemainingView(viewsets.ReadOnlyModelViewSet):
    queryset = BranchGoodsSnapRemainingStatement.objects.all().prefetch_related(
            Prefetch('items', queryset=BranchGoodsSnapRemainingItem.objects.select_related('product')))
    serializer_class = BranchGoodsSnapRemainingStatementSerializer

    @action(detail=False, methods=['GET'])
    def get_pdf(self, request, *args, **kwargs):
        idate = request.query_params.get('date', date.today().strftime('%Y-%m-%d'))
        branch = request.query_params.get('branch', 'STHQ')
        instance = self.filter_queryset(self.get_queryset()).get(branch__inv_code=branch, date_issue=idate)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(instance.bill_number)
        pdf = SnapRemainingPdf(instance.bill_number, data=instance)
        pdf.create_pdf(response=response)
        return response

    @action(detail=False, methods=['GET'])
    def get_excel(self, request, *args, **kwargs):
        idate = request.query_params.get('date', date.today())
        start, end = MonthMixIn.get_month_range(idate)
        branch = request.query_params.get('branch', None)
        excel = ExcelSnapRemaining(end=end, start=start, branch=branch)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

