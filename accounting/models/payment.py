from django.db import models
from core.models import AbstractBaseCode


class PaymentType(AbstractBaseCode):
    enable = models.BooleanField(default=True)
