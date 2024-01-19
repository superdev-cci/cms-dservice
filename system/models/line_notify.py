from django.db import models


class LineAgent(models.Model):
    agent = models.CharField(max_length=64)
    token = models.CharField(max_length=128)
    enable = models.BooleanField(default=False)
