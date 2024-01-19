from .settings import *
# DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'cms.cciofficial.com',
        'NAME': 'cci_db',
        'USER': 'cms_agent',
        'PASSWORD': 'cMs!@54ze7',
        'PORT': '3311',
        'OPTIONS': {
            "init_command": "SET storage_engine=MYISAM",
            # 'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
            # 'charset': 'utf8',
            # 'use_unicode': True
        }
    }
}

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.AllowAny',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    # ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}
#
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://dev.p-enterprise.com:6379/0",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
#
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('dev.p-enterprise.com', 6379)],
#         },
#     },
# }
#
#
# # CELERY STUFF
# BROKER_URL = 'redis://dev.p-enterprise.com:6379'
# CELERY_RESULT_BACKEND = 'redis://dev.p-enterprise.com:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Bangkok'
