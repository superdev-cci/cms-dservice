from django.db import models


class LogTravelCredit(models.Model):
    mcode = models.CharField(max_length=255)
    inv_code = models.CharField(max_length=255)
    sadate = models.DateField()
    satime = models.TimeField()
    sano = models.CharField(max_length=255)
    value_in = models.DecimalField(db_column='_in', max_digits=15,
                                   decimal_places=2)  # Field renamed because it started with '_'.
    value_out = models.DecimalField(db_column='_out', max_digits=15,
                                    decimal_places=2)  # Field renamed because it started with '_'.
    total = models.DecimalField(max_digits=15, decimal_places=2)
    uid = models.CharField(max_length=255)
    sa_type = models.CharField(max_length=255)
    value_option = models.CharField(db_column='_option', max_length=255)  # Field renamed because it started with '_'.

    class Meta:
        verbose_name_plural = 'TravelCredit log'
