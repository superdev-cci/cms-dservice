from django.conf.urls import url
from .views import *
route_list = [
    {
        'path': r'logs/hpv',
        'view': LogHpvView
    },
    {
        'path': r'logs/general',
        'view': LogView
    },
]

urlpatterns = [
    # url(r'checkin/$', MemberCheckInView),
    # url(r'login/$', MemberLogInView),
    # url(r'mcode/search/', autocompleteModel),
]