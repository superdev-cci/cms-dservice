from django.db import models


class NoticeInformation(models.Model):
    head = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    dates = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1)
    popup = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ali_news'

