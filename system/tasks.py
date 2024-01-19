from __future__ import absolute_import
import os
import requests
from celery import shared_task
from core.agent import line
import datetime
from django.db.models import Q
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from system_log.models import LogTravelPoint
from trip.models import TravelPointStack


@shared_task
def daily_calculate():
    line_agent = line.LineNotifyAgentMixIn()
    message = 'System AGENT : Task <daily position calculate> {} : {}'.format('TestNotify',
                                                                              datetime.datetime.now().strftime(
                                                                                  '%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
    try:
        host = os.environ.get('CMS_HOST', 'cms.cciofficial.com')
        protocol = os.environ.get('CMS_HTTP', 'http')
        r = requests.get('{}://{}/backoffice/cron_position.php'.format(protocol, host), timeout=None)
    except:
        pass
    return


@shared_task
def daily_snap_binary_calculate():
    line_agent = line.LineNotifyAgentMixIn()
    message = 'System AGENT : Task <SnapBinaryTree> {} : {}'.format('TestNotify',
                                                                    datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
    try:
        host = os.environ.get('CMS_HOST', 'cms.cciofficial.com')
        protocol = os.environ.get('CMS_HTTP', 'http')
        r = requests.get('{}://{}/backoffice/api/reindex_binary.php'.format(protocol, host), timeout=None)
    except:
        pass
    return


@shared_task
def wipe_all_travel_point():
    line_agent = line.LineNotifyAgentMixIn()
    last_day = datetime.date.today().replace(day=1)
    queryset = TravelPointStack.objects.select_related('member').filter(
        Q(remaining_silver_point__gt=0) | Q(remaining_gold_point__gt=0), stamp_date__lt=last_day)
    logs = [LogTravelPoint(member=x.member,
                           silver_out=x.remaining_silver_point,
                           gold_out=x.remaining_gold_point,
                           remark='Point expired'
                           ) for x in queryset]
    LogTravelPoint.objects.bulk_create(logs)
    queryset.update(remaining_silver_point=0, remaining_gold_point=0)
    message = 'System AGENT : Task <Travel point expired> {} : {}'.format('TestNotify',
                                                                          datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
    return
