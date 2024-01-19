import re
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

from event.models import PreAttendee
from event.serializers import MemberAttendeeSerializer
from member.models import Member
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route, permission_classes, action
from rest_framework.response import Response
from ..models import Event
from ..models import Attendee
from ..serializers import AttendeeSerializer
from ..serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        return super(EventViewSet, self).retrieve(request, *args, **kwargs)

    @action(detail=False, methods=['GET'], permission_classes=(AllowAny,))
    def search_member(self, request, *args, **kwargs):
        member_code = request.query_params.get('code', None)
        if member_code is None:
            return Response([], status=status.HTTP_200_OK)
        query = Member.objects.filter(Q(mcode__icontains=member_code) | Q(name_t__icontains=member_code))
        data = {}
        for x in query[:5]:
            data[x.mcode] = x.full_name
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'], permission_classes=(AllowAny,))
    def check_pre_attendee(self, request, pk, *args, **kwargs):
        dt = datetime.now()
        instance = self.get_object()
        member_code = request.query_params.get('code')
        is_exist = Attendee.objects.filter(event__id=pk, members__mcode=member_code).exists()
        if is_exist:
            member = Member.objects.get(mcode=member_code)
            serializer = MemberAttendeeSerializer(member)
            response = {
                'code': 10,
                'message': 'Duplicate register',
                'member': serializer.data
            }
            return Response(response, status=status.HTTP_409_CONFLICT)
        if instance.event_tag is None:
            time_check = False
        else:
            time_check = re.match(r'\w+:\w+', instance.event_tag)
        has_reg = Attendee.objects.filter(members__mcode=member_code).exists()

        if time_check:
            ref_time = instance.event_tag.split(':')
            ref_dt = dt.replace(hour=int(ref_time[0]), minute=int(ref_time[1]))
            diff = dt - ref_dt
            if diff.total_seconds() > 0:
                if has_reg:
                    return Response({"result": 'OK', 'skip': True}, status=status.HTTP_200_OK)
                else:
                    return Response({"result": 'OK', 'skip': False}, status=status.HTTP_200_OK)
            query = PreAttendee.objects.filter(event_id=pk, members__mcode=member_code)
            if len(query):
                if has_reg:
                    return Response({"result": 'OK', 'skip': True}, status=status.HTTP_200_OK)
                else:
                    return Response({"result": 'OK', 'skip': False}, status=status.HTTP_200_OK)
            else:
                return Response({"result": 'FAIL'}, status=status.HTTP_200_OK)
        else:
            if has_reg:
                return Response({"result": 'OK', 'skip': True}, status=status.HTTP_200_OK)
            else:
                return Response({"result": 'OK', 'skip': False}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'], permission_classes=(AllowAny,))
    def pre_register(self, request, pk, *args, **kwargs):
        try:
            data = request.data
            instance = self.get_object()
            register_type = data.get('group', 'member')
            member_code = data.get('code', None)
            member = Member.objects.get(mcode=member_code)
            query = PreAttendee.objects.filter(event_id=pk, members__mcode=member_code)
            if len(query):
                return Response({"result": 'fail', 'reason': 'already register'}, status=status.HTTP_409_CONFLICT)
            else:
                serializer = MemberAttendeeSerializer(member)
                pre_attendee = PreAttendee.objects.filter(event=instance, group=register_type)

                if len(pre_attendee) == 0:
                    pre_attendee = PreAttendee.objects.create(event=instance, group=register_type)
                else:
                    pre_attendee = pre_attendee.first()
                pre_attendee.members.add(member)
                return Response({"result": 'OK', 'data': serializer.data}, status=status.HTTP_200_OK)
        except (Http404, ValueError) as e:
            response = {
                'message': '{}'.format(e)
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], permission_classes=(AllowAny,))
    def register(self, request, *args, **kwargs):
        try:
            data = request.data
            instance = self.get_object()
            register_type = data.get('type', 'member')

            if register_type is None:
                raise ValueError('register type not defined')
            elif register_type == 'member' or register_type == 'person':

                # reg_data = data.get(register_type, None)
                #
                # if reg_data is None:
                #     raise ValueError('{} not defined'.format(register_type))

                route_to = getattr(self, 'register_{}'.format(register_type), None)

                if route_to is not None:
                    return route_to(instance=instance, data=data)
                else:
                    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except (Http404, ValueError) as e:
            response = {
                'message': '{}'.format(e)
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], permission_classes=(AllowAny,))
    def get_event(self, request, pk=None):
        current_date = datetime.now()
        queryset = Event.objects.filter(date=current_date).order_by('date')[:5]
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def get_attendees(self, request, pk=None):
        queryset = Event.objects.all().select_related('attendee').prefetch_related('attendee__members')
        try:
            event = get_object_or_404(queryset, pk=pk)
            serializer = AttendeeSerializer(event.attendee)
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], permission_classes=(AllowAny,))
    def get_register_count(self, request, pk=None):
        instance = self.get_object()
        if instance:
            attendee = self.get_attendee(instance)
            data = {
                'event': EventSerializer(instance).data,
                'count': attendee.members.count()
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_attendee(self, instance):
        attendee = None
        if hasattr(instance, 'attendee'):
            attendee = instance.attendee
        else:
            attendee = Attendee.objects.create(event=instance)
        return attendee

    def register_member(self, instance, data):
        mem_code = data.get('mcode')
        member = Member.objects.get(mcode=mem_code)
        serializer = MemberAttendeeSerializer(member)
        is_exist = Attendee.objects.filter(event=instance, members__mcode=mem_code).exists()
        if is_exist:
            response = {
                'code': 10,
                'message': 'Duplicate register',
                'member': serializer.data
            }
            return Response(response, status=status.HTTP_409_CONFLICT)
        else:
            save_flag = False
            if data.get('email', '') != '':
                member.email = data.get('email')
                save_flag = True
            if data.get('mobile', '') != '':
                member.mobile = data.get('mobile')
                save_flag = True
            if data.get('address', '') != '':
                member.address = data.get('address')
                save_flag = True
            if data.get('districtid', '') != '':
                member.districtid = data.get('districtid')
                save_flag = True
            if data.get('amphurid', '') != '':
                member.amphurid = data.get('amphurid')
                save_flag = True
            if data.get('provinceid', '') != '':
                member.provinceid = data.get('provinceid')
                save_flag = True
            if data.get('zip', '') != '':
                member.zip = data.get('zip')
                save_flag = True
            attendee = self.get_attendee(instance)
            attendee.members.add(member)
            if save_flag:
                member.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
