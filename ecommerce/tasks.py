from __future__ import absolute_import
from celery import shared_task
from core.agent import LineNotifyAgentMixIn
from .report import SoldDailySummary, SoldMonthlySummary
from ecommerce.models import SaleInvoice
import datetime
from datetime import timedelta


@shared_task
def ticker_task():
    line_agent = LineNotifyAgentMixIn()
    message = 'Ecommerce AGENT : Task Hello from {} : {}'.format('	TestNotify',
                                                                 datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')


@shared_task
def sale_summary():
    line_agent = LineNotifyAgentMixIn()
    daily_sale = SoldDailySummary()
    month_sale = SoldMonthlySummary()
    message = 'Ecommerce AGENT :\n'
    message += daily_sale.process_notify()
    # message = 'Sale summary task say Hello from {} : {}' \
    #     .format('TestNotify',
    #             datetime.datetime.now().strftime('%H:%M:%S'))
    message += '\nยอดขายเดือนนี้ : {:,} บาท'.format(month_sale.monthly_summary)
    # message += '\nยอดเครคิดท่องเที่ยวที่จ่ายเดือนนี้ : {:,} บาท'.format(month_sale.monthly_summary_tc)
    line_agent.line_notify(message, 'ComisionSystem')


@shared_task
def order_remover():
    line_agent = LineNotifyAgentMixIn()
    last_day = datetime.date.today() - timedelta(days=6)
    queryset = SaleInvoice.objects.filter(bill_state__in=['OR', 'PP'], order_number__isnull=False,
                                          sadate__lte=last_day)
    total_order = queryset.count()
    queryset.update(cancel=1, remark='System Order expired', bill_state='CA')
    message = 'Ecommerce AGENT : Daily order remove total: {}'.format(total_order)
    line_agent.line_notify(message, 'TestNotify')


@shared_task
def run_every():
    line_agent = LineNotifyAgentMixIn()
    message = 'Run every 1 hour say Hello from {} : {}' \
        .format('TestNotify',
                datetime.datetime.now().strftime('%H:%M:%S'))
    line_agent.line_notify(message, 'TestNotify')
