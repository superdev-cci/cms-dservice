from django.db import models
from core.models import AbstractBaseProductItem


class ProductClass(models.Model):
    """
       a class model represent product class design for dropship shipment rule
       """
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Product Class'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(AbstractBaseProductItem):
    """
    a class model represent product detail
    """
    group_id = models.IntegerField()
    personel_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ud = models.CharField(max_length=1, blank=True)
    sync = models.CharField(max_length=1, blank=True, null=True)
    web = models.CharField(max_length=1, blank=True, null=True)
    st = models.IntegerField(blank=True, null=True)
    sst = models.IntegerField(blank=True, null=True)
    bf = models.IntegerField(blank=True, null=True)
    sh = models.CharField(max_length=1, blank=True, null=True)
    pcode_stock = models.CharField(max_length=20, blank=True, null=True)
    sup_code = models.CharField(max_length=255, blank=True, null=True)
    sa_type_a = models.IntegerField(blank=True, null=True)
    sa_type_h = models.IntegerField(blank=True, null=True)
    qtyr = models.IntegerField(blank=True, null=True)
    ato = models.IntegerField(blank=True, null=True)

    # Add on attribute
    product_class = models.ForeignKey('ProductClass', null=True, blank=True, on_delete=models.SET_NULL)
    height = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)

    buffer_stock = models.IntegerField(blank=True, null=True, default=0)
    safety_stock = models.IntegerField(blank=True, null=True, default=0)

    carton_size = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        db_table = 'ali_product'
        verbose_name_plural = 'Product'
        ordering = ('pcode',)

    def __str__(self):
        return '{} : {}'.format(self.pcode, self.pdesc)

    @property
    def volume(self):
        return self.height * self.length * self.width


class ProductCategory(models.Model):
    """
    a class models represent product's category
    """
    groupname = models.CharField(max_length=250)
    bf_ref = models.CharField(max_length=25)

    class Meta:
        db_table = 'ali_productgroup'
        verbose_name_plural = 'Product Category'
