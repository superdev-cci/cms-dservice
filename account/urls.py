from rest_framework import routers
from django.conf.urls import url, include
from .views import UserViewSet, GroupViewSet
from .views import LoginView
from .views import LogoutView
from .views import RefreshView

route_list = [
    {
        'path': r'account/staff',
        'view': UserViewSet
    },
    {
        'path': r'account/group',
        'view': GroupViewSet
    },
]

urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='token'),
    url(r'logout/$', LogoutView.as_view(), name="revoke-token"),
    url(r'refresh/$', RefreshView.as_view(), name='token'),
    # url(r'^', include(router.urls))
]
