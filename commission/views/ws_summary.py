from datetime import datetime, timedelta, date

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication import MemberTokenAuthentication, URLTokenMemberAuthentication
from core.authentication.legacy import BasicAuthDefault
from ..models import WeakStrongSummary
from ..report.weak_strong import WeakStrongBalanceJsonReport, WeakStrongBalanceExcelReport
from ..serializers import WeakStrongSummarySerializer
from ..report import SummaryFastCommission


class WeakStrongSummaryView(viewsets.ModelViewSet):
    queryset = WeakStrongSummary.objects.all()
    serializer_class = WeakStrongSummarySerializer
    authentication_classes = (BasicAuthDefault, MemberTokenAuthentication)
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
    def get_summary(self, request, *args, **kwargs):
        period = request.query_params.get('period', 'monthly')
        try:
            member = request.member
            start = request.query_params.get('start', None)
            end = request.query_params.get('end', None)
            if start is None:
                end = datetime.today()
                start = end.replace(day=1, month=end.month - 1)

            instance = WeakStrongBalanceJsonReport(start=start, end=end, get_type=period, members=[member.code, ])
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_400_BAD_REQUEST)

        return Response({"result": instance.total[member.code]}, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], authentication_classes=(URLTokenMemberAuthentication,))
    def get_excel(self, request, *args, **kwargs):
        try:
            member = request.member
            start = request.query_params.get('start', None)
            end = request.query_params.get('end', None)
            if start is None:
                end = datetime.today()
                start = end.replace(day=1, month=end.month - 1)
            excel = WeakStrongBalanceExcelReport(start=start, end=end, members=[member.code, ])
            excel.process()
            response = HttpResponse(excel.response_file,
                                    content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
            return response
        except Exception as e:
            return Response({
                'reason': e.__str__()
            }, status.HTTP_400_BAD_REQUEST)
