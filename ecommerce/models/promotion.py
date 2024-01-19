from django.db import models

from core.models import AbstractBaseProductItem


class DropShipPromotionType(models.Model):
    """
    a class represent a promotional dropship's type
    """
    name = models.CharField(max_length=32)
    meta = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class DropShipPromotion(models.Model):
    """
    a class represent a promotional dropship
    """
    name = models.CharField(max_length=32)
    types = models.ManyToManyField(DropShipPromotionType, blank=True)
    items = models.ManyToManyField('ProductClass', blank=True)
    formula = models.CharField(max_length=64)
    priority = models.IntegerField(default=0)
    ship_prices = models.CharField(max_length=32, default='(0,0)')

    def __str__(self):
        return self.name


class Promotion(AbstractBaseProductItem):
    """
    a class represent a promotional products
    """
    sa_type = models.CharField(max_length=2, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    pv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    special_pv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    qty = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    st = models.IntegerField(blank=True, null=True)
    sst = models.IntegerField(blank=True, null=True)
    bf = models.IntegerField(blank=True, null=True)
    ato = models.IntegerField(blank=True, null=True)
    ud = models.CharField(max_length=1, blank=True, null=True)
    locationbase = models.CharField(max_length=255, blank=True, null=True)
    pos_mb = models.IntegerField(blank=True, null=True)
    pos_su = models.IntegerField(blank=True, null=True)
    pos_ex = models.IntegerField(blank=True, null=True)
    pos_br = models.IntegerField(blank=True, null=True)
    pos_si = models.IntegerField(blank=True, null=True)
    pos_go = models.IntegerField(blank=True, null=True)
    pos_pl = models.IntegerField(blank=True, null=True)
    pos_pe = models.IntegerField(blank=True, null=True)
    pos_ru = models.IntegerField(blank=True, null=True)
    pos_sa = models.IntegerField(blank=True, null=True)
    pos_em = models.IntegerField(blank=True, null=True)
    pos_di = models.IntegerField(blank=True, null=True)
    pos_bd = models.IntegerField(blank=True, null=True)
    pos_bl = models.IntegerField(blank=True, null=True)
    pos_cd = models.IntegerField(blank=True, null=True)
    pos_id = models.IntegerField(blank=True, null=True)
    pos_pd = models.IntegerField(blank=True, null=True)
    pos_rd = models.IntegerField(blank=True, null=True)
    vat = models.IntegerField(default=7)
    activated = models.BooleanField(default=False)

    class Meta:
        db_table = 'ali_product_package'

    @property
    def all_item_price(self):
        """
        a method represent full products's price

        :return: (decimal): summary products price in promotion
        """
        total = 0
        for x in self.items.all():
            total += x.qty * x.product.price
        return total

    @property
    def prices_factor(self):
        """
        a method represent ratio promotion price per summary products price in promotion

        :return: (float): ratio
        """
        return self.price / self.all_item_price


class PromotionItem(models.Model):
    """
    a class represent a products in promotional product
    """
    package = models.CharField(max_length=20)
    promotion = models.ForeignKey('Promotion', on_delete=models.CASCADE, null=True, blank=True, related_name='items')
    pcode = models.CharField(max_length=20)
    pdesc = models.CharField(max_length=100)
    qty = models.IntegerField()
    mdate = models.DateField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'ali_product_package1'
