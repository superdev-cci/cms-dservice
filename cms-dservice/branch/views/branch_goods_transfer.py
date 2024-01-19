from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from accounting.models import StatementState
from core.filters import StatementDateTime, BranchStatementFilter
from core.pagination import StandardResultsSetPagination
from ..functions import update_stock
from ..models import BranchGoodsImportStatement, \
    BranchGoodsExportStatement
from ..serializers import BranchGoodsImportStatementSerializer, BranchGoodsExportStatementSerializer


class BranchImportStatementView(viewsets.ModelViewSet):
    queryset = BranchGoodsImportStatement.objects.all().select_related('statement_type', 'statement_state', 'branch', 'from_branch')
    serializer_class = BranchGoodsImportStatementSerializer
    # authentication_classes = (BasicAuthDefault,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter, StatementDateTime, BranchStatementFilter)
    date_range_fields = ('date_issue',)
    branch_field = 'from_branch'
    # product_field = 'pcode'
    search_fields = ('seller_name', 'bill_number', 'statement_type', 'statement_state')

    @action(detail=True, methods=['PUT'])
    def receive_goods(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.statement_state.code in ('DP', 'OR', 'PD'):
            instance.statement_state = StatementState.objects.get(code='CM')
            update_stock(instance, 'receive', 'import_statement')
            instance.save()
            return Response(BranchGoodsImportStatementSerializer(instance).data, status.HTTP_200_OK)
        return Response({'reason': 'Invalid statement state'}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['PUT'])
    def reject_goods(self, request, *args, **kwargs):
        # This api not available for now
        # instance = self.get_object()
        # obj_list = update_stock(instance, 'reject', 'import_statement')
        # instance.statement_state = StatementState.objects.get(code='RJ')
        # instance.save()
        # return Response(BranchGoodsImportStatementSerializer(instance).data, status.HTTP_200_OK)
        return Response({'reason': 'This api not available for now'}, status=status.HTTP_403_FORBIDDEN)

    # @action(detail=False, methods=['GET'])
    # def get_excel(self, request, *args, **kwargs):
    #     excel = ExcelStockMovement(**kwargs)
    #     excel.process_data()
    #     return Response({'result': excel.save_file()}, status.HTTP_200_OK)


class BranchExportStatementView(viewsets.ModelViewSet):
    queryset = BranchGoodsExportStatement.objects.all().select_related('statement_type', 'statement_state', 'branch', 'to_branch')
    serializer_class = BranchGoodsExportStatementSerializer
    # authentication_classes = (BasicAuthDefault,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter, StatementDateTime, BranchStatementFilter)
    date_range_fields = ('date_issue',)
    branch_field = 'to_branch'
    # product_field = 'pcode'
    search_fields = ('seller_name', 'bill_number', 'statement_type', 'statement_state')

    @action(detail=True, methods=['GET'])
    def send_goods(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.statement_state.code in ('OR', 'PD'):
            update_stock(instance, 'send', 'export_statement')
            # instance.statement_state = StatementState.objects.get(code='DP')
            # instance.save()
            return Response(BranchGoodsExportStatementSerializer(instance).data, status.HTTP_200_OK)
        return Response({'reason': 'Invalid statement state'}, status=status.HTTP_403_FORBIDDEN)
    # @action(detail=True, methods=['GET'])
    # def receive_goods(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     obj_list = update_stock(instance, 'receive', 'export_statement')
    #     instance.statement_state = StatementState.objects.get(code='CM')
    #     instance.save()
    #     return Response(BranchGoodsExportStatementSerializer(instance).data, status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def reject_goods(self, request, *args, **kwargs):
        instance = self.get_object()
        obj_list = update_stock(instance, 'reject', 'export_statement')
        instance.statement_state = StatementState.objects.get(code='RJ')
        instance.save()
        return Response(BranchGoodsExportStatementSerializer(instance).data, status.HTTP_200_OK)
