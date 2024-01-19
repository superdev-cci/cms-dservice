from django.conf.urls import url
from .views import *

route_list = [
    {
        'path': r'api/commission/report',
        'view': CommissionReportView
    },
    {
        'path': r'api/analyzed/pvtransfer',
        'view': OrgScanPvView
    },
    {
        'path': r'api/commission/teamcms',
        'view': MemberOrgReportView
    },
    {
        'path': r'api/commission/weakstrong',
        'view': WeakStrongCurrentRoundView
    },
    {
        'path': r'api/fast_commission',
        'view': FastCommissionView
    },
    {
        'path': r'api/week_payment',
        'view': WeekPaymentView
    },
    {
        'path': r'api/sale_maintain',
        'view': SaleMaintainView
    },
    {
        'path': r'api/month_payment',
        'view': MonthPaymentView
    },
    {
        'path': r'api/honor_change',
        'view': HonorChangeLogView
    },
    {
        'path': r'api/summary_round',
        'view': SummaryRoundView
    },
    {
        'path': r'api/ws_summary',
        'view': WeakStrongSummaryView
    },
    # {
    #     'path': r'api/commission_b',
    #     'view': CommissionBReportView
    # },
]
