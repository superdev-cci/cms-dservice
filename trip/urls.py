from django.conf.urls import url
from .views import *

route_list = [
    {
        'path': r'api/trip',
        'view': TripView
    },
    {
        'path': r'api/travel_point',
        'view': TravelPointUseStatementView
    },
    {
        'path': r'api/travel_point_stack',
        'view': TravelPointStackView
    },
]
