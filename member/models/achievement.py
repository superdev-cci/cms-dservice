from django.db import models
from core.models import AbstractBaseCode
from datetime import date


class Achievement(AbstractBaseCode):
    """
    a class model represent a member achievement
    This class inherit class `AbstractBaseCode` receive attribute from `AbstractBaseCode`
    """
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    stamp_date = models.DateField(default=date.today)
    status = models.BooleanField(default=True)
