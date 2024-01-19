from django.conf.urls import url
from .views import MemberView, MemberFavorite, MemberStatusView, MemberMatrixView, NoticeInformationView, \
    AchievementView, MemberSocialTagConfigView

route_list = [
    {
        'path': r'api/member',
        'view': MemberView
    },
{
        'path': r'api/social_tag',
        'view': MemberSocialTagConfigView
    },
    {
        'path': r'api/member_favorite',
        'view': MemberFavorite
    },
    {
        'path': r'api/member_status',
        'view': MemberStatusView
    },
    {
        'path': r'matrix/member',
        'view': MemberMatrixView
    },
    {
        'path': r'api/member_achievement',
        'view': AchievementView
    },
    {
        'path': r'api/notice',
        'view': NoticeInformationView
    }
]

urlpatterns = [
    # url(r'checkin/$', MemberCheckInView),
    # url(r'login/$', MemberLogInView),
    # url(r'mcode/search/', autocompleteModel),
]
