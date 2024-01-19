from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.core import urlresolvers

urls = urlresolvers.get_resolver()
from django.conf.urls import RegexURLPattern, RegexURLResolver


def if_none(value):
    if value:
        return value
    return ''


def print_urls(urls, parent_pattern=None):
    for url in urls.url_patterns:
        if isinstance(url, RegexURLResolver):
            print_urls(url, if_none(parent_pattern) + url.regex.pattern)
        elif isinstance(url, RegexURLPattern):
            print(if_none(parent_pattern) + url.regex.pattern)


class CommissionCalculateBlockMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass
        # print('Process view CommissionCalculateBlockMiddleware')
