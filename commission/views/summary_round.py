from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.authentication.legacy import BasicAuthDefault
from ..models import WeekRound
from ..report import WeekRoundReport, MonthRoundReport
from ..serializers import WeekRoundSerializer


class SummaryRoundView(viewsets.ModelViewSet):
    queryset = WeekRound.objects.all()
    serializer_class = WeekRoundSerializer
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
    def week_round_report(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        instance = WeekRoundReport(start=start, end=end)
        return Response(instance.total, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def month_round_report(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        instance = MonthRoundReport(start=start, end=end)
        return Response(instance.total, status.HTTP_200_OK)