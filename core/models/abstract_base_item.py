from django.db import models


class AbstractBaseItem(models.Model):
    """
    a Base class model have only attribute `name`
    """
    name = models.CharField(max_length=64, default=" ")

    class Meta:
        abstract = True
