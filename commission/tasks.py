from __future__ import absolute_import
import os
import requests
from celery import shared_task
from core.agent import line
import datetime
from commission.functions.pv import stack_check


@shared_task
def hold_expired():
    line_agent = line.LineNotifyAgentMixIn()
    message = 'PV AGENT : Task <HoldExpired> {} : {}'.format('TestNotify',
                                                             datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
    try:
        host = os.environ.get('CMS_HOST', 'cms.cciofficial.com')
        protocol = os.environ.get('CMS_HTTP', 'http')
        url = '{}://{}/api/commission/hold_expired.php'.format(protocol, host)
        r = requests.get(url, timeout=None)
    except Exception as e:
        print(e)
    return


@shared_task
def pv_stack_check():
    total, message = stack_check.check_stack_pv()
    line_agent = line.LineNotifyAgentMixIn()
    if total:
        line_agent.line_notify(message, 'TestNotify')
    else:
        print('{} : Pv system is healthy'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%m:%S')))
    return
