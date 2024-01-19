from django.db import models
from core.models import AbstractBaseCode


class StatementType(AbstractBaseCode):
    use_app = models.CharField(max_length=32, default=" ")


class StatementState(AbstractBaseCode):
    use_app = models.CharField(max_length=32, default=" ")
