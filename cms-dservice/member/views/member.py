import random
import os
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Count, Q, Window, F
from django.db.models.functions import RowNumber
from datetime import datetime, timedelta, date
from django.http import Http404, FileResponse, HttpResponse
from django.conf import settings

from core.authentication.legacy import BasicAuthDefault
from core.utility.save_image import create_image_pdf
from core.pagination import StandardResultsSetPagination, AdaptivePagination
from member.serializers import MemberSerializer
from ..serializers import MemberShortSerializer, MemberChildSerializer, MemberDashboardSerializer, \
    MemberWithTreeSerializer, MemberSponsorSerializer
from ..models import Member
from core.filters.member import MemberGroupFilter, MemberHonorFilter, MemberLevelFilter
from ..filter import MemberBusinessTypeFilter, TerminateBackendFilter, SuspendBackendFilter
from ..report.analyst.excel_child_report import ExcelChildActivityAnalyst
from ..report.pandas.sponsor_analyst import ExcelDataFrameSponsorChild
from openpyxl.writer.excel import save_virtual_workbook


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberShortSerializer
    filter_backends = (
        SearchFilter, MemberGroupFilter, MemberBusinessTypeFilter, MemberHonorFilter, MemberLevelFilter,
        OrderingFilter, TerminateBackendFilter, SuspendBackendFilter)
    authentication_classes = (BasicAuthDefault,)
    permission_classes = (IsAuthenticated,)
    pagination_class = AdaptivePagination
    ordering_fields = ('mcode', 'name_t', 'mdate', 'mobile', 'level', 'honor', 'hpv')
    search_fields = ('mcode', 'name_t', 'mobile', 'id', 'id_card', 'email')
    group_field = 'group'

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
    def get_detail(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('mcode', None)
        try:
            queryset = Member.objects.get(mcode=mem_code)
            result = MemberShortSerializer(queryset).data
        except Member.DoesNotExist:
            result = {}
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_members(self, request, *args, **kwargs):
        result = {
            'members_each_level': list(Member.objects.values('level').order_by().annotate(num=Count('level')).annotate(
                active=Count('level', filter=Q(status_terminate=0)))),
            'members_each_honor': list(Member.objects.values('honor').order_by().annotate(num=Count('honor')).annotate(
                active=Count('level', filter=Q(status_terminate=0))))
        }
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def search(self, request, *args, **kwargs):
        data = request.query_params
        target = data.get('ref', None)
        search_key = data.get('q', None)
        try:
            instance = Member.objects.get(mcode=target)
            queryset = instance.down_lines.filter(
                Q(name_t__icontains=search_key) |
                Q(mcode__icontains=search_key) |
                Q(mobile__icontains=search_key),
                Q(status_terminate=0)
            )[0:5]
            result = MemberChildSerializer(queryset, many=True).data
        except Member.DoesNotExist:
            result = {}
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def children(self, request, *args, **kwargs):
        result = {}
        data = request.query_params
        search_key = data.get('q', '')
        try:
            queryset = request.member.down_lines.filter(status_terminate=0)
            if search_key != '':
                queryset = queryset.filter(
                    Q(name_t__icontains=search_key) |
                    Q(mcode__icontains=search_key) |
                    Q(mobile__icontains=search_key)
                )
            queryset = OrderingFilter().filter_queryset(self.request, queryset, self)
            page = self.paginate_queryset(queryset)
            if page is not None:
                favorite = [x.mcode for x in request.member.favorite.all()]
                context = self.get_serializer_context()
                context['favorite'] = favorite
                context['head_member'] = request.member
                serializer = MemberSerializer(page, many=True, context=context)
                return self.get_paginated_response(serializer.data)
        except Member.DoesNotExist:
            result = {}
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def empty_upline(self, request, *args, **kwargs):
        queryset = Member.objects.filter(upa_code='')
        page = self.paginate_queryset(queryset)
        context = self.get_serializer_context()
        serializer = MemberSerializer(page, many=True, context=context)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['GET'])
    def empty_sponsor(self, request, *args, **kwargs):
        queryset = Member.objects.filter(sp_code='')
        page = self.paginate_queryset(queryset)
        context = self.get_serializer_context()
        serializer = MemberSerializer(page, many=True, context=context)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['GET'])
    def dashboard(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('mcode', None)
        try:
            instance = Member.objects.get(mcode=mem_code)
            result = MemberDashboardSerializer(instance).data
        except Member.DoesNotExist:
            result = {}
        return Response(result, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_tree(self, request, *args, **kwargs):
        data = request.query_params
        mem_code = data.get('mcode', None)
        try:
            instance = Member.objects.get(mcode=mem_code)
            serializer = MemberWithTreeSerializer(instance, context={'request': request})
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_random_code(self, request, *args, **kwargs):
        assert 'nation' in request.query_params, KeyError('nation must be in query')
        nation = request.query_params['nation']
        is_process = True
        start_time = datetime.now()

        def try_get_code():
            items = []
            for x in range(1, 20):
                items.append('{}{:07}'.format(nation, random.randrange(1, 9999999)))
            match = [x.code for x in Member.objects.filter(mcode__in=items)]
            available = list(set(items) - set(match))
            if len(available):
                return available[0]
            return None

        while is_process:
            mcode = try_get_code()
            if mcode is not None:
                is_process = False
            diff = datetime.now() - start_time
            if diff.seconds >= 60:
                raise RecursionError('Time out')

        if 'customer' in request.query_params:
            mcode = 'M{}'.format(nation, mcode[2:])

        return Response({'code': mcode}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def check_code(self, request, *args, **kwargs):
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                pass

            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except (TypeError, ValueError):
                pass

        assert 'mcode' in request.query_params, KeyError('code must be in query')
        mcode = request.query_params['mcode']
        if not is_number(mcode[-6:]):
            return Response({'result': 'fail'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        cnt = Member.objects.filter(mcode=mcode).count()
        if cnt:
            return Response({'result': 'fail'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({'code': mcode}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def check_id_card(self, request, *args, **kwargs):
        # assert 'nation' in request.query_params, KeyError('nation must be in query')
        assert 'id_card' in request.query_params, KeyError('id_card must be in query')
        # nation = request.query_params['nation']
        id_card = request.query_params['id_card']
        is_exist = Member.objects.filter(id_card=id_card).count()
        if is_exist:
            return Response({
                "result": False,
                "reason": "This id card/passport already used !!!"
            }, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({
                "result": True,
                "reason": "This id card/passport can use"
            }, status=status.HTTP_200_OK)

        # if nation != 'TH':
        #     return Response({
        #         "result": True,
        #         "reason": "This passport can use"
        #     }, status=status.HTTP_200_OK)
        # else:
        #     if Member.verify_id_card(id_card) is False:
        #         return Response({'result': 'fail'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        #     return Response({
        #         "result": True,
        #         "reason": "This id card can use"
        #     }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_doc(self, request, *args, **kwargs):
        mem_code = request.query_params.get('mcode', None)
        file_type = request.query_params.get('file_type')
        dir_root = os.path.join(settings.MEDIA_ROOT, "document")

        try:
            # if self.request.mirror is False:
            #     return Response({'detail': 'file not found'}, status=status.HTTP_400_BAD_REQUEST)
            instance = Member.objects.get(mcode=mem_code)
            if file_type == 'id_card':
                dir_root = os.path.join(dir_root, "id_card")
                file_path = '{}/{}.pdf'.format(dir_root, instance.mcode)
                response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename={}_id_card.pdf'.format(instance.mcode)
                # if instance.document.get('id_read_count', 0) == 0:
                #     instance.document['id_read_count'] = 0
                # else:
                #     instance.document['id_read_count'] += 1
            elif file_type == 'bank':
                dir_root = os.path.join(dir_root, "bank")
                file_path = '{}/{}.pdf'.format(dir_root, instance.code)
                response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename={}_bank.pdf'.format(instance.code)
                # if instance.document.get('bank_read_count', 0) == 0:
                #     instance.document['bank_read_count'] = 0
                # else:
                #     instance.document['bank_read_count'] += 1
            else:
                raise Exception('not fount')

            return response

        except Exception as e:
            return Response({'detail': 'file not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'])
    def upload_doc(self, request, *args, **kwargs):
        upload_type = request.query_params.get('upload_type')
        dir_root = os.path.join(settings.MEDIA_ROOT, "document")
        mem_code = request.query_params.get('mcode', None)
        instance = Member.objects.get(mcode=mem_code)
        file = request.FILES['file']
        if upload_type == 'id_card':
            dir_root = os.path.join(dir_root, "id_card")
            create_image_pdf(dir_root, file, instance.mcode)
            instance.id_card_img = dir_root + file.name
            instance.id_card_img_date = datetime.now()
        elif upload_type == 'bank':
            dir_root = os.path.join(dir_root, "bank")
            create_image_pdf(dir_root, file, instance.mcode)
            instance.acc_no_img = dir_root + file.name
            instance.acc_no_img_date = datetime.now()
        else:
            return Response({'detail': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
        instance.save()
        return Response({'result': 'success'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['GET'])
    def verify_sponsor(self, request, *args, **kwargs):
        mem_code = request.query_params.get('mcode', None)
        try:
            instance = Member.objects.get(mcode=mem_code)
            if instance.level == 'MB':
                return Response({
                    "code": mem_code,
                    "name": instance.name_t,
                    "result": False,
                    "reason": mem_code + " is a MB level can't use as a sponsor"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "code": mem_code,
                    "name": instance.name_t,
                    "result": True,
                    "reason": mem_code + " is a " + instance.level + " level can use as a sponsor"
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def check_tax_number(self, request, *args, **kwargs):
        assert 'tax' in request.query_params, KeyError('tax must be in query')
        tax = request.query_params.get('tax', None)
        is_exist = Member.objects.filter(id_tax=tax)
        if is_exist:
            return Response({'result': tax + " already use"}, status=status.HTTP_200_OK)
        else:
            return Response({'result': "you can use this tax number: " + tax}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def check_mobile(self, request, *args, **kwargs):
        assert 'mobile' in request.query_params, KeyError('mobile must be in query')
        mb_req = request.query_params.get('mobile', None)
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        mb_save = ""
        for ch in mb_req:
            if ch in num_list:
                mb_save += ch
        is_exist = Member.objects.filter(mobile=mb_save)
        if is_exist:
            return Response({'result': mb_save + " already use"}, status=status.HTTP_200_OK)
        else:
            return Response({'result': "you can use this mobile number: " + mb_save}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_sponsor_report(self, request, *args, **kwargs):
        assert 'sp_code' in request.query_params, KeyError('sp_code must be in query')
        sponsor_code = request.query_params.get('sp_code', None)
        try:
            instance = Member.objects.get(mcode=sponsor_code)
            result = MemberSponsorSerializer(Member.objects.filter(sp_code=instance.mcode), many=True).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def get_upline_report(self, request, *args, **kwargs):
        assert 'upa_code' in request.query_params, KeyError('upa_code must be in query')
        upline_code = request.query_params.get('upa_code', None)
        try:
            instance = Member.objects.get(mcode=upline_code)
            result = MemberSponsorSerializer(Member.objects.filter(upa_code=instance.mcode), many=True).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'], permission_classes=(IsAuthenticated,))
    def export_sponsor_tree_activity_excel(self, request, *args, **kwargs):
        assert 'mcode' in request.query_params, KeyError('mcode must be in query')
        mcode = request.query_params.get('mcode', None)
        assert 'start' in request.query_params, KeyError('start must be in query')
        start_date = request.query_params.get('start', None)
        end_date = request.query_params.get('end', datetime.today().strftime("%Y-%m-%d"))
        excel = ExcelChildActivityAnalyst(start=start_date, end=end_date, mcode=mcode)
        excel.process_data()
        response = HttpResponse(excel.response_file, content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename={}'.format(excel.file_name)
        return response

    @action(detail=False, methods=['GET'], permission_classes=(IsAuthenticated,))
    def export_sponsor_tree_activity_excel_dataframe(self, request, *args, **kwargs):
        assert 'honor' in request.query_params, KeyError('honor must be in query')
        honor = request.query_params.get('honor', None)
        assert 'start' in request.query_params, KeyError('start must be in query')
        start_date = request.query_params.get('start', None)
        end_date = request.query_params.get('end', datetime.today().strftime("%Y-%m-%d"))
        mcode_list = Member.objects.filter(
            status_terminate=0, status_suspend=0, honor=honor).values_list("mcode", flat=True)
        excel = ExcelDataFrameSponsorChild(start=start_date, end=end_date, mcode=mcode_list)
        file = excel.generate_excel
        response = HttpResponse(save_virtual_workbook(file.book), content_type='application/ms-excel')
        filename = date.today().strftime("%Y-%m-%d") + "_" + honor + "_sponsor_tree_analyst.xlsx"
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response
