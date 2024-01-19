from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings


# Create your views here.
def env_check(request):
    data = {k: v for k, v in os.environ.items()}
    if 'DB_PASSWORD' in data:
        data['DB_PASSWORD'] = '*********'
    data['DATABASE'] = settings.DATABASES['default']['HOST']
    data['PORT'] = settings.DATABASES['default']['PORT']
    data['APP_VERSION'] = os.environ.get('APP_VERSION')
    data['VERSION_NAME'] = os.environ.get('VERSION_NAME')
    data['BUILD_NUMBER'] = os.environ.get('BUILD_NUMBER')

    return JsonResponse({
        "status": 'OK',
        "evn": data
    })
