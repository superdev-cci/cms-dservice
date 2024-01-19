from django.contrib.postgres.fields import JSONField
from django.db import models


class ServiceSetting(models.Model):
    name = models.CharField(max_length=64)
    enable = models.BooleanField(default=False)
    meta = JSONField(null=True, blank=True)
