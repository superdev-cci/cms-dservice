from django.db import models
from core.models import AbstractBaseCode


class MemberGroup(AbstractBaseCode):
    """
    a class model represent a member group
    This class inherit class `AbstractBaseCode` receive attribute from `AbstractBaseCode`
    """
    status_qualified = models.IntegerField(default=0)

    class Meta:
        ordering = ('-name',)


class ClientVatType(AbstractBaseCode):

    class Meta:
        ordering = ('-name',)
