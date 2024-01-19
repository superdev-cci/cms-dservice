from django.db import models
from datetime import datetime, timedelta


class MemberActive(models.Model):
    member = models.CharField(max_length=64, blank=True, primary_key=True)
    last_seen = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'matrix_memberactive'
        ordering = ['-last_seen']
        managed = False

    def __str__(self):
        return '{} : {}'.format(self.member.mcode, self.last_seen.strftime('%Y-%m-%d'))

    @staticmethod
    def get_active_connection():
        last_seen = datetime.now() - timedelta(minutes=15)
        queryset = MemberActive.objects.filter(last_seen__gte=last_seen)
        return queryset.count()


class MemberDocumentCheckup(models.Model):
    date_issue = models.DateTimeField(blank=True, auto_now=True, primary_key=True)
    suspend = models.IntegerField(default=0)
    terminate = models.IntegerField(default=0)

    def __str__(self):
        return '{} : S->{} , T-> {}'.format(self.date_issue.strftime('%Y-%m-%d'), self.suspend, self.terminate)
