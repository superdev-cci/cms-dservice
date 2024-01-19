from __future__ import absolute_import
from celery import shared_task
from core.agent import LineNotifyAgentMixIn
from member import node
from member.functions.add_member_to_group import update_member_group
from member.schedulers.register_check import RegisterCheckup
from member.models import MemberDocumentCheckup
import util
import datetime
import requests
import os


@shared_task
def reindex__sponsor_tree_task():
    line_agent = LineNotifyAgentMixIn()
    p_time = datetime.datetime.now()
    node.calculate_sponsor_tree()
    end_time = util.print_time_delta(p_time, datetime.datetime.now())
    message = 'Member AGENT : Task <Reindex sponsor member> {} : Calculate time {}'.format('TestNotify',
                                                                                           end_time)
    line_agent.line_notify(message, 'TestNotify')


@shared_task
def reindex_task():
    line_agent = LineNotifyAgentMixIn()
    p_time = datetime.datetime.now()
    node.calculate_tree()
    node.calculate_sponsor_tree()
    end_time = util.print_time_delta(p_time, datetime.datetime.now())
    message = 'Member AGENT : Task <Reindex member> {} : Calculate time {}'.format('TestNotify',
                                                                                   end_time)
    update_member_group()
    line_agent.line_notify(message, 'TestNotify')


@shared_task
def binary_snap():
    line_agent = LineNotifyAgentMixIn()
    message = 'Member AGENT : Task <Snap structure> {} : {}'.format('TestNotify',
                                                                    datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
    try:
        host = os.environ.get('CMS_HOST', 'cms.cciofficial.com')
        protocol = os.environ.get('CMS_HTTP', 'https')
        r = requests.get('{}://{}/backoffice/api/reindex_binary.php'.format(protocol, host), timeout=None)
    except:
        pass
    return


@shared_task
def document_check_up():
    line_agent = LineNotifyAgentMixIn()
    executor = RegisterCheckup()
    try:
        suspend = executor.process_check_document()
        terminate = executor.process_terminate()
        MemberDocumentCheckup.objects.create(suspend=suspend, terminate=terminate)
        message = 'Routine AGENT : Task <Document checkup> : {} Success'.format(
            datetime.datetime.now().strftime('%H:%M:%S'))
    except:
        message = 'Routine AGENT : Task <Document checkup> : {} Failure'.format(
            datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
    return
