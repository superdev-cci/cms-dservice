from __future__ import absolute_import
import os
import requests
from celery import shared_task
from core.agent import line
import datetime
from django.db.models import Q
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from system_log.models import LogTravelCredit
from trip.models import TravelPointStack
from member.models import Member


@shared_task
def wipe_all_travel_credit():
    line_agent = line.LineNotifyAgentMixIn()
    queryset = Member.objects.filter(tc_value__gt=0)
    logs = [LogTravelCredit(mcode=x.mcode, inv_code='System', sadate=datetime.date.today(), satime="00:00:00",
                            sano='CREDIT EXP', value_in=0, value_out=x.tc_value, total=0,
                            uid='System', sa_type='', value_option="Monthly Expired"
                            ) for x in queryset]
    LogTravelCredit.objects.bulk_create(logs)
    queryset.update(tc_value=0)
    message = 'System AGENT : Task <Travel credit expired> {} : {}'.format('TestNotify',
                                                                           datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
    return
