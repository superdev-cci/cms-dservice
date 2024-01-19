from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.report.pdf.transfer_hq import InvoiceTransferHqPdf
from ..serializers import BranchTransferHqSerializer
from ..models import BranchTransferHq
from ecommerce.functions import dropship as dropship_function


class BranchTransferHqView(viewsets.ReadOnlyModelViewSet):
    queryset = BranchTransferHq.objects.all()\
        # .prefetch_related(
        #     Prefetch('stockadjustitem_set', queryset=StockAdjustItem.objects.select_related('product')))
    serializer_class = BranchTransferHqSerializer

    # def list(self, request, *args, **kwargs):
    #     return Response(status.HTTP_403_FORBIDDEN)

    # @action(detail=False, methods=['post'])
    # def calprices(self, request, *args, **kwargs):
    #     data = dropship_function.recal_prices(request.data)
    #     return Response(data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_pdf(self, request, *args, **kwargs):
        bill_number = request.query_params['bill_number']
        instance = self.filter_queryset(self.get_queryset()).get(sano=bill_number)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(instance.bill_number)
        pdf = InvoiceTransferHqPdf(instance.bill_number, data=instance)
        pdf.create_pdf(response=response)
        return response

    @action(detail=True, methods=['GET'])
    def print(self, request, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(instance.bill_number)
        pdf = InvoiceTransferHqPdf(instance.bill_number, data=instance)
        pdf.create_pdf(response=response)
        return response
