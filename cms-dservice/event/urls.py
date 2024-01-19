from .views import EventViewSet

route_list = [
    {
        'path': r'api/events/event',
        'view': EventViewSet
    },
]
