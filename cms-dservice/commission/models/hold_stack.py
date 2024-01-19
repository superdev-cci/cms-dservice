from django.db import models
from django.db.models import Sum
import datetime


# Create your models here.
class HoldPvStack(models.Model):
    TYPE_CHOICE = (
        ('S', 'Sale'),
        ('T', 'Transfer'),
    )

    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True)
    stamp_date = models.DateField(default=datetime.date.today, db_column='stampDate')
    pv = models.IntegerField(default=0)
    remaining = models.IntegerField(default=0)
    offset_day = models.IntegerField(default=0)
    stack_type = models.CharField(max_length=4, choices=TYPE_CHOICE, blank=True, null=True, default='S')

    class Meta:
        db_table = 'hold_expire'

    @staticmethod
    def all_hold_pv():
        queryset = HoldPvStack.objects.filter(remaining__gt=0).aggregate(total_pv=Sum('remaining'))
        return queryset.get('total_pv', 0)
