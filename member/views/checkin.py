from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.db.models import Sum
# from django.db.models.functions import TruncMonth, TruncDay, TruncYear, TruncQuarter
from datetime import datetime, timedelta, date

from ..serializers import MemberShortSerializer
from ..models import Member


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('mcode')
    serializer_class = MemberShortSerializer
    template_name = 'check_in_template.html'

    @list_route(renderer_classes=[renderers.TemplateHTMLRenderer])
    def blank_form(self, request, *args, **kwargs):
        serializer = MemberShortSerializer()
        return Response({'serializer': serializer})

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

# from django.shortcuts import render, redirect
# from django import forms
# from django.utils import timezone
# from django.http import HttpResponse
# from member.forms import CheckInMemberForm
# from ..models import Member


# def MemberCheckInView(request):
#     if request.method == "POST":
#         form = CheckInMemberForm(request.POST)
#         if form.is_valid():
#             model_instance = form.save(commit=False)
#             model_instance.timestamp = timezone.now()
#             model_instance.save()
#             return redirect('/member/checkin/')
#     else:
#         form = CheckInMemberForm()
#         return render(request, 'check_in_template.html', {'form': form})

# def MemberLogInView(request):
#     return render(request, 'login.html')

# def autocompleteModel(request):
#     if request.is_ajax():
#         q = request.GET.get('term', '')
#         membs = Member.objects.filter(mcode__icontains = q )[:20]
#         results = []
#         for me in membs:
#             resp = {}
#             resp['mcode'] = me.mcode
#             resp['name_t'] = me.name_t
#             results.append(resp)
#         data = json.dumps(results)
#     else:
#         data = 'fail'
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)

