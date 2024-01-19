# from django.contrib.postgres.fields import JSONField
from django.db import models


class AbstractBaseProductItem(models.Model):
    pv_factor = 5.5
    credits_charge = 3.5

    pcode = models.CharField(primary_key=True, max_length=20)
    pdesc = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    customer_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bprice = models.DecimalField(max_digits=15, decimal_places=2)
    vat = models.DecimalField(max_digits=15, decimal_places=2)
    pv = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    weight = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    fdate = models.DateField(blank=True, null=True)
    tdate = models.DateField(blank=True, null=True)
    # name = models.CharField(max_length=64, default=" ")
    # display_name = JSONField(default={'en': '...', 'th': '...'})
    # description = JSONField(default={'en': '...', 'th': '...'})
    locationbase = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    product_img = models.CharField(max_length=255, blank=True, null=True)
    activated = models.BooleanField(default=True)

    cost = models.FloatField(default=0)

    class Meta:
        abstract = True

    # @property
    # def short_description(self):
    #     desp = self.description.get('en', '...')
    #     return desp
    #
    # def get_display_name(self, key):
    #     return self.display_name.get(key, '...')

    @property
    def charge_prices(self):
        return float(float(self.price) * (self.credits_charge / 100))

    @property
    def net_prices(self):
        return float(self.price * 100 / 107)

    @property
    def margin(self):
        start_cost = (float(self.pv) * self.pv_factor) + self.cost + self.charge_prices
        if self.price == 0:
            return 0
        cost_percent = 1 - (float(start_cost) / float(self.price))
        return round(cost_percent * 100, 4)

    @property
    def margin_net(self):
        start_cost = (float(self.pv) * self.pv_factor) + self.cost + self.charge_prices
        if self.net_prices == 0:
            return 0
        cost_percent = 1 - (float(start_cost) / self.net_prices)
        return round(cost_percent * 100, 4)
