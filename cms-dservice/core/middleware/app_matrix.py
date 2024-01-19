from prometheus_client import Gauge
from django.utils.deprecation import MiddlewareMixin
from ecommerce.report import SoldDailySummary
from datetime import date
from member.models import MemberActive
from commission.models import HoldPvStack
from commission.report.holdpv_activity import PvActivityReport

connections_total = Gauge('cms_django_active_member', 'Counter of active connections')
bkk_sales = Gauge('cms_django_bkk_sales', 'Sales value for BKK branch')
bkk02_sales = Gauge('cms_django_bkk02_sales', 'Sales value for BKK02 branch')
cri01_sales = Gauge('cms_django_cri01_sales', 'Sales value for CRI01 branch')
hy01_sales = Gauge('cms_django_hy01_sales', 'Sales value for HY01 branch')
kl01_sales = Gauge('cms_django_kl01_sales', 'Sales value for KL01 branch')
total_sales = Gauge('cms_django_total_sales', 'Sales value for All branch')
hold_pv = Gauge('cms_django_hold_pv_total', 'Hold pv in system')
hold_pv_out = Gauge('cms_django_hold_pv_out', 'Hold pv transfer out in system')
hold_pv_in = Gauge('cms_django_hold_pv_in', 'New Hold pv in system')
hold_pv_transfer = Gauge('cms_django_hold_pv_transfer', 'Hold pv transfer in system')


class CmsMatrixMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/prometheus/metrics':
            active_user = MemberActive.get_active_connection()
            connections_total.set(active_user)

            # Sales data
            sales_data = SoldDailySummary().daily_summary()
            bkk_sales.set(sales_data.get('BKK01', 0))
            bkk02_sales.set(sales_data.get('BKK02', 0))
            cri01_sales.set(sales_data.get('CRI01', 0))
            hy01_sales.set(sales_data.get('HY01', 0))
            kl01_sales.set(sales_data.get('KL01', 0))
            total_sales.set(sales_data.get('total', 0))

            # Commission
            hold_pv.set(HoldPvStack.all_hold_pv())
            # Pv activity
            activity_hpv = PvActivityReport(get_type='daily')
            activity_hpv_data = activity_hpv.result
            today = date.today().strftime('%Y-%m-%d')
            activity_hpv_instance = activity_hpv_data.get(today, None)
            if activity_hpv_instance is not None:
                hold_pv_out.set(activity_hpv_instance.get('out', 0))
                hold_pv_in.set(activity_hpv_instance.get('in', 0))
                hold_pv_transfer.set(activity_hpv_instance.get('transfer', 0))
            else:
                hold_pv_out.set(0)
                hold_pv_in.set(0)
                hold_pv_transfer.set(0)

        return
