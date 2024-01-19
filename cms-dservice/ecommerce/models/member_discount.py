from django.db import models


class MemberDiscount(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True, blank=True)
    date_issue = models.DateField(auto_now_add=True)
    expired_date = models.DateField(null=True, blank=True)
    value = models.FloatField(default=0)
    remaining = models.FloatField(default=0)

    def __str__(self):
        return '{} : {}'.format(self.member, self.value)
