from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication.legacy import BasicAuthDefault
from ..filter import PaidStateBackendFilter
from ..models import WeekPayment
from ..report import ExcelWeekPayment
from ..serializers import WeekPaymentSerializer


class WeekPaymentView(viewsets.ModelViewSet):
    queryset = WeekPayment.objects.all()
    serializer_class = WeekPaymentSerializer
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, PaidStateBackendFilter)
    search_fields = ('mcode', 'date_start', 'date_issue', 'name_t', 'mobile')

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

    @action(detail=False, methods=['GET'])
    def get_excel_week_payment(self, request, *args, **kwargs):
        mem_code = request.query_params.get('mcode', None)
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        excel = ExcelWeekPayment(start=start, end=end, mcode=mem_code)
        excel.process_data()
        response = HttpResponse(excel.response_file,
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response
