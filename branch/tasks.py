from __future__ import absolute_import
from celery import shared_task
from branch.functions.snap_stock import BranchSnapStockCard
from branch.functions.item_stock import link_record
from core.agent import LineNotifyAgentMixIn


@shared_task
def sale_snap_stock():
    line_agent = LineNotifyAgentMixIn()
    stamp = BranchSnapStockCard()
    message = 'Stock AGENT :\n'
    message += 'Stock card stamp '
    try:
        link_record()
        stamp.create()
        message += 'success !!'
    except Exception as e:
        message += 'fail !!\n'
        message += e.__str__()
    line_agent.line_notify(message, 'TestNotify')

