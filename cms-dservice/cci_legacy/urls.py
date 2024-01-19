"""cci_legacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from router.router import globals_router, register_routes
from account.urls import route_list as account_routes
from accounting.urls import route_list as accounting_routes
from ecommerce.urls import route_list as ecom_routes
from event.urls import route_list as event_routes
from branch.urls import route_list as branch_routes
from trip.urls import route_list as trip_routes
from commission.urls import route_list as commission_routes
from member.urls import route_list as member_routes
from system_log.urls import route_list as logs_routes

router_list = account_routes + \
              accounting_routes + \
              ecom_routes + \
              branch_routes + \
              trip_routes + \
              commission_routes + \
              member_routes + \
              event_routes + \
              logs_routes

register_routes(router_list)

urlpatterns = [
    url(r'^', include(globals_router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^member/', include('member.urls')),
    url(r'^system/', include('system.urls')),
    url(r'^prometheus/', include('django_prometheus.urls')),
]
