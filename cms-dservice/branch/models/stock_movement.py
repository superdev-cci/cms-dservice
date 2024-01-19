from django.db import models


class StockStatement(models.Model):
    client_code = models.CharField(max_length=16, db_column='mcode')
    client_name = models.CharField(max_length=255, db_column='name_t')
    # client = models.ForeignKey('member.Member', on_delete=models.SET_NULL, blank=True, null=True)
    branch_name = models.CharField(max_length=32, db_column='inv_code')
    # branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, blank=True, null=True)
    from_branch = models.CharField(max_length=32, db_column='inv_ref', null=True, blank=True)
    to_branch = models.CharField(max_length=32, db_column='inv_action', null=True, blank=True)
    bill_number = models.CharField(max_length=64, db_column='sano')
    sano_ref = models.CharField(max_length=64, blank=True, null=True)
    pcode = models.CharField(max_length=32)
    # product = models.ForeignKey('ecommerce.Product', on_delete=models.SET_NULL, blank=True, null=True)
    pdesc = models.CharField(max_length=255)
    in_qty = models.IntegerField(default=0)
    in_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    in_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    out_qty = models.IntegerField(default=0)
    out_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    out_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    date_issue = models.DateField(auto_now_add=True, db_column='sadate')
    rdate = models.DateTimeField(auto_now_add=True, db_column='rdate')
    rccode = models.CharField(max_length=16, null=True, blank=True)
    bring_forward = models.IntegerField(null=True, blank=True, db_column='yokma')
    balance = models.IntegerField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    uid = models.CharField(max_length=32)
    action = models.CharField(max_length=16)
    cancel = models.IntegerField(default=0)

    class Meta:
        db_table = 'ali_stockcard_s'
        ordering = ('-id', )