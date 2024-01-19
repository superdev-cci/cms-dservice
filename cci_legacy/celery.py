from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cci_legacy.settings')

app = Celery('cci_legacy')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
# app.conf.timezone = 'UTC'


# app.conf.beat_schedule = {
#     'ticker': {
#         'task': 'commission.tasks.hold_expired_task',
#         'schedule': crontab(), # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
#     },
# }


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
