from django.db import models
from datetime import datetime, date

from django.db.models import Sum


class TravelPointStack(models.Model):
    member = models.ForeignKey('member.Member', blank=True, on_delete=models.CASCADE)
    stamp_date = models.DateField(default=date.today)
    gold_point = models.IntegerField(default=0)
    silver_point = models.IntegerField(default=0)
    remaining_gold_point = models.IntegerField(default=0)
    remaining_silver_point = models.IntegerField(default=0)

    class Meta:
        ordering = ('stamp_date',)

    @staticmethod
    def get_gold_coin(member):
        queryset = TravelPointStack.objects.filter(remaining_gold_point__gt=0, member=member).aggregate(
            total_gold=Sum('remaining_gold_point'))
        result = queryset.get('total_gold', 0)
        return result if result is not None else 0

    @staticmethod
    def get_silver_coin(member):
        queryset = TravelPointStack.objects.filter(remaining_silver_point__gt=0, member=member).aggregate(
            total_silver=Sum('remaining_silver_point'))
        result = queryset.get('total_silver', 0)
        return result if result is not None else 0


class TravelPointUseStatement(models.Model):
    STATE_TYPE_CHOICE = (
        ('CA', 'Cancel'),
        ('CM', 'Completed'),
    )
    bill_number = models.CharField(max_length=32, null=True, blank=True)
    member = models.ForeignKey('member.Member', null=True, blank=True, on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', null=True, blank=True, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today)
    gold_coin = models.IntegerField(default=0)
    silver_coin = models.IntegerField(default=0)
    state = models.CharField(max_length=2, choices=STATE_TYPE_CHOICE, blank=True, null=True)

    class Meta:
        ordering = ('-issue_date',)

    @staticmethod
    def get_total_coin(trip, member):
        queryset = TravelPointUseStatement.objects.filter(trip=trip, member=member, state='CM').aggregate(
            total_gold=Sum('gold_coin'), total_silver=Sum('silver_coin'))
        return queryset

    @staticmethod
    def generate_bill_number():
        dt = datetime.today()
        prefix = "TP{}".format(dt.strftime('%y%m'))
        queryset = TravelPointUseStatement.objects.filter(bill_number__startswith=prefix).order_by('-id')
        if len(queryset) == 0:
            running_number = 1
        else:
            try:
                running_number = queryset.first().bill_number[-4:]
            except Exception as e:
                running_number = None

            if running_number is None:
                running_number = 1
            else:
                running_number = int(running_number)
                running_number += 1

        return 'TP{}{:04}'.format(dt.strftime('%y%m'), running_number)
