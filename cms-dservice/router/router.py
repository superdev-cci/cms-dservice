# from dynamic_rest.routers import DynamicRouter
from rest_framework import routers

globals_router = routers.SimpleRouter(trailing_slash=False)


def register_routes(route_list):
    for route in route_list:
        try:
            globals_router.register(route['path'], route['view'], base_name=route.get('name', None))
        except Exception as e:
            print(e)
    return
