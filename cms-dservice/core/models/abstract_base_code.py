from django.db import models
from .abstract_base_item import AbstractBaseItem


class AbstractBaseCode(AbstractBaseItem):
    """
    a Base class model have only attribute `code`
    This class inherit class `AbstractBaseItem` receive attribute from `AbstractBaseItem`
    """
    code = models.CharField(max_length=4, default=" ")

    class Meta:
        abstract = True

    def __str__(self):
        return self.code
