from django.db import models
from datetime import datetime, date


class LogTravelPoint(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    date_issue = models.DateField(default=date.today)
    statement = models.CharField(max_length=255, null=True, blank=True)
    silver_in = models.IntegerField(default=0)
    silver_out = models.IntegerField(default=0)
    gold_in = models.IntegerField(default=0)
    gold_out = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    remark = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'TravelPoint log'
