from django.db import models


class ShippingBox(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    height = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    active = models.FloatField(default=True)
    max_weight = models.FloatField(default=1)
    inbound_cost = models.FloatField(default=0)
    outbound_cost = models.FloatField(default=0)
    space_margin = models.FloatField(default=1)

    def __str__(self):
        return "{} : {:,} ".format(self.name, self.volume)

    @property
    def volume(self):
        return (self.height * self.length * self.width) * self.space_margin
